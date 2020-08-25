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

# Genres
genre_labels = gle_genre.fit_transform(books['genres'])
genre_mappings = {index: label for index, label in 
                  enumerate(gle_genre.classes_)}

# Ratings
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

# User Input
print("Welcome to the Book Recommender System!")
print("")
fictionOrNon = input("Please enter Fiction if you are looking for Fiction genres or Nonfiction if you are looking for Nonfiction genres: ")
fictionOrNon = fictionOrNon.lower()
user_genre= None
if fictionOrNon == 'fiction':
    print("")
    print("The following are the types of Fiction Genres offered:")
    Fiction_Genres = ['Animal', 'Biblical', 'Bizarro', 'Christian', 'Fan', 'Fiction', 'Flash', 'Gay', 'Historical', 'Lds', 'Lesbian', 
    'Literary', 'Military', 'Realistic', 'Science', 'Speculative', 'Weird', 'Womens']
    for genre in Fiction_Genres:
        print(genre)
    print("")
    fictionType = input("Please enter which Fiction Genre from the above that you are looking for: ")
    fictionType = fictionType.lower()
    
    if fictionType == 'animal':
        print("")
        print("The following are the types of Animal Fiction Genres offered:")
        Animal_Genres = ['Animals', 'Childrens']
        for genre in Animal_Genres:
            print(genre)
        print("")
        animalType = input("Please enter which of the above Animal Fiction types you are looking for: ")
        animalType = animalType.lower()
        user_genre = 'Animal Fiction|' + animalType

    elif fictionType == 'biblical':
        print("")
        print("Biblical Fiction only offers Biblical Fiction History")
        biblicalType = 'History'
        biblicalType = biblicalType.lower()
        user_genre = 'Biblical Fiction|' + biblicalType

    elif fictionType == 'bizarro':
        print("")
        print("Bizarro Fiction only offers Bizarro Fiction Horror")
        bizarroType = 'Horror'
        bizarroType = bizarroType.lower()
        user_genre = 'Bizaro Fiction|' + bizarroType

    elif fictionType == 'christian':
        print("")
        print("The following are the types of Christian Fiction genres offered:")
        ChristianFict_Genres = ['Academic', 'American', 'Amish', 'Apocalyptic', 'Biography', 'Chick Lit', 'Childrens', 'Contemporary', 
        'Cultural', 'Drama', 'Evangelism', 'Family', 'Fantasy', 'Historical', 'Holiday', 'Horror', 'Inspirational', 'Lds', 'Leadership', 
        'Literature', 'Love Inspired', 'Marriage', 'Mystery', 'Paranormal', 'Prayer', 'Reference', 'Romance', 'Self Help', 'Short Stories', 
        'Spirituality', 'Suspense', 'Thriller', 'War', 'Westerns', 'Young Adult']
        for genre in ChristianFict_Genres:
            print(genre)
        print("")
        christainFictionType = input("Please enter which of the above Christian Fiction types you are looking for: ")
        christainFictionType = christainFictionType.lower()
        user_genre = 'Christian Fiction|' + christainFictionType

    elif fictionType == 'fan':
        print("")
        print("The following are the types of Fan Fiction Genres offered:")
        Fan_Genres = ['Fantasy', 'Lgbt', 'Romance']
        for genre in Fan_Genres:
            print(genre)
        print("")
        fanType = input("Please enter which of the above Fan Fiction Types you are looking for: ")
        fanType = fanType.lower()
        user_genre = 'Fan Fiction|' + fanType

    elif fictionType == 'fiction':
        print("")
        print("The following are the types of Fiction Types offered:")
        Fiction_Genres = ['Abandoned', 'Academic', 'Action', 'Adventure', 'Alcohol', 'Alternate History', 'American', 'Amish', 'Animals',
        'Anthropology', 'Apocalyptic', 'Art', 'Asian Literature', 'Audiobook', 'Autobiography', 'Aviation', 'Biography', 
        'Buffy The Vampire Slayer', 'Business', 'Canon', 'Central Africa', 'Chick Lit', 'Childrens', 'Classic Literature', 'Colouring Books', 
        'Combat', 'Comics', 'Computers', 'Contemporary', 'Couture', 'Crafts', 'Crime', 'Criticism', 'Cultural', 'Culture', 'Currency', 'Cyberpunk', 
        'Dark', 'Dc Comics', 'Death', 'Design', 'Diary', 'Disability', 'Drama', 'Dungeons and Dragons', 'Dystopia', 'Earth', 'Eastern Africa', 
        'Economics', 'Education', 'Environment', 'Erotica', 'Esoterica', 'European Literature', 'Fairy Tales', 'Family', 'Fantasy', 'Female Authors', 
        'Folklore', 'Food and Drink', 'Football', 'Gamebooks', 'Games', 'Gardening', 'Gender', 'Gothic', 'Graphic Novels Comics', 'Harlequin', 
        'Health', 'Heroic Fantasy', 'Historical', 'Holiday', 'Horror', 'Humor', 'Language', 'Law', 'Lds', 'Leadership', 'Lgbt', 'Linguistics', 
        'Literature', 'Love', 'Magical Realism', 'Manga', 'Marriage', 'Medical', 'Menage', 'Mental Health', 'Military', 'Military History', 
        'Modern', 'Movies', 'Music', 'Mystery', 'Mythology', 'New York', 'Nobel Prize', 'North American History', 'Northern Africa', 'Novella', 
        'Novels', 'Occult', 'Paranormal', 'Plays', 'Poetry', 'Politics', 'Polyamorous', 'Prayer', 'Productivity', 'Pulp', 'Race', 'Reference', 
        'Relationships', 'Retellings', 'Roman', 'Romance', 'School Stories', 'Sequential Art', 'Sexuality', 'Shapeshifters', 'Short Stories', 
        'Soccer', 'Social Issues', 'Social Movements', 'Sociology', 'Southern Africa', 'Space', 'Spirituality', 'Sports', 'Spy Thriller', 
        'Superheroes', 'Suspense', 'Textbooks', 'The United States Of America', 'Thriller', 'Time Travel', 'Travel', 'True Story', 'United States', 
        'Urban', 'War', 'Warfare', 'Western Africa', 'Westerns', 'Witchcraft', 'Womens', 'World Of Warcraft', 'World War II', 'Writing', 'Young Adult']
        for genre in Fiction_Genres:
            print(genre)
        print("")
        fictType = input("Please enter which of the above Fiction Types you are looking for: ")
        fictType = fictType.lower()
        user_genre = 'Fiction|' + fictType

    elif fictionType == 'flash':
        print("")
        print("Flash Fiction only has Short Stories available")
        flashType = 'Short Stories'
        flashType = flashType.lower()
        user_genre = 'Flash Fiction|' + flashType

    elif fictionType == 'gay':
        print("")
        print("The following are the types of Gay Fiction offered: ")
        Gay_Genres = ['Lgbt', 'Romance']
        for genre in Gay_Genres:
            print(genre)
        print("")
        gayType = input("Please enter which of the above Gay Fiction Types you are looking for: ")
        gayType = gayType.lower()
        user_genre = 'Gay Fiction|' + gayType

    elif fictionType == 'historical':
        print("")
        print("The following are the types of Historical Fiction offered:")
        Historical_Genres = ['Adventure', 'American', 'Animals', 'Art', 'Childrens', 'Cultural', 'European Literature', 'Fairy Tales', 
        'Fantasy', 'Historical', 'Holiday', 'Horror', 'Humor', 'Lgbt', 'Literature', 'Mystery', 'Paranormal', 'Philosophy', 'Plays', 
        'Poetry', 'Religion', 'Romance', 'School Stories', 'Sequential Art', 'Short Stories', 'Sports', 'Thriller', 'War', 'Westerns', 
        'World War II', 'Young Adult']
        for genre in Historical_Genres:
            print(genre)
        print("")
        historicalType = input("Please enter which of the above Historical Fiction Types you are looking for: ")
        historicalType = historicalType.lower()
        user_genre = 'Historical Fiction|' + historicalType

    elif fictionType == 'lds':
        print("")
        print("The following are the types of Lds Fiction offered:")
        Lds_Genres = ['Lds', 'Young Adult']
        for genre in Lds_Genres:
            print(genre)
        print("")
        ldsType = input("Please enter which of the above Lds Fiction Types you are looking for: ")
        ldsType = ldsType.lower()
        user_genre = 'Lds Fiction|' + ldsType

    elif fictionType == 'lesbian':
        print("")
        print("The following are the types of Lesbian Fiction offered:")
        Lesbian_Genres = ['Fantasy', 'Lgbt']
        for genre in Lesbian_Genres:
            print(genre)
        print("")
        lesbianType = input("Please enter which of the above Lesbian Fiction Types you are looking for: ")
        lesbianType = lesbianType.lower()
        user_genre = 'Lesbian Fiction|' + lesbianType

    elif fictionType == 'literary':
        print("")
        print("The following are the types of Literary Fiction offered:")
        Literary_Genres = ['Adult', 'Autobiography', 'Cultural', 'European Literature', 'Humor', 'Literature', 'Music', 'Mystery', 
        'Plays', 'Poetry', 'Romance', 'Suspense', 'Young Adult']
        for genre in Literary_Genres:
            print(genre)
        print("")
        literaryType = input("Please enter which of the above Literary Types you are looking for: ")
        literaryType = literaryType.lower()
        user_genre = 'Literary Fiction|' + literaryType

    elif fictionType == 'military':
        print("")
        print("The following are the types of Military Fiction offered:")
        Military_Genres = ['Adventure', 'Biography', 'Fantasy', 'Historical', 'History', 'Horror', 'Lgbt', 'Military History', 'Poetry', 
        'Politics', 'Romance', 'War', 'Young Adult']
        for genre in Military_Genres:
            print(genre)
        print("")
        militaryType = input("Please enter which of the above Military Fiction Types you are looking for: ")
        militaryType = militaryType.lower()
        user_genre = 'Military Fiction|' + militaryType

    elif fictionType == 'realistic':
        print("")
        print("The following are the types of Realistic Fiction offered:")
        Realistic_Genres = ['Abandoned', 'Adult', 'Adventure', 'Animals', 'Childrens', 'Contemporary', 'Cultural', 'European Literature', 
        'Fantasy', 'Historical', 'Humor', 'Inspirational', 'Mystery', 'Parenting', 'Philosophy', 'Poetry', 'Psychology', 'Romance', 
        'Sequential Art', 'Slice Of Life', 'Sports', 'Young Adult']
        for genre in Realistic_Genres:
            print(genre)
        print("")
        realisticType = input("Please enter which of the above Realistic Fiction Types you are looking for: ")
        realisticType = realisticType.lower()
        user_genre = 'Realistic Fiction|' + realisticType

    elif fictionType == 'science':
        print("")
        print("The following are the Genres of Science Fiction offered:")
        Science_Genres = ['Fantasy', 'Romance', 'Science']
        for genre in Science_Genres:
            print(genre)
        print("")
        scienceType = input("Please enter which of the above Science Fiction Genres you are looking for: ")
        scienceType = scienceType.lower()
        if scienceType == 'fantasy':
            print("")
            print("The following are the types of Science Fiction Fantasy offered:")
            Fantasy_Genres = ['Adult', 'Anthologies', 'Fantasy', 'Horror', 'Humor', 'Modern', 'Sequential Art','Young Adult']
            for genre in Fantasy_Genres:
                print(genre)
            print("")
            sType = input("Please enter which of the above Science Fiction Fantasy types you are looking for: ")
        elif scienceType == 'romance':
            print("")
            print("The following are the types of Science Fiction Romance offered:")
            Romance_Genres = ['Erotica', 'Romance']
            for genre in Romance_Genres:
                print(genre)
            print("")
            sType = input("Please enter which of the above Science Fiction Romance types you are looking for: ")
        elif scienceType == 'science':
            print("")
            print("The following are the types of Science Fiction offered:")
            Science_Genres = ['40k', 'Action', 'Adventure', 'Aliens', 'Alternate History', 'Anthologies', 'Apocalyptic', 'Art', 'Audiobook', 
            'Business', 'Childrens', 'Comics', 'Contemporary', 'Cultural', 'Cyberpunk', 'Dystopia', 'Erotica', 'European Literature', 
            'Fantasy', 'Feminism', 'Futuristic', 'Games', 'Gender', 'Horror', 'Humor', 'Lds', 'Lgbt', 'Literature', 'Marvel', 'Mathematics', 
            'Movies', 'Mystery', 'Novels', 'Paranormal', 'Philosophy', 'Plays', 'Politics', 'Pop Culture', 'Reference', 'Religion', 'Robots', 
            'Romance', 'Sequential Art', 'Short Stories', 'Space', 'Sports', 'Spy Thriller', 'Steampunk', 'Technology', 'Thriller', 
            'Time Travel', 'War', 'Young Adult']
            for genre in Science_Genres:
                print(genre)
            print("")
            sType = input("Please enter which of the above Science Fiction types you are looking for: ")
        else:
            print("You did not select a valid Science Fiction Genre")
        sType = sType.lower()
        user_genre = 'Science Fiction|' + sType

    elif fictionType == 'speculative':
        print("")
        print("The following are the types of Speculative Fiction offered:")
        Speculative_Genres =['Fantasy', 'Horror', 'Mystery', 'Short Stories']
        for genre in Speculative_Genres:
            print(genre)
        print("")
        speculativeType = input("Please enter which of the above Speculative Fiction types you are looking for: ")
        speculativeType = speculativeType.lower()
        user_genre = 'Speculative Fiction|' + speculativeType

    elif fictionType == 'weird': 
        print("")
        print("The following are the types of Weird Fiction offered:")
        Weird_Genres = ['Fantasy', 'Horror']
        for genre in Weird_Genres:
            print(genre)
        print("")
        weirdType = input("Please enter which of the aabove Weird Fiction types you are looking for: ")
        weirdType = weirdType.lower()
        user_genre = 'Weird Fiction|' + weirdType

    elif fictionType == 'womens':
        print("")
        print("The following are the types of Womens Fiction offered:")
        Womens_Genres = ['Chick Lit', 'Contemporary', 'Fantasy', 'Holiday', 'Humor', 'Mystery', 'Paranomral', 'Romance', 'Thriller', 
        'Young Adult']
        for genre in Womens_Genres:
            print(genre)
        print("")
        womensType = input("Please enter which of the above Womens Fiction types you are looking for: ")
        womensType = womensType.lower()
        user_genre = 'Womens Fiction|' + womensType

    else:
        print("You did not enter a valid Fiction Type")

