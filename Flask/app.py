import numpy as np
import pandas as pd
import pickle
import os
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open('C:/Users/suhni/traffic-intelligence-app/model.pkl', 'rb'))

model_columns = ['temp', 'rain', 'snow', 'day', 'month', 'year', 'hours', 'minutes', 'seconds',
    'holiday_Columbus Day', 'holiday_Independence Day', 'holiday_Labor Day',
    'holiday_Martin Luther King Jr Day', 'holiday_Memorial Day', 'holiday_New Years Day',
    'holiday_State Fair', 'holiday_Thanksgiving Day', 'holiday_Veterans Day',
    'holiday_Washingtons Birthday', 'weather_Clouds', 'weather_Drizzle', 'weather_Fog',
    'weather_Haze', 'weather_Mist', 'weather_Rain', 'weather_Smoke', 'weather_Snow',
    'weather_Squall', 'weather_Thunderstorm'
]

@app.route('/')
def home():
    return render_template('index.html', prediction_text=None)

@app.route('/predict', methods=["POST"])
def predict():
    try:
        form = request.form
        input_data = {
            'holiday': form['holiday'],
            'temp': float(form['temp']),
            'rain': float(form['rain']),
            'snow': float(form['snow']),
            'weather': form['weather'],
            'year': int(form['year']),
            'month': int(form['month']),
            'day': int(form['day']),
            'hours': int(form['hours']),
            'minutes': int(form['minutes']),
            'seconds': int(form['seconds']),
        }

        df = pd.DataFrame([input_data])
        df = pd.get_dummies(df)

        for col in model_columns:
            if col not in df.columns:
                df[col] = 0

        df = df[model_columns]

        prediction = model.predict(df)
        text = f"Estimated Traffic Volume is: {int(prediction[0])}"

        return render_template('index.html', prediction_text=text)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True, use_reloader=False)
