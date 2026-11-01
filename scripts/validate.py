#!/usr/bin/env python3
"""Validate the published research package without opening the source archive."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        return None


coverage = read_json(ROOT / "coverage.json")
source = read_json(ROOT / "source-verification.json")
records = 0
if coverage is not None:
    participants = coverage.get("participants", [])
    require(len(participants) == 25, "Ожидалось 25 участников")
    author_ids: set[int] = set()
    all_ids: set[int] = set()
    snapshot_ids = set(coverage.get("other_authors", {}).get("read_post_ids", []))
    snapshot_ids.update(i for part in participants for i in part.get("read_post_ids", []))
    for p in participants:
        aid = p.get("author_id")
        require(isinstance(aid, int) and aid not in author_ids, f"Повторный/неверный author_id: {aid}")
        author_ids.add(aid)
        ids = p.get("read_post_ids", [])
        unique_ids = set(ids)
        require(len(ids) == len(unique_ids), f"{aid}: повтор post_id")
        require(not all_ids.intersection(unique_ids), f"{aid}: post_id встречается у другого автора")
        all_ids.update(unique_ids)
        require(p.get("post_count", 0) >= 100, f"{aid}: автор ниже порога")
        require(len(ids) == p.get("post_count") == p.get("read_count"), f"{aid}: расходится охват")
        require(not p.get("unread_post_ids"), f"{aid}: есть непрочитанные ID")
        chapter = ROOT / "participants" / f"{aid}.md"
        facts = ROOT / "factchecks" / f"{aid}.jsonl"
        require(chapter.is_file(), f"{aid}: отсутствует глава")
        if not facts.is_file():
            errors.append(f"{aid}: отсутствует реестр")
            continue
        count = 0
        for number, line in enumerate(facts.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except ValueError as exc:
                errors.append(f"{facts.relative_to(ROOT)}:{number}: {exc}")
                continue
            count += 1
            if not isinstance(obj, dict):
                errors.append(f"{aid}:{number}: ожидался объект")
                continue
            require(bool(obj.get("claim") or obj.get("assertion")), f"{aid}:{number}: нет утверждения")
            require(bool(obj.get("verdict")), f"{aid}:{number}: нет вердикта")
            post_ids = obj.get("post_ids", [obj.get("post_id")])
            if not isinstance(post_ids, list):
                post_ids = [post_ids]
            require(bool(post_ids) and all(isinstance(i, int) and i in snapshot_ids for i in post_ids),
                    f"{aid}:{number}: post_id отсутствует в снимке")
            # Некоторые записи описывают непроверенный личный результат; там внешнего источника может не быть.
            require("sources" in obj or "source_urls" in obj, f"{aid}:{number}: нет поля источников")
        require(count == p.get("factcheck_entries"), f"{aid}: неверное число проверок")
        records += count
    other = coverage.get("other_authors", {})
    other_ids = other.get("read_post_ids", [])
    require(len(other_ids) == len(set(other_ids)) == other.get("post_count") == 2890,
            "Не совпадает охват авторов ниже порога")
    require(not set(other_ids).intersection(all_ids), "ID ниже порога пересекаются с отобранными авторами")
    all_ids.update(other_ids)
    blocks = other.get("chronological_blocks", [])
    block_ids = [i for block in blocks for i in block.get("read_post_ids", [])]
    require(len(block_ids) == len(set(block_ids)) and set(block_ids) == set(other_ids),
            "Хронологические блоки не совпадают с охватом авторов ниже порога")
    require(len(all_ids) == coverage.get("snapshot_posts") == 33410, "Общий охват не равен снимку")
    require(coverage.get("unique_post_ids_read") == 33410 and coverage.get("unique_post_ids_unread") == 0,
            "Некорректный общий счётчик охвата")
    require(coverage.get("all_selected_participants_covered") is True and coverage.get("all_less_active_covered") is True,
            "Не подтверждён полный охват")
    for directory, suffix in (("participants", ".md"), ("factchecks", ".jsonl")):
        present = {p.stem for p in (ROOT / directory).glob(f"*{suffix}")}
        require(present == {str(i) for i in author_ids}, f"{directory}: лишние или отсутствующие файлы")
if source is not None:
    require(source.get("ok") is True and source.get("sqlite_posts") == 33410,
            "Метаданные исходной проверки не совпадают со снимком")

# Проверяем относительные Markdown-ссылки на файлы. Внешние адреса и якоря не запрашиваем.
links = 0
for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).strip().strip("<>").split()[0]
        parts = urlsplit(target)
        if parts.scheme or target.startswith("#"):
            continue
        destination = (path.parent / unquote(parts.path)).resolve()
        links += 1
        require(destination.is_relative_to(ROOT) and destination.exists(),
                f"{path.relative_to(ROOT)}: отсутствует локальная ссылка {target}")

if errors:
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    print(f"Ошибок: {len(errors)}", file=sys.stderr)
    sys.exit(1)
print(f"OK: 25 авторов, {len(all_ids)} post_id, {records} записей проверок, {links} локальных ссылок.")
print("Проверена согласованность файлов; исходные сообщения и внешние источники не проверялись.")
