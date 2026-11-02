# Titration Analyzer

A Streamlit web app for analyzing acid–base titration data: plot pH vs. titrant
volume, find the equivalence point (1st/2nd derivative and Gran plot), and
calculate analyte concentration and pKa with propagated uncertainty.

## Setup (Windows, PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
streamlit run app.py   # start the app
pytest                 # run the tests
```
