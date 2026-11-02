# Titration Analyzer — Project Instructions

## About me
- I'm a senior chemistry major and a **beginner in Python**. I've written basic scripts but I'm still learning pandas, numpy, and plotting.
- This is a **portfolio project**. I need to understand and be able to explain every line, so teaching matters more than speed.
- I'm on Windows and work in VS Code.

## What this project is
A Python web app (Streamlit) that analyzes acid–base titration data from my own lab work:
- Load data from CSV/Excel, or let me type in handwritten readings
- Plot pH vs. titrant volume
- Find the equivalence point (1st/2nd derivative methods and a Gran plot)
- Calculate analyte concentration and pKa (from the half-equivalence point)
- Carry measurement uncertainty through to the results
- Export a results report

Target: working, deployed version 1 by mid-December 2026.

## How to work with me
- **Small steps.** Work on one function or feature at a time. Don't build several features in one go.
- **Explain as you go.** After writing code, briefly explain what each important part does and why. Point out any new Python concept (e.g. "this is a list comprehension").
- **Plan before big changes.** For anything touching more than one file, show me the plan first and wait for my OK.
- **Show the chemistry.** When implementing a calculation, write the equation in a comment and cite the method (e.g. Harris, *Quantitative Chemical Analysis*).
- **Leave some for me.** When a task is a good learning exercise, suggest I try writing it myself first and offer hints instead of the full answer.
- **Keep it simple.** Prefer readable code over clever code. No unnecessary abstractions or extra libraries.

## Tech stack
- Python 3.12+
- pandas, numpy, scipy (numerical work)
- matplotlib or plotly (plots)
- streamlit (web app)
- pytest (tests)
- Use a virtual environment (`.venv`) and keep `requirements.txt` up to date.

## Project layout
```
titration-analyzer/
├── CLAUDE.md
├── README.md
├── requirements.txt
├── app.py               # Streamlit interface
├── titration/
│   ├── __init__.py
│   ├── io.py            # loading and validating data
│   ├── analysis.py      # equivalence point, concentration, pKa
│   └── uncertainty.py   # error propagation
├── data/
│   └── sample/          # example datasets (no personal info)
└── tests/
    └── test_analysis.py
```

## Code standards
- Every function gets a short docstring with units (e.g. `volume_mL`, `conc_M`).
- Always include units in variable names.
- Every calculation function gets at least one test against a textbook problem with a known answer.
- Run `pytest` before saying a feature is done.
- Commit after each working step with a clear message.

## Data format
CSV with columns `volume_mL,pH`, one row per reading. Run metadata (analyte, titrant concentration ± uncertainty, aliquot volume, date) is entered in the app or a separate header block.
