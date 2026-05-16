from flask import Flask, jsonify, request
#jsonify for json files, request- for api's
app = Flask(__name__)
#static data, isbn = publication no.
books = [
    {'id': 1, 'title':'1984', 'author':'George Orwell','available': True, 'isbn':'123456789'},
    {'id':2, 'title':'To kill a mockingbird', 'author': 'Harpenter', 'available': True, 'isbn': '234567'}
]

# Get method
# Reading and displaying all the books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books}), 200

# Get method
# Reading a specific book
@app.route('/api/books/<int:bookid>', methods=['GET'])
def get_book(bookid):
    book = next((b for b in books if b['id'] == bookid), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book)


# Post method
# add new book
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.json
    if 'title' not in new_book or 'author' not in new_book or 'isbn' not in new_book:
        return jsonify({'error': 'invalid book data'}), 400
    new_book['id'] = books[-1]['id'] + 1 if books else 1
    new_book['available'] = True
    books.append(new_book)
    return jsonify(new_book), 201

# put method
@app.route('/api/books/update/<int:bookid>', methods= ['PUT'])
def update_book(bookid):
    updated_data = request.json
    book = next((b for b in books if b['id'] == bookid), None)
    if book is None:
        return jsonify({'error':'Book not found'}), 404
    book.update(updated_data)
    return jsonify(book)


# delete method
@app.route('/api/books/remove/<int:bookid>', methods=['DELETE'])
def delete_book(bookid):
    global books # take outerside books variable
    books = [b for b in books if b['id']!= bookid]
    return jsonify({'result':'Book is deleted'}), 200


if __name__ =='__main__':
    app.run(debug=True)