import os
import redis
from rq import Worker, Queue, Connection

import datetime
import pickle
from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from database import mongo_connect

listen = ['default']
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)

def train(user_name, model_name, categories):#, IMAGE_DIR):
    IMAGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                             'images')
    # PREPROCESSING
    data = []
    labels = []
    for ii, category in enumerate(categories):
        for jj, file in enumerate(os.listdir(os.path.join(IMAGE_DIR, category))):
            img_path = os.path.join(IMAGE_DIR, category, file)
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

    [users, images, models] = mongo_connect()

    models.insert_one({'model_name':model_name,
                    'user_name':user_name,
                    'model_path':save_location,
                    'categories_trained':categories,
                    'model_stats': model_stats,
                    'date_uploaded':datetime.datetime.now().strftime('%Y/%m/%d, %H:%M:%S EST')})

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
