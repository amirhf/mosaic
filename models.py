from extensions import db

'''
Design a books table that includes fields for id (primary key), title, author, ISBN
(unique field), publication_time, genre, price and quantity.
'''
class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,auto_increment=True, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(255), unique=True, nullable=False)
    publication_time = db.Column(db.DateTime)
    genre = db.Column(db.String(255))
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'isbn': self.isbn,
            'publication_time': self.publication_time,
            'price': self.price,
            'quantity': self.quantity
        }

