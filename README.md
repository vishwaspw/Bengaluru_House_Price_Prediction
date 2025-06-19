# Bengaluru House Price Prediction

Get instant price estimates for properties in Bengaluru.

## 🚀 Live Demo
[Click here to use the deployed app!](https://bengaluru-house-price-prediction-acly.onrender.com)

---

## Project Overview

This project builds a machine learning model to predict house prices in Bangalore based on factors like location, square footage, and the number of rooms. The model is deployed as a web app using Flask, HTML, and CSS, and is accessible online.

## Dataset
- **Dataset used:** `Bengaluru_House_Data.xls`
- **Location:** Bangalore
- **Features:** 
  - Total square footage
  - BHK (bedrooms, hall, kitchen)
  - Bathrooms
  - Location
- **Target:** House price (in Lakhs)

## Requirements

Install the necessary packages with the following command:

```
pip install -r requirements.txt
```

## Usage

### Local Usage
1. **Open the Notebook:** Launch the Jupyter Notebook and open `Bengaluru house price.ipynb`.
2. **Run the Cells:** Execute each cell step-by-step to load data, preprocess it, train the model, and evaluate performance.
3. **Predict Prices:** Use the trained model to predict prices by running the final cell.
4. **Run the Web App Locally:**
   - Make sure you have `model.pkl` and `columns.pkl` generated from the notebook.
   - Run:
     ```
     python app.py
     ```
   - Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

### Online Usage
- Use the live app here: [https://bengaluru-house-price-prediction-acly.onrender.com](https://bengaluru-house-price-prediction-acly.onrender.com)

## Deployment

This app is deployed for free on [Render](https://render.com/):
- All code and assets are in this repository.
- The `Procfile` and `requirements.txt` are set up for easy deployment.
- Static files (including background image) are in the `static/` folder.

## Technologies Used
- **Python**
- **Flask** for the web app
- **Pandas** and **NumPy** for data manipulation
- **Scikit-Learn** for model building and evaluation
- **Bootstrap** and custom CSS for UI

---

© 2025 Bengaluru House Price Predictor
