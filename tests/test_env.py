"""Automatikus tesztek a Feladatkártya #1-hez. Ezeket futtatja a CI minden push után."""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent


def read_requirements():
    # A régebbi PowerShell ">" átirányítása UTF-16-ot ír, ezért mindkét kódolást elfogadjuk.
    raw = (ROOT / "requirements.txt").read_bytes()
    for enc in ("utf-8-sig", "utf-16"):
        try:
            return raw.decode(enc).lower()
        except UnicodeDecodeError:
            continue
    return ""


def test_python_version():
    assert sys.version_info >= (3, 10), "Legalább Python 3.10 kell"


def test_requirements_exists():
    assert (ROOT / "requirements.txt").exists(), "Hiányzik a requirements.txt"


def test_requirements_content():
    text = read_requirements()
    assert "numpy" in text and "pandas" in text, "A requirements.txt-ben szerepelnie kell a numpy és a pandas csomagnak"


def test_sample_data():
    df = pd.read_csv(ROOT / "data" / "bolyai_labs_minta.csv")
    assert len(df) == 6
    assert round(df["valaszido_ms"].mean(), 1) == 663.3
