# Ethik- und Fairness-Entscheidungen

## 1. Merkmal `geschlecht`

- **Entscheidung:** `geschlecht` wird in der deskriptiven Analyse verwendet, aber nicht als Merkmal im Modell.
- **Begründung:**
  - Ziel des Modells ist die Früherkennung von Kündigungsrisiken, nicht die Einordnung von Personen nach Geschlecht.
  - Ein Modell, das nach Geschlecht klassifiziert, wäre rechtlich (AGG) und ethisch problematisch und würde vom Betriebsrat abgelehnt.
- **Verwendung in der Analyse:** Geschlechterverteilung nach Hierarchieebene und Abteilung als Nebenbefund.
  Mögliche Unterschiede (z. B. beim Gehalt) werden als Hinweise für weiterführende Analysen benannt,
  aber nicht im Rahmen dieses Projekts untersucht.

## 2. Personenbezogene Vorhersagen

- **Entscheidung:** Ergebnisse werden ausschließlich als aggregierte Risikosegmente weitergegeben, nicht als individuelle Vorhersagen.
- **Mindestgröße:** Jedes Segment umfasst mindestens 10 Personen.
- **Begründung:**
  1. Eine Wahrscheinlichkeit ist keine Gewissheit: Ein Risiko von 78 % bedeutet auch, dass die Person mit 22 % Wahrscheinlichkeit bleibt.
  2. Prävention: Gruppenmaßnahmen erreichen auch Personen mit mittlerem Risiko, die noch gehalten werden können.
  3. Strukturelle Ursachen (z. B. Überstunden in einer Abteilung) lassen sich besser mit Gruppenmaßnahmen lösen.
  4. Stigmatisierung vermeiden: Eine individuelle Risikoeinstufung kann das Verhalten von Führungskräften beeinflussen
     und so eine selbsterfüllende Prophezeiung auslösen.
  5. Datenschutz und Mitbestimmung: Individuelle Bewertungen berühren die DSGVO und erfordern die Beteiligung des Betriebsrats.
  6. Die Mindestgröße verhindert Rückschlüsse auf Einzelpersonen. Zudem sind Quoten in sehr kleinen Gruppen statistisch instabil.
- **Mögliche Gegenfrage:** „Verlieren Sie mit Segmenten nicht an Präzision?"
  **Antwort:** Das Modell wird auf Personenebene trainiert, die Ergebnisse werden aggregiert weitergegeben.
  Individuelle Vorhersagen wären nur mit Betriebsvereinbarung, Transparenz gegenüber den Mitarbeitenden und klarer Begründung denkbar.

## 3. Fairness-Prüfung

- **Entscheidung:** Nach dem Training wird geprüft, ob das Modell für alle Geschlechtergruppen gleich gut funktioniert.
- **Vorgehen:** Konfusionsmatrix je Gruppe auf dem Testdatensatz; Vergleich von Recall und Falsch-Positiv-Rate.
- **Begründung:** Auch ohne `geschlecht` als Merkmal kann das Modell über Proxy-Variablen (z. B. Abteilung, Gehalt)
  Gruppen unterschiedlich behandeln.
- **Interpretation:** Unterschiedliche Fehlerraten zeigen zunächst ein Problem des Modells, nicht automatisch der Arbeitsbedingungen.
  Sie sind Hinweise für weiterführende Analysen und werden mit der deskriptiven Analyse nach Geschlecht abgeglichen.
- **Einschränkung:** Die Gruppe „divers" ist voraussichtlich klein; Ergebnisse für diese Gruppe sind statistisch wenig belastbar.

## 4. Metrik

- **Recall als Hauptmetrik:** Eine übersehene Kündigung (False Negative) ist teurer als ein Fehlalarm (False Positive),
  da das Projektziel die Vermeidung von Kündigungen ist.
- **Zusammenhang mit Entscheidung 2:** Da mit Gruppengesprächen gearbeitet wird und keine Einzelperson markiert wird,
  sind Fehlalarme kostengünstig. Ein empfindlicheres Modell mit höherem Recall ist daher vertretbar.

## 5. Merkmal `abwesenheitstage_jahr`

- **Entscheidung:** `abwesenheitstage_jahr` wird als Modellmerkmal verwendet.
- **Hintergrund:** Die Spalte umfasst Krankheits- und Sonderurlaubstage. Krankheitsbezogene Angaben
  können als Gesundheitsdaten gelten und sind nach DSGVO besonders schutzwürdig.
- **Begründung:**
  - Hohe Abwesenheit kann ein frühes Signal für Überlastung oder Unzufriedenheit sein und ist daher
    für ein Frühwarnsystem relevant.
  - Es wird nur die Gesamtzahl der Tage verwendet, keine Diagnosen oder Abwesenheitsgründe.
  - Ergebnisse werden ausschließlich als Risikosegmente mit mindestens 10 Personen weitergegeben;
    Rückschlüsse auf Einzelpersonen sind nicht möglich.
- **Risiken:**
  - Mögliche Benachteiligung von Personen mit chronischer Erkrankung oder Behinderung (AGG).
  - Fehlinterpretation, da Sonderurlaub (z. B. Pflege von Angehörigen) in derselben Zahl enthalten ist.
- **Maßnahmen:**
  - Vergleich des Modells mit und ohne dieses Merkmal: Ist der Leistungsgewinn gering,
    wird das Merkmal entfernt.
  - Einsatz in der Praxis nur mit Zustimmung des Betriebsrats.