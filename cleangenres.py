import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Accessing Dataset
nba = pd.read_csv("book_data.csv",delimiter=',')#, nrows=1000)

# Drop unwanted columns
books = nba.drop(columns = ['book_edition','book_format','book_isbn','book_pages',
                            'book_rating_count','book_review_count'])
books.dataframeName = 'book_data.csv'
nRow, nCol = books.shape
print(f'There are {nRow} rows and {nCol} columns')

# Editing genres to create less unique genres
for label, content in books.items():
    if label == 'genres':
        #print(f'label: {label}')
        c = content.str.split('|')     
        for i in range(nRow):
            #print(f'content: {content[i]}')
            
            zero = ''
            one = ''
            if '|' in str(content[i]):
          
                # Check For Fiction or Non Fiction
                for j in range(len(c[i])):
                    # Check if item says nonfiction
                    if 'Nonfiction' in str(c[i][j]) or 'Non fiction' in str(c[i][j]) or 'Non Fiction' in str(c[i][j]):
                        zero = 'Nonfiction'
                        break
                    # Check if item says fiction
                    elif 'Fiction' in str(c[i][j]):
                        if 'Adult' in str(c[i][j]):
                            zero = 'Fiction'
                        else:
                            zero = c[i][j]
                            
                        break
                    else:
                        # Assume Fiction if not labeled nonfiction
                        zero = 'Fiction'
                
                # Check to get another specific genre
                for j in range(len(c[i])):
                    if not 'Fiction' in str(c[i][j]) and not 'Nonfiction' in str(c[i][j]) and not 'Non fiction' in str(c[i][j]) and not 'Non Fiction' in str(c[i][j]):
                        # remove genres that may come up due to goodreads users
                        if 'Not Finish' in c[i][j]:
                            continue
                        if 'Unfinished' in c[i][j]:
                            continue
                        if 'Own' in c[i][j]:
                            continue
                            
                        # remove specific TV genre items
                        if 'Media Tie In' in c[i][j]:
                            continue
                        if 'Tv' in c[i][j]:
                            continue
                        if 'Star Trek' in c[i][j]:
                            continue
                        if 'Star Wars' in c[i][j]:
                            continue
                        if 'Doctor Who' in c[i][j]:
                            continue
                            
                        # Remove any award genre given
                        if 'Award' in c[i][j]:
                            continue
                            
                        # remove genres without much description
                        if 'New Adult' in c[i][j]:
                            continue 
                        if 'Book Club' in c[i][j]:
                            continue
                        if 'Classics' in c[i][j]:
                            continue
                            
                        # If genre already contains info then do not include it
                        if 'Christian' in c[i][j] or 'Catholic' in c[i][j]:
                            if 'Fiction' in zero:
                                zero = f'Christian Fiction'
                            else:
                                zero = f'Christian Nonfiction'
                            continue
                        
                        if 'Science' in c[i][j] and 'Science' in zero:
                            continue
                            
                        # Combine some categories
                        if 'Gay' in c[i][j] or 'Glbt' in c[i][j]:
                            one = 'Lgbt'
                        else:
                            one = c[i][j]
                            
                        break
                        
                
                # Combine some categories
                if 'Sports' in str(one):
                    one = 'Sports'
                elif 'Romantic' in str(one) or 'Romance' in str(one):
                    one = 'Romance'
                elif 'Computer' in str(one):
                    one = 'Computers'
                    
                # Make sure two for each entry
                if len(one) == 0 and 'Christian' in zero:
                    one = 'Religion'
                elif len(one) == 0:
                    one = 'Adult'
                                
            else:
                # Although this may be incorrect assume 
                # anything with one genre is nonfiction
                # unless fiction is in the genre
                if 'Fiction' in str(content[i]):
                    zero = 'Fiction'
                    one = content[i]
                else:
                    zero = 'Nonfiction'
                    one = content[i]
                
            # Replace genre column with new genre
            books['genres'] = books['genres'].replace([f'{content[i]}'],f'{zero}|{one}')
           
# Debug prints to show new genres           
nunique = books.nunique()
print(nunique)

new_books = books.dropna()
genres = np.unique(new_books['genres'])
print(genres)

# Put changed data into new file to use
books.to_csv('new_data.csv')