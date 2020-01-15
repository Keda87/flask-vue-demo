import uuid

from quart import Quart, jsonify, request
from quart_cors import cors

DEBUG = True

app = Quart(__name__)
app.config.from_object(__name__)

cors(app)


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


@app.route('/books', methods=['get', 'post'])
async def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = await request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
        })
        response_object['books'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['put', 'delete'])
async def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = await request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    elif request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


@app.route('/ping', methods=['get'])
async def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
