🌼 Iris Flower Classification App

This project predicts the species of an Iris flower (Setosa, Versicolor, or Virginica) based on its sepal and petal measurements.
It uses a Decision Tree Classifier and is deployed as an interactive web app using Streamlit
.

🚀 Features

Predicts iris flower species using user-input measurements

Simple and interactive Streamlit UI

Quick model built on the classic Iris dataset

Easy to extend with new ML algorithms

🧠 Tech Stack

Python 3

Scikit-learn – for model training

Pandas – for data handling

Joblib – for saving/loading the model

Streamlit – for web app deployment

📁 Project Structure
irisflowerproject/
│
├── app.py               # Streamlit web app
├── iris_model.pkl       # Saved Decision Tree model
├── requirements.txt     # Python dependencies
├── iris.csv (optional)  # Dataset if included
└── README.md            # Project description

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/<your-username>/irisflowerproject.git
cd irisflowerproject


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py

🧩 How It Works

Load the Iris dataset

Train a Decision Tree Classifier

Save the model using joblib

Build a Streamlit interface for user input

Predict and display the flower species

🌸 Demo
Measurement Input	Predicted Species
Sepal: 5.1 x 3.5 cm	Iris-setosa
Sepal: 6.7 x 3.0 cm	Iris-versicolor
🏁 Future Enhancements

Add support for multiple ML algorithms

Include data visualization (heatmaps, charts)

Deploy online (Streamlit Cloud or HuggingFace Spaces)# Iris-Flower-Classification
