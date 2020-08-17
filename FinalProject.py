import pandas

data = 'book_data.csv'
dataset = pandas.DataFrame(pandas.read_csv(data))
new_dataset = dataset.drop(['book_edition', 'book_format', 'book_isbn', 'book_pages', 'book_rating_count', 'book_review_count'], axis = 1)

print(new_dataset)

# USe Naive Bayes first to classify the data based upon genre and rating
# Once Naive Bayes is applied use filtering to give the user back the top 10 recommendations based upon their input