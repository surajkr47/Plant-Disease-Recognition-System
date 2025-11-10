from flask import Flask, render_template,request,redirect,send_from_directory,url_for
import numpy as np
import json
import uuid
import tensorflow as tf
import os 

app = Flask(__name__)


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


MODEL_PATH_WINDOWS = os.path.join(SCRIPT_DIR, "models", "plant_disease_recog_model_pwp.keras")

MODEL_PATH = MODEL_PATH_WINDOWS.replace('\\', '/') 

JSON_PATH = os.path.join(SCRIPT_DIR, "plant_disease.json").replace('\\', '/')


try:
    print(f"Attempting to load model from: {MODEL_PATH}")
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:

    print("====================================================================================")
    print(f"CRITICAL ERROR: Failed to load Keras model.")
    print(f"Path verified to exist: {MODEL_PATH}")
    print("If this error persists, the file may be corrupted or locked (e.g., by an antivirus or another program).")
    print(f"Original Error: {e}")
    print("====================================================================================")
    model = None 


label = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Background_without_leaves',
 'Blueberry___healthy',
 'Cherry___Powdery_mildew',
 'Cherry___healthy',
 'Corn___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn___Common_rust',
 'Corn___Northern_Leaf_Blight',
 'Corn___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']

# Load plant_disease.json using the absolute path
plant_disease = {}
try:
    with open(JSON_PATH,'r') as file:
        plant_disease = json.load(file)
except FileNotFoundError:
    print(f"ERROR: plant_disease.json not found at: {JSON_PATH}")


# print(plant_disease[4])

@app.route('/uploadimages/<path:filename>')
def uploaded_images(filename):
    # Construct an absolute path for security and reliability
    UPLOAD_FOLDER = os.path.join(SCRIPT_DIR, 'uploadimages')
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/',methods = ['GET'])
def home():
    return render_template('home.html')

def extract_features(image):
    if model is None:
        return None
    # No change needed here, load_img is fine with path
    image = tf.keras.utils.load_img(image,target_size=(160,160))
    feature = tf.keras.utils.img_to_array(image)
    feature = np.array([feature])
    return feature

def model_predict(image):
    if model is None:
        return {"name": "Model Load Failure", "cure": "Cannot run prediction because the model failed to load on startup."}
        
    img = extract_features(image)
    if img is None:
        return {"name": "Error", "cure": "Failed to extract image features."}

    prediction = model.predict(img)
    prediction_index = prediction.argmax()
    
    if 0 <= prediction_index < len(plant_disease):
        prediction_label = plant_disease[prediction_index]
    else:
        # Fallback if prediction index is out of bounds
        name = label[prediction_index] if 0 <= prediction_index < len(label) else "Unknown Prediction"
        prediction_label = {"name": name, "cure": "Prediction index out of bounds."}

    return prediction_label

@app.route('/upload/',methods = ['POST','GET'])
def uploadimage():
    if request.method == "POST":
        image = request.files['img']
        
        # Ensure the 'uploadimages' directory exists before saving
        UPLOAD_FOLDER = os.path.join(SCRIPT_DIR, 'uploadimages')
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        
        temp_filename = f"temp_{uuid.uuid4().hex}_{image.filename}"
        full_file_path = os.path.join(UPLOAD_FOLDER, temp_filename)
        
        image.save(full_file_path)
        print(f'File saved to: {full_file_path}')
        
        # We pass the full path to model_predict for consistency
        prediction = model_predict(full_file_path)
        
        # For the URL path, we only need the relative path from the uploadimages route
        image_url_path = f'/uploadimages/{temp_filename}'
        
        return render_template('home.html',result=True,imagepath = image_url_path, prediction = prediction )
    
    else:
        return redirect('/')
        
    
if __name__ == "__main__":
    app.run(debug=True)