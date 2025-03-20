<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Titanic Survival Prediction Project</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 40px;
      color: #333;
      background-color: #f9f9f9;
    }
    h1, h2, h3 {
      color: #0056b3;
    }
    p {
      margin-bottom: 10px;
    }
    ul {
      margin-bottom: 20px;
    }
    .section {
      margin-bottom: 40px;
    }
  </style>
</head>
<body>
  <h1>Titanic Survival Prediction Project</h1>

  <div class="section">
    <h2>Importing Libraries</h2>
    <p>In this project, I use essential libraries to enhance data manipulation and visualization:</p>
    <ul>
      <li><b>pandas:</b> For data manipulation and analysis.</li>
      <li><b>numpy:</b> For efficient numerical operations.</li>
      <li><b>seaborn:</b> For creating informative statistical visualizations.</li>
      <li><b>matplotlib.pyplot:</b> For plotting and visualizing analysis results.</li>
    </ul>
  </div>

  <div class="section">
    <h2>Loading Data</h2>
    <p>I load data from CSV files using pandas, splitting it into train and test datasets. These datasets contain valuable information about Titanic passengers, forming the basis of the analysis.</p>
  </div>

  <div class="section">
    <h2>Exploratory Data Analysis (EDA)</h2>
    <p>During EDA, I explore the dataset using various visualizations to uncover insights, including:</p>
    <ul>
      <li>Visualizing distributions of key features such as <b>age</b>, <b>SibSp</b>, <b>Parch</b>, and <b>fare</b>.</li>
      <li>Analyzing relationships between variables to identify patterns and correlations.</li>
    </ul>
  </div>

  <div class="section">
    <h2>Data Cleaning</h2>
    <p>Data cleaning is an essential phase where I:</p>
    <ul>
      <li>Handle missing values using appropriate imputation techniques.</li>
      <li>Drop unnecessary columns like <b>PassengerId</b>, <b>Cabin</b>, <b>Name</b>, and <b>Ticket</b>.</li>
      <li>Perform feature engineering to create or transform features, improving predictive performance.</li>
    </ul>
  </div>

  <div class="section">
    <h2>Model Testing</h2>
    <p>I evaluate different machine learning models to predict passenger survival, including:</p>
    <ul>
      <li>Decision Tree</li>
      <li>LGBM</li>
      <li>XGBoost</li>
      <li>RandomForest</li>
      <li>ExtraTrees</li>
      <li>Logistic Regression</li>
    </ul>
    <p>My best model achieved an accuracy of <b>73.8%</b>, effectively predicting survival outcomes.</p>
  </div>

  <div class="section">
    <h2>Test Submission</h2>
    <p>After training my model, I use it to predict the survival outcomes for the test dataset. I generate a submission file for evaluation, ensuring accurate model performance on unseen data.</p>
  </div>

  <div class="section">
    <h2>Conclusion</h2>
    <p>With a predictive accuracy of <b>73.8%</b>, the model successfully forecasts Titanic passenger survival. This project demonstrates practical applications of machine learning and provides insights into the factors influencing survival during the Titanic disaster.</p>
  </div>
</body>
</html>
