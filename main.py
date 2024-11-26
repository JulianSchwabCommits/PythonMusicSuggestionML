import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

#music_data = pd.read_csv('./music.csv')
#x = music_data.drop(columns=['genre'])
#y = music_data['genre']     

#model = DecisionTreeClassifier()
#model.fit(x,y)

model = joblib.load('music-recommender.joblib')

# Erstelle ein DataFrame mit den korrekten Spaltennamen
prediction_data = pd.DataFrame([[22, 0]], columns=['age', 'gender'])
predictions = model.predict(prediction_data)
print(predictions)
