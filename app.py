from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import json

with open('model/plant_disease_remedies.json', 'r', encoding='utf-8') as f:
    remedies = json.load(f)


app = Flask(__name__)
model = load_model('model/plant disease.h5')

# List of class labels — replace these with your actual model's classes
class_labels = ['Apple__black_rot', 'Apple__healthy', 'Apple__rust', 'Apple__scab',
                'Cassava__bacterial_blight', 'Cassava__brown_streak_disease',
                'Cassava__green_mottle', 'Cassava__healthy', 'Cassava__mosaic_disease',
                'Cherry__healthy', 'Cherry__powdery_mildew', 'Chili__healthy',
                'Chili__leaf curl', 'Chili__leaf spot', 'Chili__whitefly',
                'Chili__yellowish', 'Coffee__cercospora_leaf_spot', 'Coffee__healthy',
                'Coffee__red_spider_mite', 'Coffee__rust', 'Corn__common_rust',
                'Corn__gray_leaf_spot', 'Corn__healthy', 'Corn__northern_leaf_blight',
                'Cucumber__diseased', 'Cucumber__healthy', 'Gauva__diseased',
                'Gauva__healthy', 'Grape__black_measles', 'Grape__black_rot',
                'Grape__healthy', 'Grape__leaf_blight_(isariopsis_leaf_spot)',
                'Jamun__diseased', 'Jamun__healthy', 'Lemon__diseased', 'Lemon__healthy',
                'Mango__diseased', 'Mango__healthy', 'Peach__bacterial_spot',
                'Peach__healthy', 'Pepper_bell__bacterial_spot', 'Pepper_bell__healthy',
                'Pomegranate__diseased', 'Pomegranate__healthy', 'Potato__early_blight',
                'Potato__healthy', 'Potato__late_blight', 'Rice__brown_spot',
                'Rice__healthy', 'Rice__hispa', 'Rice__leaf_blast', 'Rice__neck_blast',
                'Soybean__bacterial_blight', 'Soybean__caterpillar',
                'Soybean__diabrotica_speciosa', 'Soybean__downy_mildew', 'Soybean__healthy',
                'Soybean__mosaic_virus', 'Soybean__powdery_mildew', 'Soybean__rust',
                'Soybean__southern_blight', 'Strawberry___leaf_scorch',
                'Strawberry__healthy', 'Sugarcane__bacterial_blight', 'Sugarcane__healthy',
                'Sugarcane__red_rot', 'Sugarcane__red_stripe', 'Sugarcane__rust',
                'Tea__algal_leaf', 'Tea__anthracnose', 'Tea__bird_eye_spot',
                'Tea__brown_blight', 'Tea__healthy', 'Tea__red_leaf_spot',
                'Tomato__bacterial_spot', 'Tomato__early_blight', 'Tomato__healthy',
                'Tomato__late_blight', 'Tomato__leaf_mold', 'Tomato__mosaic_virus',
                'Tomato__septoria_leaf_spot', 'Tomato__spider_mites_(two_spotted_spider_mite)',
                'Tomato__target_spot', 'Tomato__yellow_leaf_curl_virus', 'Wheat__brown_rust',
                'Wheat__healthy', 'Wheat__septoria', 'Wheat__yellow_rust']

