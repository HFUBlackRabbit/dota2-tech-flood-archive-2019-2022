# Архив «Технической флудильни» Dota2.ru: 2019–2022

История участников и событий **архивного треда** [«Техническая флудильня» № 1300377](https://dota2.ru/forum/threads/texnicheskaja-fludilnja.1300377/) с 11 августа 2019 по 19 февраля 2022 года. Это завершённый исторический снимок, а не действующая тема форума.

**[История треда и хайлайты →](thread.md)** · [Все участники](#участники) · [Методология](docs/methodology.md) · [Условия использования](RIGHTS.md)

Продолжение после переезда в новую тему рассмотрено в отдельном репозитории: [dota2-tech-flood-study](https://github.com/HFUBlackRabbit/dota2-tech-flood-study). Этот архив и исследование продолжения — разные репозитории и разные снимки.

| Охват | Значение |
|---|---:|
| Сообщения в снимке | 33 410 |
| Уникальные author_id | 294 |
| Авторы с не менее чем 100 постами | 25 |
| Сообщения авторов ниже порога | 2 890 |
| Записи технических проверок | 215 |
| Последний post_id снимка | 26619911 |

Каждому из 25 авторов посвящены глава, хронология и реестр отдельных технических проверок. Исследование подготовлено AI-агентами; прочитанные посты и результаты отбора сохранены в [coverage.json](coverage.json). Это реконструкция по сообщениям: личные мотивы, диагнозы и исходы за пределами снимка не устанавливались. Техническая проверка выборочная и не означает, что подтверждён каждый совет.

## Участники

Подсчёт выполнен по уникальным `post_id` с группировкой по `author_id`; имена взяты из снимка. Даты и периоды в главах — UTC.

| Участник | author_id | Постов | Глава | Проверки |
|---|---:|---:|---|---|
| Sweet Sinner | 589886 | 3998 | [читать](participants/589886.md) | [JSONL](factchecks/589886.jsonl) |
| Denvys5 | 766227 | 3928 | [читать](participants/766227.md) | [JSONL](factchecks/766227.jsonl) |
| Sindar1n | 719362 | 3391 | [читать](participants/719362.md) | [JSONL](factchecks/719362.jsonl) |
| KellGrin | 705860 | 3304 | [читать](participants/705860.md) | [JSONL](factchecks/705860.jsonl) |
| Rick Dalton | 677194 | 3031 | [читать](participants/677194.md) | [JSONL](factchecks/677194.jsonl) |
| Leeds | 750175 | 2161 | [читать](participants/750175.md) | [JSONL](factchecks/750175.jsonl) |
| B_Rabbit | 732995 | 2116 | [читать](participants/732995.md) | [JSONL](factchecks/732995.jsonl) |
| Gachi boSS | 635955 | 1635 | [читать](participants/635955.md) | [JSONL](factchecks/635955.jsonl) |
| DWS | 691848 | 1298 | [читать](participants/691848.md) | [JSONL](factchecks/691848.jsonl) |
| Yurnelo | 456727 | 1141 | [читать](participants/456727.md) | [JSONL](factchecks/456727.jsonl) |
| Nikoliasik_Zeus | 416902 | 772 | [читать](participants/416902.md) | [JSONL](factchecks/416902.jsonl) |
| Gura | 62501 | 617 | [читать](participants/62501.md) | [JSONL](factchecks/62501.jsonl) |
| MTL | 355453 | 568 | [читать](participants/355453.md) | [JSONL](factchecks/355453.jsonl) |
| Ronan | 31059 | 504 | [читать](participants/31059.md) | [JSONL](factchecks/31059.jsonl) |
| 0xA50C1A1 | 560410 | 440 | [читать](participants/560410.md) | [JSONL](factchecks/560410.jsonl) |
| Старбой | 723713 | 280 | [читать](participants/723713.md) | [JSONL](factchecks/723713.jsonl) |
| Свиномансер | 469645 | 231 | [читать](participants/469645.md) | [JSONL](factchecks/469645.jsonl) |
| Constance | 426733 | 184 | [читать](participants/426733.md) | [JSONL](factchecks/426733.jsonl) |
| Newreg2019 | 788769 | 172 | [читать](participants/788769.md) | [JSONL](factchecks/788769.jsonl) |
| elda88 | 132173 | 152 | [читать](participants/132173.md) | [JSONL](factchecks/132173.jsonl) |
| Rezortius | 798987 | 132 | [читать](participants/798987.md) | [JSONL](factchecks/798987.jsonl) |
| KOHb2h | 127330 | 130 | [читать](participants/127330.md) | [JSONL](factchecks/127330.jsonl) |
| Bl00dWolf | 711873 | 123 | [читать](participants/711873.md) | [JSONL](factchecks/711873.jsonl) |
| Chloe Price | 102698 | 111 | [читать](participants/102698.md) | [JSONL](factchecks/102698.jsonl) |
| Кружечка Кофе | 616980 | 101 | [читать](participants/616980.md) | [JSONL](factchecks/616980.jsonl) |

## Проверить комплект

Нужен Python 3.9 или новее, дополнительные пакеты не нужны:

```bash
python3 scripts/validate.py
```

Проверка сверяет внутреннюю согласованность отбора и журналов ID, состав глав и реестров, JSON/JSONL и локальные Markdown-ссылки. Она не обращается к форуму и внешним источникам и не воспроизводит аналитическое чтение или фактчекинг. Исходная SQLite, JSONL сообщений, HTML и рабочие журналы вне `coverage.json` в комплект **не включены**. [Результаты исходной проверки снимка](source-verification.json) приведены для справки и не являются текущей проверкой этих отсутствующих файлов.

## Ограничения

Снимок не атомарен; удалённые и недоступные сообщения не восстановлены, изображения и видео не скачаны. Исходные тексты форума принадлежат их авторам, внешние статьи — правообладателям; [подробнее](RIGHTS.md).