elif fictionOrNon == 'nonfiction':
    print("")
    nonType = input("Please enter Christian if you are looking for Christian Nonfiction and Nonfiction if you are looking for another kind of Nonfiction: ")
    nonType = nonType.lower()
    if nonType == 'christian':
        print("")
        print("The following are the types of Christian Nonfiction offered:")
        ChristianNon_Genres = ['Autobiography', 'Biography', 'Childrens', 'Cultural', 'Health', 'Inspirational', 'Lds', 'Leadership', 
        'Marriage', 'Old Testament', 'Philosophy', 'Poetry', 'Prayer', 'Reference', 'Relationships', 'Religion', 'Romance', 
        'Science', 'Self Help', 'Spirituality']
        for genre in ChristianNon_Genres:
            print(genre)
        print("")
        christianNon = input("Please enter which of the above Christian Nonfiction types you are looking for: ")
        christianNon = christianNon.lower()
        user_genre = 'Christian Nonfiction|' + christianNon
        
    elif nonType == 'nonfiction':
        print("")
        print("The following are the types of Nonfiction offered:")
        Non_Genres =["Abandoned", "Academic", "Adult", "Adventure", "Alcohol", "Aliens", " Anthologies", "Anthropology", "Architecture", 
        "Artifical Intelligence", "Asian Literature", "Audiobook", "Autobiography", "Aviation", "Biography Memoir", "Biology", "Buffy The Vampire Slayer",
         "Business", "Childrens", "Church", "Combat", "Computers", "Contemporary","Couture", "Crafts", "Crime", "Criticism", "Cultural", "Culture", "Currency",
         "Design", "Diary", "Dystopia", "Economics", "Education", "Envvironment", "Erotica", "Esoterica", "European Literature", "Family Law", "Fantasy", 
         "Female Authors", "Feminism", "Finance", "Folk Tales", "Food and Drink", "Football", "Games", "Gardening", "Gender", "Graphic Novels Comics", "Health", 
         "Historical", "History", "History and Politics", "Horror", "How To", "Humanities", "Humor", "Inspirational", "Kids", "Language", "Law", "Leadership",
         "Lgbt", "Literature", "Marriage", "Medical", "Mental Health", "Military History", "Movies", "Mystery", "Nature", "New York", "North American History", 
         "Northern Africa", "Nurses", "Occult", "Paranormal", "Paranormal Urban Fantasy", "Parenting", "Philosophy", "Plays", "Politics", "Polyamory", "Prayer",
          "Productivity", "Psychology","Race", "Reference", "Relationships", "Religion", "Romance", "Science", "Self Help", "Sequential Art", "Sexuality", 
          "Short Stories", "Soccer", "Social", "Social Issues", "Social Movements", "Social Science", "Sociology", "Space", "Spirituality", "Sports", "Teaching", 
          "Textbooks", "The United States Of America", "Thriller", "Travel", "True Story", "United States", "War", "Witchcraft", "World War II", "Writing"]

        for genre in Non_Genres:
            print(genre)
        print("")    
        non = input("Please enter which of the above Nonfiction types you are looking for: ")
        non = non.lower()
        user_genre = 'Nonfiction|' + non
    else:
        print("You did not enter a valid NonFiction Type")
