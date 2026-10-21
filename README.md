# Mitarbeiterfluktuation bei Sonnenfeld Industries GmbH

**Explorative Analyse und Frühwarnmodell** · Teil des Abschlussprojekts IHK Datenanalyst (Masterschool)

> **Status:** in Arbeit

## Geschäftsproblem

Die jährliche Kündigungsquote bei Sonnenfeld Industries (Stuttgart, ca. 10.000 Mitarbeitende) ist
in zwei Jahren von unter 10 % auf rund 17 % gestiegen. Die Personalabteilung möchte verstehen,
welche Faktoren mit erhöhtem Kündigungsrisiko zusammenhängen, und ein einfaches Frühwarnsystem aufbauen.

## Leitfragen

<!-- TODO: finale Fragen eintragen -->
1. …
2. …
3. …

## Zentrale Ergebnisse

<!-- Am Projektende: 3–5 Kernaussagen, Modellleistung, Empfehlungen für die HR-Leitung -->

## Vorgehen

| Schritt | Notebook |
|---|---|
| Eingangsprüfung und vertiefte EDA | [`01_eda.ipynb`](notebooks/01_eda.ipynb) |
| Feature Engineering und Modellierung | [`02_modellierung.ipynb`](notebooks/02_modellierung.ipynb) |
| Evaluation, Feature Importance und Fairness | [`03_evaluation_fairness.ipynb`](notebooks/03_evaluation_fairness.ipynb) |

Die Datenbereinigung und das Tableau-Dashboard wurden von meinem Projektpartner Jakub umgesetzt
und sind nicht Teil dieses Repositorys.

## Projektstruktur

```
├── data/
│   ├── input/          Bereinigte Daten (nicht versioniert)
│   └── processed/      Features und Risikosegmente (nicht versioniert)
├── notebooks/          Analyse in drei Schritten
├── src/sonnenfeld/     Wiederverwendbarer Code (Konfiguration, Features, Modell, Grafikstil)
├── reports/figures/    Exportierte Grafiken
├── docs/               ML Canvas, Datenmodell, Ethik-Entscheidungen
└── CLAUDE.md           Projektkontext für Claude Code
```

## Daten und Datenschutz

- Synthetischer Datensatz, bereitgestellt von Masterschool; die Daten selbst werden nicht veröffentlicht.
- Das Merkmal `geschlecht` wird nicht als Modell-Feature verwendet, sondern nur für eine
  Fairness-Prüfung. Begründung: [`docs/ethik_entscheidungen.md`](docs/ethik_entscheidungen.md).
- Ergebnisse werden als aggregierte Risikosegmente weitergegeben, nicht als personenbezogene Vorhersagen.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

## Werkzeuge

Python (pandas, scikit-learn, matplotlib, seaborn) · Jupyter · Git/GitHub · Claude Code
