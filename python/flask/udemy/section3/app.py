from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template


app = Flask(__name__)


stores = [
    {
        'name': 'My woderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    return "Welcome, Test WebAPI page"


@app.route('/test')
def render_test():
    # front-end
    # render_template: templates/index.html
    return render_template('index.html')


@app.route('/stores', methods=['GET'])
def get_stores():
    return jsonify(stores)


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    if not request_data:
        return jsonify({'messages': 'occur error json format'})

    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>/items', methods=['GET'])
def get_store_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})

    # XXX: change to 404 Not found
    return jsonify({'messages': 'not found item'})


@app.route('/store/<string:store_name>/item', methods=['POST'])
def add_item_to_store(store_name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == store_name:
            store['items'].append(request_data)
            return jsonify(request_data)

    return jsonify({'messages': 'not found store'})
