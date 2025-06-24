# Traffic Volume Estimation Web App
This is a Flask-based machine learning web application that predicts traffic volume based on various inputs such as date, time, weather conditions, and holidays. The model was trained using historical traffic data (up to 2022) and supports an interactive UI for input and prediction display.

🔍 Features
🎯 Predicts traffic volume based on:

Weather (rain, snow, temperature, etc.)

Date and time (day, month, year, hour, minute, second)

Public holidays

🌐 User-friendly web interface with:

Background image and translucent form container

Responsive layout and styling

Dynamic result rendering after prediction

⚙️ Built using:

Flask (Python web framework)

HTML5 + CSS3

scikit-learn / XGBoost model for prediction

🧠 ML Model Details
Model trained on historical traffic dataset from [source, if applicable].

Inputs were preprocessed and one-hot encoded during training.

The model expects features such as:

Encoded holidays (holiday_Columbus Day, etc.)

Encoded weather conditions (weather_Rain, etc.)

Normal numeric features (temp, rain, snow, time fields)

📌 Note: The model is trained only on data from 2012 to 2022 and may not generalize well for future years.

🚀 How to Run the Project
Clone this repo:

bash
Copy
Edit
git clone https://github.com/yourusername/traffic-volume-estimation.git
cd traffic-volume-estimation
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Place your trained model file (model.pkl) in the project root.

Run the app:

bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser.

📁 File Structure
php
Copy
Edit
├── app.py                # Flask app
├── model.pkl             # Trained machine learning model
├── templates/
│   └── index.html        # Main HTML template with form and result
├── requirements.txt      # Python dependencies
└── README.md             # Project description
