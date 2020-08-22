import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Get Data from CSV and Drop unnecessary data items
books_fromcsv = pd.read_csv("new_data.csv", encoding='utf-8',delimiter=',')
books_dropna = books_fromcsv.dropna() # Drom Nan
books = books_dropna.drop_duplicates(subset='book_title', keep='first') # Drop duplicates
books.dataframeName = 'book_data.csv'
nRow, nCol = books.shape 
print(f'There are {nRow} rows and {nCol} columns')

# Using Langdetect remove any non-english books from list
from langdetect import detect 
# Debug print Original Shape
print(books.shape)

# Iterate over book description
for label, content in books.items():
    if label == 'book_desc':
        for i in range(nRow):
           
            # Check index in dataframe
            if i in content:
            
                # If Language is not English drop data
                try:
                    if(detect(content[i]) != 'en'):
                        books.drop(index=i, inplace=True)
                # If langdetect cannot get language 
                # Print and remove item
                except: 
                    title = books.loc[i,'book_title']
                    print(f'Couldnt detect lang desc for {title} desc={content[i]}')
                    books.drop(index=i, inplace=True)

# Debug print, New Shape
print(books.shape)

# Remove Extra columns (from reading cs)
for label, content in books.items():
    if('Unnamed' in label):
        books.drop(columns=[label], inplace=True)

# Debug check info
print(books.info())

# Put changed data into new file to use
books.to_csv('clean_data.csv')
