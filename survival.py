#importing essential libraries
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox, ttk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("tested.csv")

# Handle missing values
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Fill missing Embarked values
df['Ticket'] = pd.to_numeric(df['Ticket'], errors='coerce').fillna(0)  # Convert Ticket to numeric

# Encode categorical variables
label_encoders = {}
categorical_cols = ['Embarked']
for col in categorical_cols:
    label_encoders[col] = LabelEncoder()
    df[col] = label_encoders[col].fit_transform(df[col])

# Define features and target
features = ['PassengerId', 'Ticket', 'Embarked']
X = df[features]
y = df['Survived']  # 0=Dead, 1=Alive

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train classification model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

def predict_survival():
    try:
        # Get user input
        user_input = [float(entry.get()) for entry in entries]
        user_input = np.array(user_input).reshape(1, -1)
        user_input = scaler.transform(user_input)

        # Predict survival
        prediction = model.predict(user_input)
        result = "\U0001F7E2 Alive" if prediction[0] == 1 else "\U0001F534 Dead"
        result_label.config(text=f"Prediction: {result}", fg='green' if prediction[0] == 1 else 'red')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for the features.")

def refresh():
    for entry in entries:
        entry.delete(0, tk.END)
    result_label.config(text="")

# Create GUI window
root = tk.Tk()
root.title("Titanic Survival Prediction")
root.geometry("400x300")
root.configure(bg='#1e1e2e')  # Dark theme background

# Title Label
title_label = tk.Label(root, text="Titanic Survival Prediction", font=("Arial", 14, "bold"), bg='#1e1e2e', fg='white')
title_label.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg='#1e1e2e')
frame.pack(pady=10)

labels = ['PassengerId', 'Ticket', 'Embarked (0=C, 1=Q, 2=S)']
entries = []
for i, label in enumerate(labels):
    tk.Label(frame, text=label, font=("Arial", 10), bg='#1e1e2e', fg='white').grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = ttk.Entry(frame)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Buttons
button_frame = tk.Frame(root, bg='#1e1e2e')
button_frame.pack(pady=10)

predict_btn = ttk.Button(button_frame, text="Predict", command=predict_survival)
predict_btn.grid(row=0, column=0, padx=5)

refresh_btn = ttk.Button(button_frame, text="Refresh", command=refresh)
refresh_btn.grid(row=0, column=1, padx=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg='#1e1e2e', fg='white')
result_label.pack(pady=10)

root.mainloop()