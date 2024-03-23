"""
Training module.
"""


import os
import pickle
from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# prepare data
input_dir = './images'
categories = ['Apple', 'Banana']

data = []
labels = []
for idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path) # JPEG ONLY
        img = resize(img, (15, 15))
        data.append(img.flatten())
        labels.append(idx)

#data = np.stack(np.asarray(data, dtype=object))
#labels = np.stack(np.asarray(labels, dtype=object))
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
