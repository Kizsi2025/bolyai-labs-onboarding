"""Bolyai Labs – Feladatkártya #1: a fejlesztői környezet ellenőrzése."""
import sys

import numpy as np
import pandas as pd


def main():
    print(f"Python: {sys.version.split()[0]}")
    print(f"NumPy: {np.__version__}")
    print(f"Pandas: {pd.__version__}")

    df = pd.read_csv("data/bolyai_labs_minta.csv")
    print(f"Sorok száma: {len(df)}")
    print(f"Átlagos válaszidő: {df['valaszido_ms'].mean():.1f} ms")
    print(df.groupby("modell")["valaszido_ms"].mean())
    print("A környezet rendben van.")


if __name__ == "__main__":
    main()
