# Coffee Health Analysis Project

This project builds machine learning models to classify health conditions based on coffee consumption and lifestyle data. It compares various models, selects the best-performing one, and deploys it through a user-friendly Tkinter GUI application.

You can explore the full project and analysis on Kaggle:  
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

This project explores the relationship between coffee consumption, sleep patterns, stress levels, and health outcomes using a comprehensive dataset. It includes data preprocessing, visualization, and predictive modeling with multiple ML algorithms including Random Forest, Logistic Regression, SVM, KNN, and ANN. The model with the highest performance is saved and deployed with a Tkinter-based GUI for easy use.

## Project Structure

| File Name                          | Description                                    |
|-----------------------------------|------------------------------------------------|
| README.md                         | Project documentation                          |
| best_model.pkl                    | Saved best-performing model pipeline            |
| coffee (Notebook).ipynb           | Jupyter notebook with analysis, training, and evaluation |
| coffee4.png                      | Background image for the GUI                     |
| deployment.py                    | GUI application code using Tkinter               |
| synthetic_coffee_health_10000.csv | Dataset used for training models                |
| ydata_profile.html               | Detailed data profiling report generated via ydata-profiling |

## Requirements

- Python 3.9+  
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, ydata-profiling, joblib, Pillow  
- Tkinter (comes pre-installed with Python)  

To install dependencies, run:

```
pip install pandas numpy matplotlib seaborn scikit-learn ydata-profiling joblib pillow
```

## How to Run

1. Run `coffee (Notebook).ipynb` to preprocess data, visualize insights, train multiple models, and save the best model.  
2. Run the deployment GUI with the command:

```
python deployment.py
```

This will open an interactive window where you can input your health and lifestyle data to get predicted health issue classifications along with confidence scores.

## Deployment GUI

The GUI allows input for multiple features such as:

- Age, Gender, Country  
- Coffee Intake & Caffeine consumption  
- Sleep hours & Sleep quality  
- BMI, Heart rate, Stress level  
- Physical activity hours, Occupation  
- Smoking and Alcohol consumption

Upon clicking the "Predict" button, the app predicts health condition class and displays confidence probability.

## Files Description

| File                            | Description                        |
|--------------------------------|----------------------------------|
| coffee (Notebook).ipynb        | Data exploration, visualization, and model training |
| best_model.pkl                 | Trained and saved best model      |
| deployment.py                  | Tkinter GUI application           |
| synthetic_coffee_health_10000.csv | Dataset file                    |
| coffee4.png                   | Background image for UI            |
| ydata_profile.html            | Generated report for EDA           |
| README.md                     | This README documentation         |

## Usage Example

```
import joblib
import pandas as pd

model = joblib.load('best_model.pkl')

sample_data = pd.DataFrame({
    'Age': ,[7]
    'Gender': ['Male'],
    'Country': ['USA'],
    'Coffee_Intake': ,[8]
    'Caffeine_mg': ,
    'Sleep_Hours': ,[9]
    'Sleep_Quality': ['Good'],
    'BMI': [24.5],
    'Heart_Rate': ,
    'Stress_Level': ['Low'],
    'Physical_Activity_Hours': ,[10]
    'Occupation': ['Office'],
    'Smoking': ,
    'Alcohol_Consumption':[10]
})

prediction = model.predict(sample_data)
print("Predicted Health Issue:", prediction)
```

## License

This project is open-source and provided for educational and research purposes. Feel free to modify and expand it with appropriate attribution.

---
