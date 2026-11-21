# Boston House Prices - Data Analysis & Machine Learning

## 📌 Project Overview
This project is an end-to-end data analysis and machine learning pipeline. It uses Python to clean, analyze, and visualize a real estate dataset (Boston Housing), and builds a Linear Regression model to predict house prices based on the average number of rooms.

## 🛠️ Tech Stack
*   **Python** (Pandas, NumPy)
*   **Data Visualization** (Matplotlib, Seaborn)
*   **Machine Learning** (Scikit-Learn)

## 📊 Key Steps Performed
1.  **Data Loading & Cleaning**: Loaded the dataset using Pandas, handled whitespace separators, and assigned proper column names to make the data readable.
2.  **Exploratory Data Analysis (EDA)**: Used `df.describe()` to understand statistical distributions and identify outliers.
3.  **Visualization**: Created a scatter plot with a regression line (Trend Line) to prove the positive correlation between the number of rooms (`RM`) and the house price (`MEDV`).
4.  **Machine Learning**: Trained a `LinearRegression` model on the `RM` feature to predict `MEDV`.
5.  **Prediction**: Tested the model on a new house with 6 rooms, and it successfully predicted a price of approximately **$19,940**.

## 📈 Results & Insights
*   **Positive Correlation**: The analysis clearly shows that as the number of rooms increases, the median house value increases.
*   **Price Cap**: The dataset has a cap at $50,000 for the highest house prices.
*   **Model Accuracy**: The Linear Regression model successfully learned the trend and provided a realistic prediction for a 6-room house based on historical data.

## 🚀 How to Run
1. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn