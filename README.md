<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="style.css" />
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
    <h2>Installation</h2>
    <p>To install the required dependencies, run the following command:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
  </div>

  <div class="section">
    <h2>Cloning the Repository</h2>
    <p>You can clone the repository using the following command:</p>
    <pre><code>git clone &lt;repository_url&gt;</code></pre>
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
</body>
</html>
