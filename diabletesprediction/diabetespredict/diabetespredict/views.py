
from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from xgboost import XGBClassifier




# Load the dataset
diabetes_dataset = pd.read_csv('C:\\Users\\HP\\OneDrive\\Documents\\ML\\dataset.csv') 

# Separate the data and labels
X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

# Standardize the data
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
X = standardized_data

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Initialize base classifiers
svm_classifier = SVC(kernel='linear')
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=2)
xgb_classifier = XGBClassifier()

# Create a voting classifier
voting_classifier = VotingClassifier(estimators=[
    ('svm', svm_classifier),
    ('rf', rf_classifier),
    ('xgb', xgb_classifier)
], voting='hard')

# Train the voting classifier
voting_classifier.fit(X_train, Y_train)

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    input_data = np.array([val1, val2, val3, val4, val5, val6, val7, val8])
    input_data_reshaped = input_data.reshape(1, -1)
    std_data = scaler.transform(input_data_reshaped)

    prediction = voting_classifier.predict(std_data)

    result1 = ""
    if prediction[0] == 1:
        result1 = "Positive "
    else:
        result1 = "Negative"

    return render(request, 'predict.html', {"result2": result1})
