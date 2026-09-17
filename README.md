# MARKETPLACE ANALYTICS

Анализ маркетплейса: метрики продаж, юнит-экономика, когорты селлеров и продуктовая воронка.
PostgreSQL, Python, DataLens.

## О чём проект

Данные описывают маркетплейс: заказы, товарные позиции, категории, селлеры, комиссия площадки,
плюс отдельная таблица пользовательских событий. Задача была разобраться,
за счёт чего растёт оборот, где площадка зарабатывает и как устроен путь пользователя до покупки.

## Структура

```
notebooks/
  00_data_quality.ipynb      проверка данных, ограничения для остальных ноутбуков
  01_sales_and_margin.ipynb  GMV, AOV, маржа, take rate, категории, декомпозиция прироста
  02_cohorts_ltv.ipynb       retention селлеров, ARPPS, LTV по когортам
  03_events_funnel.ipynb     DAU, sticky factor, воронка view -> cart -> purchase
sql/                         запросы вынесены из ноутбуков в отдельные файлы
src/                         подключение к базе и общие хелперы
data/marts/                  агрегаты в csv, из них строится дашборд
```

## Стек

Python, pandas, numpy, SQLAlchemy, psycopg2, matplotlib, seaborn, PostgreSQL, Yandex DataLens.
