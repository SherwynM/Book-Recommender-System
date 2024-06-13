from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('data/model.pkl', 'rb'))
book_names = pickle.load(open('data/book_name.pkl', 'rb')).tolist()
final_rating = pickle.load(open('data/filtered_final.pkl', 'rb'))
book_pivot = pickle.load(open('data/book_pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url

def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    return books_list, poster_url


@app.route('/', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        book_name_val = request.form['query']
        if book_name_val not in book_names:
            return render_template("pagenotfound.html")
        else:
            recommended_books, poster_url = recommend_book(book_name_val)
            return render_template("index.html", book_names=book_names, book_set=recommended_books[1:], poster=poster_url[1:],val=book_name_val,quotes="'")
    elif request.method == 'GET':
        return render_template("index.html", book_names=book_names)

@app.template_filter('zip')
def zip_filter(a, b):
    return zip(a, b)

if __name__ == '__main__':
    app.run()
