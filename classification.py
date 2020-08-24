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

# Functions for prediction program
## Predict Books
def predict_books(input_genre,rating_start,rating_end):
    """
        Predicts books based on input genre and rating
        Outputs - Dictionary of lists which contain book title, author, and rating
    """
    # Init Function
    runique = np.unique(ratings_labels)
    predictions = {}
    output_predictions = {}
    count = 1
    
    # Predict for each unique rating
    for x in runique:
        if ratings_mappings[x] >= rating_start and ratings_mappings[x] < rating_end:
            # print(f'encode{x} = {ratings_mappings[x]}')
            f'encode{x} = {ratings_mappings[x]}'
            prediction = model.predict([[input_genre, x]])
            predictions[x] = prediction

    #Print Predictions
    for p in predictions.keys():

        # Get book name from title mapping
        bookname = title_mappings[int(predictions[p])]

        # Get index in dataframe to find location of book
        title_index = books[books['book_title'] == bookname].index

        # Pull Author and rating data from location
        author = books.loc[title_index.values,'book_authors'].values[0]
        rating = books.loc[title_index.values,'book_rating'].values[0]
        
        # Create an array to contain strings relating to book 
        book_prediction = [bookname, author, rating]
        
        # Add book to output predictions    
        if not book_prediction in output_predictions.values():
            output_predictions[count] = book_prediction
            count = count + 1
    
    return output_predictions
    
## Create Printable Object
def create_printable_object(book_prediction_list):
    """
        This creates an object to print a list based on the dictionary of book predictions
        Output - list of strings to print
    """
    # Init
    forprint = []
    for p in book_prediction_list.keys():
        # Create printable list of predictions
        printable = f'{p}: {book_prediction_list[p][0]} by {book_prediction_list[p][1]} (GR Rating {book_prediction_list[p][2]})'
        forprint.append(printable)
            
    # Return printable list
    return forprint

## Print Predictions as a book list
def print_books(forprint):
    print(f'For Genre {genre_mappings[input_genre]}')
    count = 1
    for p in forprint:
        print(p)
    
## Choose Book
#def choose_book(predictions, rating):
def choose_book(input_genre,rating_start,rating_end):
    """
        Recursive function checks titles with user 
        Will do additional prediction to get a title if initial
        prediction does not produce a book user wants
        Output - Number for title of book selection
    """
    #Print Predictions as a book list
    final_prediction = []
    predictions = predict_books(input_genre,rating_start,rating_end)
    forprint = create_printable_object(predictions)
    print_books(forprint)
    print('\n')
    
    # Inquire user about printed titles
    print("Do any of these titles interest you?!\n")
    rating_next = float(rating_start - 0.3)
    yes = input("Y/N: ")
    yes.lower()
    
    # Check User Input
    if yes == 'y':
        title_num = input("Which title interests you, input number: ")
        final_prediction = predictions[int(title_num)]
    elif yes == 'n':
        # Check rating is not too low
        if float(predictions[1][2]) > (rating_next+0.5):
            print("If you do not like this selection, try again with a different genre.\n")
            return predictions[1]
        final_prediction = choose_book(input_genre,rating_next,rating_start)
        
    else:
        print("This is not a valid input, try again.")
        final_prediction = choose_book(input_genre,rating_start,rating_end)
    
    # Return the chosen book
    return final_prediction

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

###### Predict this item/ Multiple Predictions######
# Specify Genre - Intention to get genre from user input
input_genre = 200

# Inquire about which title reader would like to see
book_select = choose_book(input_genre,4.6,5.1)

# Get index in dataframe to find location of book
title_index = books[books['book_title'] == book_select[0]].index
description = books.loc[title_index.values,'book_desc'].values[0]
print(f'\nDescription of {book_select[0]} by {book_select[1]}: \n\n{description}\n')