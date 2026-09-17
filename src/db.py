
import os
from pathlib import Path
from urllib.parse import quote_plus

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

ROOT = Path(__file__).resolve().parents[1]
SQL_DIR = ROOT / "sql"
MARTS_DIR = ROOT / "data" / "marts"

load_dotenv(ROOT / ".env")

_REQUIRED = ["DB_USER", "DB_PASSWORD", "DB_HOST", "DB_NAME"]


def get_engine():
    missing = [k for k in _REQUIRED if not os.getenv(k)]
    if missing:
        raise RuntimeError(
            "Не заданы переменные окружения: "
            + ", ".join(missing)
            + ". Скопируй .env.example в .env и заполни."
        )

    user = os.environ["DB_USER"]
    password = quote_plus(os.environ["DB_PASSWORD"])
    host = os.environ["DB_HOST"]
    port = os.getenv("DB_PORT", "6432")
    name = os.environ["DB_NAME"]

    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"
    )


def read_sql_file(name, **params):
    """Читает sql из папки sql/. Плейсхолдеры вида {date_col} подставляются через params."""
    text = (SQL_DIR / name).read_text(encoding="utf-8")
    return text.format(**params) if params else text


def query(engine, name, **params):
    """Выполняет запрос из файла и возвращает DataFrame."""
    return pd.read_sql_query(read_sql_file(name, **params), engine)


def save_mart(df, name):
    """Сохраняет агрегат в data/marts. Эти файлы коммитятся и питают дашборд."""
    MARTS_DIR.mkdir(parents=True, exist_ok=True)
    path = MARTS_DIR / f"{name}.csv"
    df.to_csv(path, index=False)
    print(f"сохранено: {path.relative_to(ROOT)}, строк {len(df)}")
    return path
