import pandas as pd
import numpy as np

pd.set_option('precision', 1)

books = pd.Series(['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland'])
authors = pd.Series(['Chales Dickens', 'John Steinbeck', 'William Shakespear', 'H. G. Wells', 'Lewis Carroll'])
user_1 = pd.Series([3.2, np.nan, 2.5])
user_2 = pd.Series([5., 1.3, 4.0, 3.8])
user_3 = pd.Series([2.0, 2.3, np.nan, 4])
user_4 = pd.Series([4, 3.5, 4, 5, 4.2])

dat = {
    'Author': authors, 
    'Book Title': books, 
    'User 1': user_1, 
    'User 2': user_2, 
    'User 3': user_3, 
    'User 4': user_4
}

book_ratings = pd.DataFrame(dat)

print(book_ratings)