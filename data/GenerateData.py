from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = ['Lumpy', 'Giggles', 'Cuddles']
num_classes = len(classes)
img_size = 224

X = []
Y = []

for index, classlabel in enumerate(classes):
    img_dir = classlabel
    files = glob.glob(img_dir + '/*')
    for i, file in enumerate(files):
        image = Image.open(file)
        image = image.convert('RGB')
        image = image.resize((img_size, img_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save('./DataSet/htf_data.npy', xy)
