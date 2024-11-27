# 🎵 Musik-Vorschläge mit ML

Ein Programm, das dir Musik vorschlägt, die zu dir passt.

## 🤔 Was macht das Programm?

Das Programm lernt aus meinen Testdaten, welche Musik sie mögen. Dann kann es für neue Personen vorhersagen, welche Musik ihnen gefallen könnte.

## 📁 Dateien und ihre Funktionen

### `main.py`
- Lädt die Musikdaten aus `music.csv`
- Trainiert das ML-Modell
- Speichert das trainierte Modell als `music-recommender.joblib`
- Macht Vorhersagen für neue Benutzer (Beispiel: 22 Jahre, männlich)

### `music.csv`
- Enthält die Trainingsdaten
- Spalten:
  - `age`: Alter der Person
  - `gender`: Geschlecht (0 = weiblich, 1 = männlich)
  - `genre`: Musikgenre (HipHop, Jazz, Classical, Dance, Acoustic)

### `visualization.py`
- Erstellt eine visuelle Darstellung des Entscheidungsbaums
- Exportiert den Baum als `music-recommender.dot`
- Zeigt, wie das Modell Entscheidungen trifft

### `music-recommender.dot`
- Grafische Darstellung des Entscheidungsbaums
- Zeigt:
  - Entscheidungsregeln (z.B. "age <= 30.5")
  - Wahrscheinlichkeiten für jedes Genre
  - Verzweigungen basierend auf Alter und Geschlecht