# User Stories

Grundlage für Kapitel 3 (Projektplanung und SCRUM-Dokumentation).

**Format:** *Als* [Rolle] *möchte ich* [Ziel], *damit* [Nutzen].

## Stakeholder

| Person | Rolle | Erwartung an das Projekt |
|---|---|---|
| Dr. Petra Lindner | Personalleiterin (Sponsorin) | Klare Aussagen darüber, welche Faktoren die Fluktuation treiben |
| Markus Wagner | Leiter HR-Analytics | Sauber dokumentierte Lösung, die das HR-Team nach Projektende weiterführen kann |
| Stefanie Voss | Betriebsratsvorsitzende | Datenschutz und faire Modellbildung, keine diskriminierenden Merkmale, keine personenbezogenen Vorhersagen ohne Begründung |

## Leitfragen

| # | Leitfrage | Entscheidung |
|---|---|---|
| F1 | In welchen Abteilungen, Hierarchieebenen und Altersgruppen ist die Fluktuationsquote am höchsten? | Wo sollte die Personalabteilung ihre Maßnahmen zuerst ansetzen? |
| F2 | Welche Gruppe nach Betriebszugehörigkeit weist eine besonders hohe Fluktuationsquote auf? | In welche Art von Programm sollte die Personalabteilung investieren: Onboarding, Personalentwicklung oder Wissenssicherung? |
| F3 | Welcher Zusammenhang besteht zwischen Überstunden bzw. dem Gehalt im Vergleich zur eigenen Hierarchieebene und der Fluktuation? | Sind strukturelle Maßnahmen nötig, um die Arbeitsbelastung zu senken und/oder die Gehälter anzupassen? |
| F4 | Lässt sich anhand der Merkmale zum Stichtag vorhersagen, welche Mitarbeitergruppen in den nächsten 12 Monaten ein erhöhtes Kündigungsrisiko haben, und welche Merkmale tragen am stärksten zur Vorhersage bei? | Mit welchen Risikogruppen führt die Personalabteilung proaktiv Gruppengespräche, und welche Arbeitsbedingungen werden angepasst? |

## User Stories

### Dr. Petra Lindner — Personalleiterin

**US-01 (F1+F2)**
Als Personalleiterin möchte ich wissen, in welchen Abteilungen, Hierarchieebenen, Altersgruppen und Gruppen nach Betriebszugehörigkeit die Fluktuationsquote am höchsten ist, damit ich entscheiden kann, wo die Personalabteilung zuerst ansetzen sollte und welche Art von Programm (Onboarding, Personalentwicklung oder Wissenssicherung) Priorität hat.

*Akzeptanzkriterien:*
- Altersgruppen und Gruppen nach Betriebszugehörigkeit definiert und begründet
- Fluktuationsquote je Abteilung, Hierarchieebene, Altersgruppe und Betriebszugehörigkeitsgruppe berechnet (inkl. Anzahl Mitarbeitende) und mit der Gesamtquote verglichen
- Zusammensetzung der Betriebszugehörigkeitsgruppen nach Hierarchieebene dargestellt
- Ergebnisse visualisiert und sortiert
- Fazit: die drei auffälligsten Gruppen und Empfehlung, welche Art von Programm Priorität hat

**US-02 (F3)**
Als Geschäftsführer/in möchte ich wissen, welcher Zusammenhang zwischen Überstunden bzw. dem Gehalt im Vergleich zur eigenen Hierarchieebene und der Fluktuation besteht, damit ich entscheiden kann, ob sich Investitionen in strukturelle Maßnahmen (z. B. zusätzliches Personal oder Gehaltsanpassungen) im Vergleich zu den Kosten der Fluktuation lohnen.

*Akzeptanzkriterien:*

- Relatives Gehalt je Abteilung und Hierarchieebene berechnet (z. B. Gehaltsquartil innerhalb der Vergleichsgruppe)
- Überstundengruppen anhand der Verteilung definiert und begründet
- Fluktuationsquote je Überstundengruppe und je Gehaltsquartil berechnet (inkl. Anzahl Mitarbeitende) und mit der Gesamtquote verglichen
- Kombination auffälliger Gruppen geprüft (z. B. Hierarchieebene × Abteilung × Überstunden)
- Fluktuationskosten geschätzt, mit dokumentierten und begründeten Annahmen
- Fazit mit Empfehlung, wo strukturelle Maßnahmen geprüft werden sollten

**US-03 (F4)**
Als Personalleiterin möchte ich wissen, welche Mitarbeitergruppen im Unternehmen in den nächsten 12 Monaten ein erhöhtes Kündigungsrisiko haben und welche Faktoren am stärksten damit zusammenhängen, damit ich festlegen kann, mit welchen Gruppen die Abteilungsleitungen frühzeitig Gespräche führen sollten und welche Arbeitsbedingungen angepasst werden müssen.

*Akzeptanzkriterien:*

- Mindestens zwei Klassifikationsmodelle trainiert und mit einem Baseline-Modell verglichen
- Recall (Klasse „gekündigt”) als Hauptmetrik; Precision, F1-Score, ROC-AUC und Konfusionsmatrix ergänzend berichtet
- Liste der Modellmerkmale dokumentiert; geschlecht nachweislich nicht enthalten
- Ergebnisse als Risikosegmente mit mindestens 10 Personen pro Segment
- Feature Importance dargestellt und auf geschäftliche Plausibilität geprüft
- Fairness-Prüfung: Recall und Falsch-Positiv-Rate nach Geschlecht verglichen

### Markus Wagner — Leiter HR-Analytics

**US-04**
Als Leiter HR-Analytics möchte ich eine vollständig dokumentierte und reproduzierbare Analyse erhalten, damit mein Team sie nach Projektende mit neu erhobenen Daten selbstständig wiederholen kann.

*Akzeptanzkriterien:*
- Klare Ordnerstruktur mit README (Setup, Ablauf, Verantwortlichkeiten)
- Cleaning-Log mit allen Bereinigungsentscheidungen
- Wiederverwendbarer Python-Code, Notebooks mit Erläuterungen zu jedem Schritt
- Anleitung zum erneuten Trainieren des Modells
- Dashboard lässt sich durch Austausch der Datendatei (gleiches Schema) aktualisieren
- Test: Eine Person ohne Projektwissen kann die Analyse anhand des README wiederholen

### Stefanie Voss — Betriebsratsvorsitzende

**US-05**
Als Betriebsratsvorsitzende möchte ich nachvollziehen können, welche Merkmale und Aggregationsverfahren in Analyse und Modellbildung verwendet werden, damit ich prüfen kann, ob der Datenschutz eingehalten wird, keine diskriminierenden Merkmale verwendet und keine personenbezogenen Vorhersagen ohne Begründung erstellt werden.

*Akzeptanzkriterien:*
- Ergebnisse und Dashboard enthalten ausschließlich aggregierte Risikosegmente, keine individuellen Vorhersagen
- Jedes Segment umfasst mindestens 10 Personen
- Liste aller Modellmerkmale mit Begründung
- `geschlecht` ist kein Modellmerkmal; Entscheidung dokumentiert und begründet
- Fairness-Prüfung: Recall und Falsch-Positiv-Rate nach Geschlecht verglichen