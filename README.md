# 🌿 AI-Powered Plant Disease Detection Web App

An AI-powered web application designed to help farmers and agricultural consultants easily detect plant diseases from leaf images. Simply upload an image of a plant leaf, and the app identifies the disease and suggests useful remedies in both English and Hindi.

---

## 📸 Demo

![App Screenshot](static/demo/demo_screenshot.png) <!-- Replace with your actual demo image path -->

---

## 📌 Features

- 🌱 Upload plant leaf images for disease detection.
- 🩺 Instant prediction of plant diseases using a pre-trained DenseNet121 deep learning model.
- 💡 Remedies and recommendations in **both English and Hindi**.
- 📊 Clean, responsive, and user-friendly interface built with **Bootstrap 5**.
- 🔐 Secure image upload handling.
- 🌐 Cross-browser and device compatibility.

---

## 🖥️ Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Python 3.12.2, Flask
- **AI Model**: DenseNet121 (Keras/TensorFlow)
- **Deployment**: Localhost (can be extended to Heroku, PythonAnywhere, AWS)

---
## 🗂️ Project Structure

├── app.py # Flask application routes and logic
├── model/
│ └── plant_disease_model.h5 # Pre-trained DenseNet121 model
├── static/
│ ├── uploads/ # Uploaded image files
│ └── demo/ # Demo images/screenshots
├── templates/
│ ├── index.html # Home page
│ ├── detect.html # Detection form
│ ├── predict.html # Prediction results
│ └── contact.html # Contact page
├── requirements.txt # Required Python packages
└── README.md # Project description file



---

## 📦 Installation & Setup

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/plant-disease-detection-app.git
cd plant-disease-detection-app
2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
4️⃣ Run the app

```bash

python app.py
5️⃣ Open in browser
Visit http://127.0.0.1:5000/ to access the app.

🧠 AI Model Details
Model Architecture: DenseNet121

Framework: TensorFlow / Keras

Input Shape: (224, 224, 3)

Classes Covered: 38 plant diseases from the PlantVillage dataset

Accuracy: ~96% on validation data

Remedy Recommendations: Based on expert agricultural guidelines, provided in both English and Hindi

📑 Key Routes in app.py
/ → Home Page

/detect → Upload and Detection Page

/predict → Prediction and Remedy Display

/contact → Contact Information

📬 Contact
Anushka Gupta
📧 anushka@example.com
📱 +91-XXXXXXXXXX
🌐 Portfolio Website

📜 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute for educational and personal projects.

🌟 Acknowledgements
PlantVillage Dataset by Penn State University

TensorFlow & Keras Team

Bootstrap 5 Framework

🚀 Future Improvements
Deploy on Heroku or AWS EC2

Add severity estimation for detected diseases

Include multilingual chatbot for agricultural guidance

Integrate IoT sensor data for precision agriculture

yaml
Copy
Edit

---

## ✅ Notes:
- Replace placeholder URLs, email, phone, and demo image paths as needed.
- If your model class count or dataset details differ, tweak the model section.
- You can optionally add a `.gitignore`, `requirements.txt`, and `LICENSE` for completeness.

---

Would you like me to generate those too? I can prep a complete project boilerplate if you’d like 📦✨
