import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# Kommentierung entfernen für Modellerstellung
print("Aktuelles Arbeitsverzeichnis:", os.getcwd())
music_data = pd.read_csv('C:/Users/TAASCJUN/OneDrive - Swisscom/Relevant/Coding/PythonMusicSuggestionML/music.csv')
x = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(x,y)

# Modell speichern
joblib.dump(model, 'music-recommender.joblib')

# Dann erst laden und vorhersagen
model = joblib.load('music-recommender.joblib')

# Erstelle ein DataFrame mit den korrekten Spaltennamen
prediction_data = pd.DataFrame([[22, 0]], columns=['age', 'gender'])
predictions = model.predict(prediction_data)
print(predictions)
