# coffee-health-analysis Project

This project builds machine learning models to classify health conditions based on coffee consumption and lifestyle data. It compares various models, selects the best-performing one, and deploys it through a user-friendly Tkinter GUI application.

You can also explore the full project and analysis on Kaggle:  
[https://www.kaggle.com/code/ahmedabdelsalam15/coffee](https://www.kaggle.com/code/ahmedabdelsalam15/coffee)

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Deployment GUI](#deployment-gui)
- [Files Description](#files-description)
- [Usage Example](#usage-example)
- [License](#license)

## Project Overview

The goal of this project is to predict the severity of health issues ("None", "Mild", "Moderate", "Severe") using features such as coffee intake, caffeine consumption, sleep patterns, BMI, heart rate, stress level, and more. The models include Random Forest, Logistic Regression, SVM, K-Nearest Neighbors, and an Artificial Neural Network (ANN). The best model is selected automatically and saved for deployment.

## Project Structure

| File Name                          | Description                                    |
|-----------------------------------|------------------------------------------------|
| README.md                         | This documentation file                        |
| best_model.pkl                    | Saved best-performing model pipeline            |
| coffee (Notebook).ipynb           | Jupyter notebook with data analysis and model training |
| coffee4.png                      | Background image for GUI                         |
| deployment.py                    | GUI code built with Tkinter for predictions     |
| synthetic_coffee_health_10000.csv | Dataset used for training models                |

## Requirements

- Python 3.9 or higher
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, ydata-profiling, joblib, Pillow
- Tkinter (comes pre-installed with Python)

To install the required Python packages, run:

pip install pandas numpy matplotlib seaborn scikit-learn ydata-profiling joblib pillow


## How to Run

1. Open and run `coffee (Notebook).ipynb` to perform exploratory data analysis, train machine learning models, and save the best model.
2. To launch the prediction GUI, run:

python deployment.py



This opens a window where you can input health and lifestyle data and receive a health issue prediction with confidence scores.

## Deployment GUI

The GUI allows input for features including age, gender, country, coffee intake, caffeine mg, sleep hours and quality, BMI, heart rate, stress level, physical activity, occupation, smoking, and alcohol consumption. The prediction and its confidence are displayed upon clicking the "Predict" button.

## Files Description

| File                            | Description                        |
|--------------------------------|----------------------------------|
| coffee (Notebook).ipynb        | Data exploration, model training  |
| best_model.pkl                 | Trained model ready for inference |
| deployment.py                  | Tkinter based GUI application      |
| synthetic_coffee_health_10000.csv | Dataset used for training       |
| coffee4.png                   | Background image for the GUI       |
| README.md                     | This project documentation         |

## Usage Example

import joblib
import pandas as pd

Load the saved model pipeline
model = joblib.load('best_model.pkl')

Create sample input data
sample_data = pd.DataFrame({
'Age': ,
'Gender': ['Male'],
'Country': ['USA'],
'Coffee_Intake': ,
'Caffeine_mg': ,
'Sleep_Hours': ,
'Sleep_Quality': ['Good'],
'BMI': [24.5],
'Heart_Rate': ,
'Stress_Level': ['Low'],
'Physical_Activity_Hours': ,
'Occupation': ['Office'],
'Smoking': ,
'Alcohol_Consumption':
})

Predict health issue class
prediction = model.predict(sample_data)
print("Predicted Health Issue:", prediction)



## License

This is an educational open-source project. You are free to use and modify it with attribution.

---
