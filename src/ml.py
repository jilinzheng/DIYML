"""
Image classification script to be modularized.
"""


import datetime
import os
import pickle
from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from flask_restful import Resource, reqparse
from .utils.database import models
from .utils.json_encode import json_encode


class TrainingAPI(Resource):
    """ Preprocess data for training. """
    def __init__(self):
        self.categories = []
        self.data = []
        self.labels = []

    def post(self):
        """
        Produces an image classification model trained on requested categories.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('user_name',
                            type=str,
                            location='args',
                            required=True,
                            help='You must specify an user.')
        parser.add_argument('model_name',
                            type=str,
                            location='args',
                            required=True,
                            help='You must provide a model name.')
        parser.add_argument('categories',
                            type=str,
                            required=True,
                            location='args',
                            help='You must specify categories to train on.',
                            action='append')
        args = parser.parse_args()

        user_name = args['user_name']
        model_name = args['model_name']
        categories = args['categories']
        IMAGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                         'images')
        
        # PREPROCESSING
        data = []
        labels = []
        for ii, category in enumerate(categories):
            for file in os.listdir(os.path.join(IMAGE_DIR, category)):
                img_path = os.path.join(IMAGE_DIR, category, file)
                img = imread(img_path) # JPEG ONLY
                img = resize(img, (15, 15))
                data.append(img.flatten())
                labels.append(ii)
        data = np.stack(data)
        labels = np.stack(labels)

        # TRAINING
        x_train, x_test, y_train, y_test = train_test_split(data,
                                                    labels,
                                                    test_size=0.2,
                                                    shuffle=True,
                                                    stratify=labels)
        
        classifier = SVC()
        parameters = [{'gamma': [0.01, 0.001, 0.0001],
                    'C': [1, 10, 100, 1000]}] # training 12 image classifiers
        grid_search = GridSearchCV(classifier, parameters)
        grid_search.fit(x_train, y_train)

        # EXPORT BEST MODEL
        best_estimator = grid_search.best_estimator_
        save_location = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                               'models',
                               f'{user_name}',
                               f'{model_name}')
        if not os.path.exists(save_location):
             os.makedirs(save_location)

        pickle.dump(best_estimator,
                    open(os.path.join(save_location,
                                      f'{model_name}.p'), 'wb'))
        
        # SAVE MODEL TO MODELS COLLECTION
        y_prediction = best_estimator.predict(x_test)
        model_stats = {'accuracy':accuracy_score(y_true=y_test, y_pred=y_prediction),
                       'precision':precision_score(y_true=y_test, y_pred=y_prediction),
                       'recall':recall_score(y_true=y_test, y_pred=y_prediction),
                       'f1':f1_score(y_true=y_test, y_pred=y_prediction)}

        models.insert_one({'model_name':model_name,
                           'user_name':user_name,
                           'model_path':save_location,
                           'categories_trained':categories,
                           'model_stats': model_stats,
                           'date_uploaded':datetime.datetime.now().strftime('%Y/%m/%d, %H:%M:%S EST')})
        
        return json_encode(models.find_one({'$and': [{'user_name':user_name},
                                                     {'model_name':model_name}]})), 201



"""
IMAGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                         'images') # need to import in the diyml(main) file

# preprocess data
categories = ['Apple', 'Banana']

data = []
labels = []
for ii, category in enumerate(categories):
    for file in os.listdir(os.path.join(IMAGE_DIR, category)):
        img_path = os.path.join(IMAGE_DIR, category, file)
        img = imread(img_path) # JPEG ONLY
        img = resize(img, (15, 15))
        data.append(img.flatten())
        labels.append(ii)
data = np.stack(data)
labels = np.stack(labels)


# train/test split
x_train, x_test, y_train, y_test = train_test_split(data,
                                                    labels,
                                                    test_size=0.2,
                                                    shuffle=True,
                                                    stratify=labels)


# train classifier
classifier = SVC()
parameters = [{'gamma': [0.01, 0.001, 0.0001],
               'C': [1, 10, 100, 1000]}] # training 12 image classifiers
grid_search = GridSearchCV(classifier, parameters)
grid_search.fit(x_train, y_train)


# test performance
best_estimator = grid_search.best_estimator_
y_prediction = best_estimator.predict(x_test)
score = accuracy_score(y_test, y_prediction)
print(f'{str(score*100)}% of samples were correctly classified')


# save model
pickle.dump(best_estimator, open('./models/first_model.p', 'wb'))
 """