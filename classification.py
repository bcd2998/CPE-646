from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
#import skimage.color
#import skimage.io
#import skimage.viewer
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

books_fromcsv = pd.read_csv("new_data.csv", encoding='utf-8',delimiter=',')#, nrows=1000)
books = books_fromcsv.dropna()
books.dataframeName = 'book_data.csv'
nRow, nCol = books.shape 
print(f'There are {nRow} rows and {nCol} columns')


print(books.head(20))

#getting training set examples labels
y_train=books['genres'].values
x_train=books['book_rating'].values

print(y_train)

from sklearn.model_selection import train_test_split
#train_data,test_data,train_labels,test_labels=train_test_split(x_train,y_train,shuffle=True,test_size=0.25,random_state=42,stratify=y_train)
#classes=np.unique(train_labels)
genres = np.unique(books['genres'])
print(genres)

from sklearn.preprocessing import LabelEncoder
gle = LabelEncoder()
genre_labels = gle.fit_transform(books['genres'])
genre_mappings = {index: label for index, label in 
                  enumerate(gle.classes_)}
print(genre_mappings)

