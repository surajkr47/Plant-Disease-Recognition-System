🌿 Plant Disease Recognition System

An intelligent Machine Learning-based system designed to detect and classify plant diseases from leaf images. The project helps farmers and agriculturists identify plant health conditions quickly and accurately using image processing and deep learning techniques.

📋 Table of Contents

About the Project

Features

Dataset

Tech Stack

Model Architecture

Project Structure

Installation

Usage

Results

Future Improvements

Contributors

License

🌱 About the Project

Agriculture is one of the most vital sectors of the economy, and plant diseases can lead to massive crop losses. This project aims to develop a Plant Disease Recognition System that uses machine learning / deep learning techniques to automatically identify diseases from images of plant leaves.

By leveraging Convolutional Neural Networks (CNNs), the model can learn to detect patterns and visual cues associated with different plant diseases and healthy leaves.

✨ Features

Detects diseases from plant leaf images

Supports multiple plant species (e.g., Tomato, Potato, Corn, etc.)

Easy-to-use web or command-line interface

Provides prediction with confidence percentage

Trained using deep learning (CNN / Transfer Learning)

🌾 Dataset

You can use the PlantVillage Dataset
 or any other dataset containing labeled plant leaf images.

Dataset structure example:

dataset/
│
├── train/
│   ├── Tomato___Bacterial_spot/
│   ├── Tomato___Healthy/
│   └── Potato___Early_blight/
│
└── test/
    ├── Tomato___Bacterial_spot/
    ├── Tomato___Healthy/
    └── Potato___Early_blight/

🧠 Tech Stack

Language: Python 🐍

Libraries: TensorFlow / Keras, OpenCV, NumPy, Matplotlib, Scikit-learn

Frameworks: Flask / Streamlit (for deployment)

Tools: Jupyter Notebook, Git, Kaggle

🏗️ Model Architecture

You can describe your approach here. Example:

Preprocessing: Image resizing, normalization, and data augmentation

Model: Custom CNN or Transfer Learning (e.g., MobileNet, VGG16, ResNet50)

Loss Function: Categorical Cross-Entropy

Optimizer: Adam

Metrics: Accuracy

📁 Project Structure

Example structure:

Plant-Disease-Recognition-System/
│
├── data/
│   └── dataset/                   # Training and testing images
│
├── models/
│   └── plant_disease_model.h5     # Saved model
│
├── notebooks/
│   └── training_notebook.ipynb    # Jupyter notebook for model training
│
├── app/
│   ├── app.py                     # Flask/Streamlit app for deployment
│   ├── static/                    # CSS/JS files
│   └── templates/                 # HTML files
│
├── requirements.txt
└── README.md

⚙️ Installation

Create a virtual environment

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run the application

python app/app.py


OR (if using Streamlit)

streamlit run app/app.py

🧩 Usage

Upload an image of a leaf through the web interface.

The model will predict the disease name and confidence score.

Results will be displayed on the screen.

📊 Results
Model	Accuracy	Loss
Custom CNN	94.5%	0.23
MobileNetV2	97.8%	0.12



🚀 Future Improvements

Add more plant species

Improve dataset diversity

Implement real-time detection using camera input

Deploy using cloud platforms (AWS / Heroku)

👨‍💻 Contributors

Suraj Kumar 
24MCA20013
UIC,Chandigarh University 

Teammate Name
Suraj Kumar (24MCA20013)
Deependra Verma (24MCA20007)

📝 License

This project is licensed under the MIT License – see the LICENSE
 file for details.
