from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)


BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

@app.route('/books', methods=['get'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS,
    })


@app.route('/ping', methods=['get'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
