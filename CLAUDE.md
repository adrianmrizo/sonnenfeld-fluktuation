# CLAUDE.md — Sonnenfeld Fluktuationsanalyse (EDA & ML)

Context and rules for Claude Code in this repository. Read this file fully before any task.

## 1. Project

Adrian's part of a two-person **IHK Datenanalyst** final project (Masterschool), published as a portfolio repo.
Fictional client: **Sonnenfeld Industries GmbH**, Stuttgart, ~10,000 employees.
Attrition rose from <10 % to ~17 % per year. Management wants to know which factors are
**associated** with resignation and wants a simple **early-warning classifier** (Frühwarnsystem).

Scope of this repo: **deep-dive EDA → feature engineering → classification model → evaluation & fairness.**
Data cleaning (before) and the Tableau dashboard (after) are done by teammate Jakub outside this repo.

Stakeholders: HR director (wants clear drivers), HR Analytics lead (wants a documented, maintainable solution),
works council (data protection, fairness, no unjustified individual predictions).

## 2. Inputs and outputs

- **Input:** cleaned table from Jakub in `data/input/` (path in `config.INPUT_FILE`). Read-only, never edit.
  The first notebook starts with an input check (row count, dtypes, missing values, duplicates, value ranges)
  because the data was cleaned by someone else.
- **Output for the dashboard:** `data/processed/dashboard_export.csv`. Format (aggregated segments vs.
  individual scores) is an **open decision** — see section 4.
- Data files are not committed (see `.gitignore`). Results are visible through notebook outputs and `reports/figures/`.

## 3. Data facts

- **Stichtag** = 31 Dec of the last fiscal year. All features describe the state on the Stichtag.
  Target `gekuendigt` (0/1) = resigned within the 12 months **after** the Stichtag.
  Never create a feature using information from after the Stichtag (leakage).
- Columns: `mitarbeiter_id, alter, geschlecht, abteilung, position, eintrittsdatum,
  betriebszugehoerigkeit_jahre, gehalt_brutto, ueberstunden_monat, zufriedenheit (1–5),
  abwesenheitstage_jahr, gekuendigt`.
- Keep original German column names. New columns: German snake_case (e.g. `gehaltsquartil`, `zugehoerigkeit_band`).

## 4. Hard rules

1. `data/input/` is read-only.
2. No leakage: split first, then fit all preprocessing inside an sklearn `Pipeline`.
   `mitarbeiter_id` and the target are never features. `modelling.split()` enforces this.
3. **Open decisions belong to Adrian.** Never decide them in code, docs or defaults; present
   the options with pros and cons and ask. Record his decision in `docs/ethik_entscheidungen.md`.
   Currently open:
   - whether `geschlecht` is used as a model feature (the brief requires a justified decision;
     works council rejects discriminatory models)
   - whether the dashboard receives individual risk scores or only aggregated segments
     (brief: no individual predictions *without justification*)
4. Imbalanced target: stratified split; report recall, precision, F1, ROC-AUC and confusion matrix.
   Never accuracy alone. Recall on class 1 is the primary metric.
5. Use `RANDOM_STATE` from `config.py` everywhere.
6. Wording: **association, not causation**.
7. Paths and constants only via `src/sonnenfeld/config.py`.
8. Charts use `src/sonnenfeld/plotting.py` and are saved to `reports/figures/` as `NN_short_name.png`.

## 5. Code conventions

- Python 3.11+, pandas, scikit-learn. **Code comments and docstrings in English.**
  Markdown cells, chart titles and docs in **German** (IHK jury).
- Reusable logic in `src/sonnenfeld/`; notebooks import it.
- Notebook structure:
  - First cell: markdown header (title, goal, input, output).
  - Markdown cell before each section explaining **why** the step is done.
  - One logical step per code cell; each section ends with an "Erkenntnis" markdown cell.
  - Must pass "Restart Kernel & Run All" before committing.
- **Keep notebook outputs** when committing — this is a portfolio repo and GitHub renders them.
  Avoid printing whole DataFrames; use `.head()`, summaries and charts.
- Prefer simple, explainable models (logistic regression, decision tree, random forest).

## 6. Git

- Solo repo, work on `main`; use a branch only for experiments.
- Small commits with conventional prefixes: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`.
- Never commit data, trained models or credentials.

## 7. Commands

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .                                     # makes `import sonnenfeld` work in notebooks
jupyter lab
```

## 8. How to work with Adrian

- Adrian is learning: explain the reasoning behind a technical choice briefly **before** writing code.
  He must defend every step in the Fachgespräch, so understanding matters more than speed.
- Ask what he thinks before giving the answer on analytical decisions (hypotheses, feature choice, threshold).
- Ask before large refactors and before any decision with ethical, legal or business impact.
- When a decision affects the report (feature choice, threshold, ethics), add it to the matching file in `docs/`.
- Flag anything that would not hold up in front of an IHK jury.
