# 🚦 Traffic Volume Estimation Web App

This is a **Flask-based machine learning web application** that predicts traffic volume based on various inputs such as date, time, weather conditions, and holidays. The model was trained using historical traffic data (up to 2022) and supports an interactive UI for input and prediction display.

---

## 🔍 Features

- 🎯 Predicts **traffic volume** based on:
  - Weather (rain, snow, temperature, etc.)
  - Date and time (day, month, year, hour, minute, second)
  - Public holidays
- 🌐 User-friendly **web interface** with:
  - Background image and translucent form container
  - Responsive layout and styling
  - Dynamic result rendering after prediction
- ⚙️ Built using:
  - **Flask** (Python web framework)
  - **HTML5 + CSS3**
  - **scikit-learn / XGBoost** model for prediction

---

## 🧠 ML Model Details

- The model was trained on a historical traffic dataset (2012–2022).
- Input data was **preprocessed** and **one-hot encoded** for categorical features like holidays and weather.
- Model expects the following features:
  - Encoded holidays (e.g., `holiday_Columbus Day`)
  - Encoded weather types (e.g., `weather_Rain`)
  - Numeric values like temperature, rain, snow, date and time components

> ⚠️ **Note**: The model is trained only on data from **2012 to 2022** and may not generalize well for future years.

---

## 🚀 How to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Suhnitha/Traffic-Intelligence-App.git
    cd Traffic-Intelligence-App
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Place the trained model file** (`model.pkl`) in the project root directory.

4. **Run the Flask app**:
    ```bash
    python app.py
    ```

5. **Open in browser**:
    ```
    http://localhost:5000
    ```

---

