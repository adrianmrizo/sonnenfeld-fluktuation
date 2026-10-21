# Datenmodell — analytische Tabelle

Eingang: bereinigte Tabelle aus der Bereinigungsphase. Hier werden Typen und neu konstruierte Features dokumentiert.

| Spalte | Typ | Herkunft | Beschreibung / Regel |
|---|---|---|---|
| mitarbeiter_id | string | Eingang | Kein Feature |
| alter | int | Eingang | |
| geschlecht | category | Eingang | Nur Fairness-Prüfung, kein Feature |
| abteilung | category | Eingang | |
| position | category (geordnet) | Eingang | Junior < Senior < Lead < Manager |
| eintrittsdatum | date | Eingang | |
| betriebszugehoerigkeit_jahre | int | Eingang | |
| gehalt_brutto | float | Eingang | EUR/Jahr |
| ueberstunden_monat | int | Eingang | |
| zufriedenheit | int | Eingang | Skala 1–5 |
| abwesenheitstage_jahr | int | Eingang | |
| gekuendigt | int (0/1) | Eingang | Zielvariable |
| *neue Features* | | konstruiert | z. B. gehaltsquartil, zugehoerigkeit_band |
