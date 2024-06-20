# Machine Learning Trashcan
Machine learning model for waste images classification with multi-label class.

## Dataset
We import the dataset from Kaggle, Roboflow, and web scraping in Google Image.

Here is the link to our final dataset: [Trashcan Final Dataset](https://drive.google.com/drive/folders/1tF26rr-uxIigt92-l66nSy11igRYq2Cz?usp=drive_link)

## Library
Libraries that we used for preprocessing the images and training the model are:
```
os
shutil
numpy
sklearn
seaborn
matplotlib
tensorflow
keras
```

## Labels
Each images has 2 labels, category and sub-category. 

Here are the category labels:
- Organik
- Anorganik
- B3


And here are the sub-category labels:
- Daun
- Kardus
- Makanan Olahan
- Kaleng
- PET 
- Tas Plastik Belanja
- Aerosol
- Baterai
- Obat Kapsul

## Model
We used transfer learning to train the model with EfficientNetB3V2 as the base model and reached an overall accuracy of 95%.

Here is the link to our final model: [Trashcan Final Model](https://drive.google.com/file/d/1OdqTuvrEpcIc0KsFWTv0v5P-Yt3Y1_7m/view?usp=drive_link)

### Confusion Matrix
Confusion matrix for category

![Category](/images/conf-main.png)

Confusion matrix for sub-category

![Sub-category](/images/conf-sub.png)

## Deployment
The final model was saved in `.h5` and the API ran in Flask Python. The Flask app later deployed in cloud using Cloud Run.

### Requirements
```
Flask==3.0.3
numpy==1.26.4
tensorflow==2.16.1
Werkzeug==3.0.3
pillow==10.3.0
```

### API Endpoint `predict` testing
- Local
    - Clone this repository
    - Make sure to download the model that we provide in [here](https://drive.google.com/file/d/1OdqTuvrEpcIc0KsFWTv0v5P-Yt3Y1_7m/view?usp=drive_link).
    - Run `pip install -r requirements.txt` command on CMD to install the required libriaries.
    - Run `python app.py` command
    - Use the URL from the response, https://127.0.0.0:5000/predict to test it in Postman or anywhere else.
- Direct
    - Use the deployed URL, https://trashcan-qnitsxbfya-et.a.run.app/predict directly.