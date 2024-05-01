"""
Redis worker.
"""


import os
import sys
import datetime
import pickle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import redis
from rq import Worker, Queue, Connection
from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import src.database as database


listen = ['default']
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
IMAGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

def train(user_name, model_name, categories):
    """ Train models with given categories """
    # PREPROCESSING
    data = []
    labels = []
    for ii, category in enumerate(categories):
        for jj, file in enumerate(os.listdir(os.path.join(IMAGE_DIR, user_name, category))):
            img_path = os.path.join(IMAGE_DIR, user_name, category, file)
            img = imread(img_path) # JPEG ONLY
            img = resize(img, (15, 15))
            data.append(img.flatten())
            labels.append(ii)
            #if jj == 100: # to shorten runtime during debug
            #    break
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
                        f'{user_name}')
    if not os.path.exists(save_location):
        os.makedirs(save_location)

    pickle.dump(best_estimator,
                open(os.path.join(save_location,
                                f'{model_name}.p'), 'wb'))

    # SAVE MODEL TO MODELS COLLECTION
    y_prediction = best_estimator.predict(x_test)
    accuracy = accuracy_score(y_true=y_test,
                              y_pred=y_prediction)
    precision = precision_score(y_true=y_test,
                                y_pred=y_prediction,
                                labels=labels,
                                average='weighted')
    recall = recall_score(y_true=y_test,
                          y_pred=y_prediction,
                          labels=labels,
                          average='weighted')
    f1 = f1_score(y_true=y_test,
                  y_pred=y_prediction,
                  labels=labels,
                  average='weighted')
    model_stats = {'accuracy':accuracy,
                   'precision':precision if type(precision) is float else precision.tolist(),
                   'recall':recall if type(recall) is float else recall.tolist(),
                   'f1':f1 if type(f1) is float else f1.tolist()}

    models = database.mongo_connect()[2]

    models.insert_one({'model_name':model_name,
                       'user_name':user_name,
                        'categories_trained':categories,
                        'model_stats': model_stats,
                        'date_uploaded':datetime.datetime.now().strftime('%Y/%m/%d, %H:%M:%S EST')})


def save_inference(user_name, prediction, inference_id):
    """ Save inference to database """
    inferences = database.mongo_connect()[3]

    inferences.insert_one({'inference_id':inference_id,
                           'user_name':user_name,
                           'prediction':prediction,
                           'date_created':datetime.datetime.now().
                           strftime('%Y/%m/%d, %H:%M:%S EST')})


def inference(user_name, model_name, filename, inference_id):
    """ Infer on user-uploaded image with selected model """
    model_location = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                  'models',
                                  f'{user_name}')

    with open(os.path.join(model_location,
                           f'{model_name}.p'),
                           'rb') as f:
        model = pickle.load(f)

    upload_location = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                  'uploads')
    with open(os.path.join(upload_location,
                           filename),
                           'rb') as file:
        file = imread(file)
        file = resize(file, (15, 15))
        file = file.flatten()

        prediction = model.predict([file])
        if prediction[0] == 0:
            save_inference(user_name, 'apple', inference_id)
        elif prediction[0] == 1:
            save_inference(user_name, 'banana', inference_id)
        elif prediction[0] == 2:
            save_inference(user_name, 'mango', inference_id)

    os.remove(os.path.join(upload_location, filename))


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
