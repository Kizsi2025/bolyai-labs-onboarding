# Bolyai Labs – Feladatkártya #1: Működő fejlesztői környezet

> Fejlesztőként szeretnék egy izolált Python-környezetet a szükséges könyvtárakkal, hogy a projekt függőségei ne ütközzenek más projektekkel, és a csapat bármelyik gépén ugyanígy fusson.

## Elfogadási feltételek

- [ ] a repó klónozva, a `.venv` létrehozva és aktiválva
- [ ] a `numpy` és a `pandas` telepítve, a `check_env.py` hiba nélkül lefut
- [ ] a `requirements.txt` feltöltve, és tartalmazza mindkét csomagot
- [ ] a CI-futás zöld (Actions fül)

**Határidő:** a 2. óra vége · **Érték:** 5 sprintpont (zöld build 2, határidő 1, commitüzenet 1, kilépőkérdések 1)

## Lépések (Windows, PowerShell)

```powershell
git clone <a saját repód címe>
cd <a repó mappája>
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install numpy pandas
python check_env.py
python -m pip freeze | Out-File -Encoding utf8 requirements.txt
git add requirements.txt
git commit -m "feat: fejlesztői környezet beállítása (feladatkártya #1)"
git push
```

VS Code-ban: `Ctrl+Shift+P` → **Python: Select Interpreter** → a `.venv`-beli Python.

Linuxon és macOS-en az aktiválás `source .venv/bin/activate`, a requirements.txt pedig `python -m pip freeze > requirements.txt`.

A `check_env.py` kimenetének végén ezt kell látnod: `Átlagos válaszidő: 663.3 ms` és `A környezet rendben van.`

## Ha elakadsz

| Tünet | Megoldás |
| --- | --- |
| Az `Activate.ps1` nem fut | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (vagy cmd-ben `.venv\Scripts\activate.bat`) |
| A `python` a Microsoft Store-t nyitja meg | Használd a `py -3` indítót |
| A pip nem éri el az internetet | `python -m pip install --no-index --find-links <wheels mappa> numpy pandas` |
| A VS Code nem találja a pandast | Rossz értelmező: válaszd a `.venv`-belit |
| Piros build: „Hiányzik a requirements.txt” | `git add requirements.txt`, commit, push |
| A `.venv` mappa felkerült a repóba | `git rm -r --cached .venv`, majd új commit |

## B-terv: Colab

Ha a 25. percre sem áll fel a helyi környezet: Colabban **File → Open notebook → GitHub** fül, jelöld be az **Include private repos** lehetőséget, nyisd meg az `onboarding_colab.ipynb`-t, futtasd, majd **File → Save a copy in GitHub**. A helyi környezetet a 2. blokk első 10 percében pótolod.

## Két szabály egész évre

1. API-kulcs és személyes adat soha nem kerül commitba vagy promptba.
2. Az MI által írt kódot is érteni kell. Amit nem tudsz elmagyarázni, azt nem adod be.
