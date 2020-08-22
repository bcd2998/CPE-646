import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

# Get Cleaned Data CSV
books = pd.read_csv("clean_data.csv", encoding='utf-8',delimiter=',')#, nrows=1000)
books.dataframeName = 'book_data.csv'
books.drop(columns=['Unnamed: 0'], inplace=True)
nRow, nCol = books.shape 
print(f'There are {nRow} rows and {nCol} columns')
# Debug print book info
print(books.info())

# Data Preprocessing with LabelEncoder
gle = LabelEncoder()

#   Genres
genre_labels = gle.fit_transform(books['genres'])
genre_mappings = {index: label for index, label in 
                  enumerate(gle.classes_)}
#   Ratings
ratings_labels = gle.fit_transform(books['book_rating'])
ratings_mappings = {index: label for index, label in enumerate(gle.classes_)}

# Title to fit model
title_labels = gle.fit_transform(books['book_title'])
title_mappings = {index: label for index, label in enumerate(gle.classes_)}

# Print Encodings
print(genre_labels)
print(ratings_labels)

# Build
fields = []
for x in range(len(genre_labels)):
    fields.append([genre_labels[x], ratings_labels[x]])

# Train Model - Gaussian Naive Bayes
model = GaussianNB()
model.fit(fields, title_labels)

# Predict this item/ Multiple Predictions
#### Intention for some UI to determine genre and 
##### code to predict at multiple rating values
input_genre = 212
runique = np.unique(ratings_labels)
predictions = {}
forprint = []

# Predict for each unique rating
for x in runique:
    if ratings_mappings[x] >= 4.6:
        print(f'encode{x} = {ratings_mappings[x]}')
        prediction = model.predict([[input_genre, x]])
        predictions[x] = prediction

#Print Predictions
for p in predictions.keys():
    # prints for debug
    #print(f'genre {genre_mappings[input_genre]}, rating{p}')
    #print(f'predicts: {predictions[p]}')
    #print(f'prediction:{title_mappings[int(predictions[p])]}')

    # Some code to get more data
    # Get book name from title mapping
    bookname = title_mappings[int(predictions[p])]

    # Get index in dataframe to find location of book
    title_index = books[books['book_title'] == bookname].index

    # Print location/ Entire entry in Dataframe
    print(f'location{books.loc[title_index.values]}')

    # Pull Author and rating data from location
    author = books.loc[title_index.values,'book_authors'].values[0]
    rating = books.loc[title_index.values,'book_rating'].values[0]
    
    # Create list of predictions
    printable = f'{bookname} by {author} (GR Rating {rating})'
    if not printable in forprint:
        forprint.append(printable)

#Print Predictions as a book list
print(f'For Genre {genre_mappings[input_genre]}')
for p in forprint:
    print(p)
    