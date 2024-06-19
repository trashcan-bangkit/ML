import os
from werkzeug.utils import secure_filename
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Ukuran input gambar untuk model
IMAGE_SIZE = (128, 128)  # Sesuaikan dengan ukuran input model Anda

# Muat model dari file .h5
model = load_model('./effnetb3v2_waste_classification.h5')

# Label kategori utama dan subkategori
main_category_labels = ['Anorganik', 'B3', 'Organik']
sub_category_labels = {
    'Anorganik': ['Kaleng', 'PET', 'Tas Plastik Belanja'],
    'B3': ['Aerosol', 'Baterai', 'Obat Kapsul'],
    'Organik': ['Daun', 'Kardus', 'Makanan Olahan']
}

def predict_image(image_path):
    image = load_img(image_path, target_size=IMAGE_SIZE)
    image_array = img_to_array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)  # Expand dimensions to match the model input shape

    predictions = model.predict(image_array)
    main_category_pred = main_category_labels[np.argmax(predictions[0])]
    sub_category_pred = sub_category_labels[main_category_pred][np.argmax(predictions[1])]

    return main_category_pred, sub_category_pred

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        app.logger.error("No file part in the request")
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        app.logger.error("No selected file")
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        app.logger.info(f"File saved to {filepath}")
        main_category, sub_category = predict_image(filepath)
        return jsonify({"main_category": main_category, "sub_category": sub_category})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)