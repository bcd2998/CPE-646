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
#print(f'There are {nRow} rows and {nCol} columns')con
# Debug print book info
#print(books.info())

# Data Preprocessing with LabelEncoder
gle_genre = LabelEncoder()
gle_rating = LabelEncoder()
gle_title = LabelEncoder()

#   Genres
genre_labels = gle_genre.fit_transform(books['genres'])
genre_mappings = {index: label for index, label in 
                  enumerate(gle_genre.classes_)}

#   Ratings
ratings_labels = gle_rating.fit_transform(books['book_rating'])
ratings_mappings = {index: label for index, label in enumerate(gle_rating.classes_)}

# Title to fit model
title_labels = gle_title.fit_transform(books['book_title'])
title_mappings = {index: label for index, label in enumerate(gle_title.classes_)}

# Print Encodings
# print(genre_labels)
# print(ratings_labels)

# Build
fields = []
for x in range(len(genre_labels)):
    fields.append([genre_labels[x], ratings_labels[x]])

# Train Model - Gaussian Naive Bayes
model = GaussianNB()
model.fit(fields, title_labels)

#Getting user input for the genre that they are looking for
# print("Welcome to the Book Recommender System!")
# fictionOrNon = input("Please enter Fiction if you are looking for Fiction genres or Nonfiction if you are looking for Nonfiction genres: ")
# fictionOrNon.lower()
# if fictionOrNon == 'fiction':
#     fictionType = input("Pleae enter which of the following fiction genres you are looking for: Animal, Biblical, Bizarro, Christian, Fan, Fiction, Flash, Gay, Historical, Lds, Lesbian, Literary, Military, Realistic, Science, Speculative, Weird, Womens: ")
#     fictionType.lower()
#     if fictionType == 'animal':
        
#         user_genre = 'Animal Fiction|' + ''
#     elif fictionType == 'biblical':
        
#         user_genre = 'Biblical Fiction|' + ''
#     elif fictionType == 'bizarro':
        
#         user_genre = 'Bizaro Fiction|'
#     elif fictionType == 'christian':
        
#         user_genre = 'Christian Fiction|' + ''
#     elif fictionType == 'fan':
        
#         user_genre = 'Fan Fiction|' + ''
#     elif fictionType == 'fiction':
        
#         user_genre = 'Fiction|' + ''
#     elif fictionType == 'gay':
        
#         user_genre = 'Gay Fiction|' + ''
#     elif fictionType == 'historical':
        
#         user_genre = 'Historical Fiction|' + ''
#     elif fictionType == 'lds':
        
#         user_genre = 'Lds Fiction|' + ''
#     elif fictionType == 'lesbian':
        
#         user_genre = 'Lesbian Fiction|' + ''
#     elif fictionType == 'literary':

#         user_genre = 'Literary Fiction|' + ''
#     elif fictionType == 'military':
        
#         user_genre = 'Military Fiction|' + ''
#     elif fictionType == 'realistic':
        
#         user_genre = 'Realistic Fiction|' +''
#     elif fictionType == 'science':
        
#         user_genre = 'Science Fiction|' + ''
#     elif fictionType == 'speculative':
        
#         user_genre = 'Speculative Fiction|' + ''
#     elif fictionType == 'weird':
        
#         user_genre = 'Weird Fiction|' + ''
#     elif fictionType == 'womens':
        
#         user_genre = 'Womens Fiction' + ''
#     else:
#         print("You did not enter a valid Fiction Type")
# elif fictionOrNon == 'nonfiction':
#     nonType = input("Please enter Christian if you are looking for Christian Nonfiction and Nonfiction if you are looking for another kind of Nonfiction: ")
#     nonType.lower()
#     if nonType == 'christian':
        
#         user_genre = 'Christian Nonfiction|' + ''
#     elif nonType == 'nonfiction':
        
#         user_genre = 'Nonfiction|' + ''
#     else:
#         print("You did not enter a valid NonFiction Type")
# else:
#     print("You did not enter a valid input!")
#For loop getting numeric value

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
        # print(f'encode{x} = {ratings_mappings[x]}')
        f'encode{x} = {ratings_mappings[x]}'
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
    