
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter


def setup():
    """Единый стиль для всех ноутбуков."""
    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.figsize"] = (12, 4)
    plt.rcParams["axes.titlesize"] = 12
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["figure.dpi"] = 110


def money_axis(ax=None, unit="M"):
    """Приводит ось Y к читаемому виду: 1500000 превращается в 1.5M."""
    div = {"K": 1e3, "M": 1e6, "B": 1e9}[unit]
    ax = ax or plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x / div:.1f}{unit}"))
    return ax


def pct_axis(ax=None):
    ax = ax or plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.0f}%"))
    return ax


def add_growth(df, cols, suffix):
    """Прирост период к периоду в процентах.

    Считается через pct_change, без обращения к номерам строк.
    Хардкод индексов ломается при любом обновлении данных.
    """
    out = df.copy()
    for c in cols:
        out[f"{c}_{suffix}"] = out[c].pct_change() * 100
    return out


def month_number(cohort_month, activity_month):
    """Номер месяца жизни когорты: 1 это месяц привлечения.

    Считается по календарю, а не через row_number в SQL.
    row_number даёт подряд идущие номера и при пропущенном месяце
    сдвигает всю когорту влево, из-за чего retention завышается.
    """
    cohort = pd.to_datetime(cohort_month)
    activity = pd.to_datetime(activity_month)
    return (activity.dt.year - cohort.dt.year) * 12 + (
        activity.dt.month - cohort.dt.month
    ) + 1


def add_time_parts(df, date_col):
    """Добавляет week и month к колонке с датой."""
    out = df.copy()
    out[date_col] = pd.to_datetime(out[date_col])
    out["week"] = out[date_col].dt.to_period("W").dt.start_time
    out["month"] = out[date_col].dt.to_period("M").dt.to_timestamp()
    return out
