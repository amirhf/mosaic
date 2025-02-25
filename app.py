from flask import Flask, request, jsonify

from config import Config
#import psycopg2
from services.service import Service
from extensions import db
import utils


app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)


# Ensure connections are closed properly
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

'''
1. Get a single book by id:
Return details of a specific book.
2. Get books:
a. Optional parameters to filter books based on the range of price.
b. Optional parameters to filter books based on the range of publication time.
c. Optional parameters to filter and return a list of books for other columns.
You can choose one of the columns to reduce time.
3. Create a book:
Add a new book.
4. Update a book:

BE Dev - Bookstore Inventory Management System 3

Update the details of a specific book.
5. Delete a book by id:
Delete a book from the inventory.
'''
@app.route('/book')
def get_book():
    id = request.args.get('id')

    if not id:
        return "Book not found", 404
    books= Service.get_book_by_id(id)
    if not books:
        return "Book not found", 404
    print(vars(books[0]))
    return jsonify(books[0].to_dict())

'''
    id = db.Column(db.Integer,auto_increment=True, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(255), unique=True, nullable=False)
    publication_time = db.Column(db.DateTime)
    genre = db.Column(db.String(255))
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer())
'''
@app.route('/search')
def search_books():
    req=request.args
    props={'id':req.get('id',None), 'title':req.get('title',None), 'isbn':req.get('isbn', None), 'genre':req.get('genre',None),
           'quantity':req.get('quantity', None),'min_price': req.get('min_price',None), 'max_price':req.get('max_price',None),'min_time':req.get('min_time',None),'max_time':req.get('max_time',None) }
    books = Service.search_book(props)
    if not books:
        return "No books found", 404

    result= [book.to_dict() for book in books]
    return jsonify(result)

@app.route('/addBook', methods=['POST'])
def add_book():
    req= request.form
    props=utils.req_to_book_props(req)
    print(props)

    count=Service.add_book(props)
    db.session.commit()
    if count == 0:
        return 'Failed to add the book', 409
    return f'Book {req.get("title")} added'

@app.route('/updateBook', methods=['PUT'])
def update_book():
    req= request.form
    props=utils.req_to_book_props(req)

    rows= Service.update_book(props)
    db.session.commit()
    if rows == 0:
        return 'No Books Found', 404
    return f'Book {props["id"]} updated'

@app.route('/deleteBook', methods=['DELETE'])
def delete_book():
    id=request.form['id']

    rows = Service.delete_book(id)
    db.session.commit()
    if rows == 0:
        return 'No Books Found', 404
    return f'Book {id} deleted'

if __name__ == '__main__':
    app.run()
