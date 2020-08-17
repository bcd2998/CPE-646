from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
#import skimage.color
#import skimage.io
#import skimage.viewer
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Distribution graphs (histogram/bar graph) of column data
#https://www.kaggle.com/kerneler/starter-goodreads-best-books-ever-4ae0203d-6
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    #print(df.info())
    #print(df.columns.values)
    nunique = df.nunique()
    print(nunique)
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] <2000]] # For displaying purposes, pick columns that have between 1 and 50 unique values
    print(df)
    nRow, nCol = df.shape
    columnNames = list(df)
    #print(list(df))
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num = None, figsize = (20 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()

# Correlation matrix
def plotCorrelationMatrix(df, graphWidth):
    filename = df.dataframeName
    df = df.dropna('columns') # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {filename}', fontsize=15)
    plt.show()
    
    # Scatter and density plots
def plotScatterMatrix(df, plotSize, textSize):
    df = df.select_dtypes(include =[np.number]) # keep only numerical columns
    # Remove rows and columns that would lead to df being singular
    df = df.dropna('columns')
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    columnNames = list(df)
    if len(columnNames) > 10: # reduce the number of columns for matrix inversion of kernel density plots
        columnNames = columnNames[:10]
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k = 1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
    plt.suptitle('Scatter and Density Plot')
    plt.show()

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
            if '|' in str(content[i]):
                if 'Sports' in str(c[i][0]):
                    c[i][0] = 'Sports'
                elif 'Sports' in str(c[i][1]):
                    c[i][1] = 'Sports'
                    
                if str(c[i][1]) == 'Classics':
                    books['genres'] = books['genres'].replace([f'{content[i]}'],f'{c[i][1]}|{c[i][0]}')
                elif str(c[i][1]) == 'Young Adult':
                    books['genres'] = books['genres'].replace([f'{content[i]}'],f'{c[i][1]}|{c[i][0]}')
                else:
                    books['genres'] = books['genres'].replace([f'{content[i]}'],f'{c[i][0]}|{c[i][1]}')
     

# Functions to graph
plotPerColumnDistribution(books,10,1)
#plotCorrelationMatrix(books, 8)
#plotScatterMatrix(books, 12, 10)

# Put changed data into new file to use
#books.to_csv('new_data.csv')
