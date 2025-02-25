def req_to_book_props(req):
    props = {'id': req.get('id', None), 'title': req.get('title', None), 'isbn': req.get('isbn', None),
         'genre': req.get('genre', None),
         'quantity': req.get('quantity', None), 'price': req.get('price', None),
         'publication_time': req.get('publication_time', None)}
    return props