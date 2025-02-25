
from models import Books, db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, DataError
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

class Service:
    @staticmethod
    def get_book_by_id(id):
        return Books.query.filter(Books.id==id).all()

    @staticmethod
    def search_book(props):
        #min_price=None, max_price=None, min_time=None, max_time=None, title=None, genre=None, isbn=None, genre=None
        search= Books.query
        if props['min_price']:
            search = search.filter(Books.price >= props['min_price'])
        if props['max_price']:
            search = search.filter(Books.price <= props['max_price'])
        if props['min_time']:
            search = search.filter(Books.publication_time >= props['min_time'])
        if props['max_time']:
            search = search.filter(Books.publication_time <= props['max_time'])
        if props['title']:
            search = search.filter(Books.title.like('%' + props['title'] + '%'))
        if props['genre']:
            search = search.filter(Books.genre.like(props['genre']))
        if props['isbn']:
            search = search.filter(Books.isbn.like(props['isbn']))
        if props['quantity']:
            search = search.filter(Books.quantity >= props['quantity'])
        return search.order_by(Books.title).all()

    @staticmethod
    def add_book(props):
        #add a new user to the database
        book=Books(title=props['title'], isbn=props['isbn'], publication_time=props['publication_time'], genre= props['genre'], price=props['price'], quantity=props['quantity'])
        try:
            db.session.add(book)
            db.session.commit()
        except IntegrityError:
            return 0
        return 1

    @staticmethod
    def update_book(props):
        try:
            book = Books.query.get_or_404(props['id'])  # Raises 404 if not found

            for key, value in props.items():
                # Check if the key is a valid column name in the User model
                if hasattr(Books, key) and key != 'id' and value:  # Prevent setting the ID
                    setattr(book, key, value)  # Dynamically sets User object's attributes

            db.session.commit()
            return book
        except Exception as e:  # Catch potential DB errors
            db.session.rollback()  # Important to rollback on error
            print(f"Error updating user: {e}")  # Log the error for debugging
            raise  # Re-raise the exception to be handled by caller
            # Or return an error value if you don't want to re-raise
            # return None  # Example: Return None on failu


    @staticmethod
    def delete_book(id):
        count= Books.query.filter(Books.id== id).delete()
        db.session.commit()
        return count