else:
    print("You did not enter a valid input!")
#For loop getting numeric value
for keys in genre_mappings:
    if user_genre.lower() == genre_mappings[keys].lower():
        input_genre = keys
        break
print("")

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
    count = 1
    # print(book_prediction_list)
    for p in book_prediction_list.keys():
        # Create printable list of predictions
        printable = f'{p}: {book_prediction_list[p][0]} by {book_prediction_list[p][1]} (GR Rating {book_prediction_list[p][2]})'
        
        forprint.append(printable)
        count += 1
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
    sorted_predictions = sorted(predictions.items(), key=lambda x:float(x[1][2]), reverse=True)
    predict = {}
    count = 1
    for i in sorted_predictions:
        predict[count] = i[1]
        count += 1
    forprint = create_printable_object(predict)
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
                # final_prediction = sorted_predictions[1]
        final_prediction = predict[int(title_num)]
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

###### Predict this item/ Multiple Predictions######
# Specify Genre - Intention to get genre from user input
# input_genre = 200

# Inquire about which title reader would like to see
book_select = choose_book(input_genre,4.6,5.1)

# Get index in dataframe to find location of book
title_index = books[books['book_title'] == book_select[0]].index
description = books.loc[title_index.values,'book_desc'].values[0]
print(f'\nDescription of {book_select[0]} by {book_select[1]}: \n\n{description}\n')
image_url = books.loc[title_index.values,'image_url'].values[0]
print(image_url)

import requests
from PIL import Image
url = image_url
image = Image.open(requests.get(url, stream=True).raw)
image.show()



    