remedies = {
    'Apple__black_rot': "Prune affected branches, remove infected fruit, and apply fungicide sprays during the growing season.",
    'Apple__healthy': "No issues detected. Maintain regular pruning and balanced fertilization.",
    'Apple__rust': "Remove nearby juniper hosts, apply fungicides, and improve air circulation around trees.",
    'Apple__scab': "Use resistant varieties, apply fungicide sprays, and remove fallen leaves.",
    'Cassava__bacterial_blight': "Remove infected plants, use disease-free cuttings, and apply copper-based bactericides.",
    'Cassava__brown_streak_disease': "Use resistant varieties, rogue infected plants, and control whiteflies.",
    'Cassava__green_mottle': "Destroy infected plants and practice crop rotation.",
    'Cassava__healthy': "Cassava is healthy. Continue regular monitoring.",
    'Cassava__mosaic_disease': "Use certified disease-free planting materials and control vector insects like whiteflies.",
    'Cherry__healthy': "No diseases detected. Maintain proper care practices.",
    'Cherry__powdery_mildew': "Prune infected shoots and apply sulfur-based or neem oil fungicides.",
    'Chili__healthy': "Plant is healthy. Regularly monitor for pests and diseases.",
    'Chili__leaf curl': "Control whiteflies, use insecticidal soaps, and remove infected plants.",
    'Chili__leaf spot': "Remove affected leaves and apply copper or neem oil sprays.",
    'Chili__whitefly': "Use sticky traps, neem oil sprays, or insecticidal soaps.",
    'Chili__yellowish': "Check for nutrient deficiencies and apply balanced fertilizers.",
    'Coffee__cercospora_leaf_spot': "Remove affected leaves and apply copper-based fungicides.",
    'Coffee__healthy': "No disease. Maintain shade, irrigation, and pruning routines.",
    'Coffee__red_spider_mite': "Spray miticides or neem oil and increase humidity.",
    'Coffee__rust': "Use resistant varieties and spray fungicides during rainy seasons.",
    'Corn__common_rust': "Apply fungicides and use resistant hybrids.",
    'Corn__gray_leaf_spot': "Rotate crops, use resistant varieties, and apply fungicides.",
    'Corn__healthy': "No disease. Keep monitoring for any symptoms.",
    'Corn__northern_leaf_blight': "Use resistant hybrids and apply fungicide sprays.",
    'Cucumber__diseased': "Remove affected plants and spray fungicides or insecticides based on symptoms.",
    'Cucumber__healthy': "Plant is healthy. Maintain regular checks.",
    'Gauva__diseased': "Prune infected twigs and apply fungicide sprays like Bordeaux mixture.",
    'Gauva__healthy': "No disease. Maintain regular pest control.",
    'Grape__black_measles': "Prune infected vines, improve drainage, and apply fungicides.",
    'Grape__black_rot': "Remove infected leaves and berries, and use preventive fungicides.",
    'Grape__healthy': "Vines are healthy. Regular care is advised.",
    'Grape__leaf_blight_(isariopsis_leaf_spot)': "Spray fungicides like mancozeb and remove infected leaves.",
    'Jamun__diseased': "Prune infected parts and spray copper-based fungicides.",
    'Jamun__healthy': "No disease. Regularly monitor for pest or fungal attacks.",
    'Lemon__diseased': "Use copper fungicides and remove affected branches.",
    'Lemon__healthy': "Maintain balanced nutrition and pest control.",
    'Mango__diseased': "Spray systemic fungicides and prune infected parts.",
    'Mango__healthy': "Good health. Maintain preventive fungicide sprays.",
    'Peach__bacterial_spot': "Apply copper-based bactericides and remove infected fruits.",
    'Peach__healthy': "Peach tree is healthy. Keep up regular pruning and sprays.",
    'Pepper_bell__bacterial_spot': "Remove affected leaves and apply copper-based sprays.",
    'Pepper_bell__healthy': "Healthy. Ensure good air circulation and balanced fertilization.",
    'Pomegranate__diseased': "Apply fungicides and avoid overhead irrigation.",
    'Pomegranate__healthy': "Maintain proper irrigation and pest control routines.",
    'Potato__early_blight': "Use fungicides like mancozeb and practice crop rotation.",
    'Potato__healthy': "Potato plants are healthy. Monitor for any signs of blight.",
    'Potato__late_blight': "Use protective fungicides and avoid overhead watering.",
    'Rice__brown_spot': "Apply balanced fertilizers and use seed treatments.",
    'Rice__healthy': "Healthy. Maintain proper field hygiene and pest control.",
    'Rice__hispa': "Spray insecticides like chlorpyrifos and remove damaged leaves.",
    'Rice__leaf_blast': "Use resistant varieties and apply fungicides.",
    'Rice__neck_blast': "Maintain proper spacing and apply fungicides at booting stage.",
    'Soybean__bacterial_blight': "Use certified seeds and apply bactericides.",
    'Soybean__caterpillar': "Use biopesticides like Bacillus thuringiensis or neem extracts.",
    'Soybean__diabrotica_speciosa': "Apply soil insecticides or crop rotation.",
    'Soybean__downy_mildew': "Spray systemic fungicides like metalaxyl.",
    'Soybean__healthy': "Healthy. Continue good agricultural practices.",
    'Soybean__mosaic_virus': "Use virus-free seeds and control aphid vectors.",
    'Soybean__powdery_mildew': "Use sulfur-based fungicides or neem oil sprays.",
    'Soybean__rust': "Apply preventive fungicides like tebuconazole.",
    'Soybean__southern_blight': "Remove infected debris and use soil fungicides.",
    'Strawberry___leaf_scorch': "Remove infected leaves and spray fungicides.",
    'Strawberry__healthy': "Healthy. Maintain good spacing and irrigation.",
    'Sugarcane__bacterial_blight': "Use disease-free setts and apply copper bactericides.",
    'Sugarcane__healthy': "Healthy. Continue regular irrigation and fertilization.",
    'Sugarcane__red_rot': "Destroy affected canes and apply hot water treatment to setts.",
    'Sugarcane__red_stripe': "Use resistant varieties and copper sprays.",
    'Sugarcane__rust': "Spray systemic fungicides like propiconazole.",
    'Tea__algal_leaf': "Remove infected leaves and apply copper oxychloride sprays.",
    'Tea__anthracnose': "Prune infected shoots and use mancozeb sprays.",
    'Tea__bird_eye_spot': "Use copper-based fungicides and remove infected leaves.",
    'Tea__brown_blight': "Apply captan or mancozeb sprays.",
    'Tea__healthy': "Healthy. Maintain regular pruning and pest control.",
    'Tea__red_leaf_spot': "Remove infected leaves and spray copper fungicides.",
    'Tomato__bacterial_spot': "Apply copper sprays and remove infected leaves.",
    'Tomato__early_blight': "Use fungicides like mancozeb and rotate crops.",
    'Tomato__healthy': "Healthy. Ensure good air circulation and balanced nutrients.",
    'Tomato__late_blight': "Apply protective fungicides and avoid overhead irrigation.",
    'Tomato__leaf_mold': "Use copper-based sprays and maintain good ventilation.",
    'Tomato__mosaic_virus': "Remove infected plants and control aphid vectors.",
    'Tomato__septoria_leaf_spot': "Use fungicides like chlorothalonil and remove infected leaves.",
    'Tomato__spider_mites_(two_spotted_spider_mite)': "Use miticides or insecticidal soap.",
    'Tomato__target_spot': "Apply fungicides like mancozeb and practice crop rotation.",
    'Tomato__yellow_leaf_curl_virus': "Remove infected plants and control whiteflies.",
    'Wheat__brown_rust': "Spray fungicides like propiconazole at flag leaf stage.",
    'Wheat__healthy': "Healthy. Maintain good fertilization and weed control.",
    'Wheat__septoria': "Use protective fungicides and remove crop debris.",
    'Wheat__yellow_rust': "Spray systemic fungicides early in the infection stage."
}

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detect')
def detect():
    return render_template('detect.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No file selected for uploading'

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        img = image.load_img(filepath, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        prediction = model.predict(img_array)
        predicted_class = class_labels[np.argmax(prediction)]

        # Fetch remedy from dictionary
        remedy = remedies.get(predicted_class, "No specific remedy available. Please consult a local expert.")

        return render_template('result.html', image_path=filepath, prediction=predicted_class, remedy=remedy)


if __name__ == '__main__':
    app.run(debug=True)


