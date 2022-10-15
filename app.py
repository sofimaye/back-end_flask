import json

from flask import Flask, request, render_template, abort, Response

app = Flask(__name__)
"""basic REST API"""

# data's look
users = [
    {
        'user_id': 1,
        'username': 'root'
    }
]

categories = [
    {
        'category_id': 2,
        'category_description': 'cosmetics'
    }
]

records = [
    {
        'record_id': 3,
        'user_id': 1,
        'category_id': 2,
        'description': 'cream was bought at market',
        'cost_in_uah': 500
    }
]


# post and get all categories
@app.route('/categories', methods=['POST'])
def post_categories():
    category = request.json
    categories.append(category)
    print(category)
    return Response(json.dumps(category), status=201, mimetype='application/json')


@app.route('/categories', methods=['GET'])
def get_categories():
    return categories


# get all user's records by user's id
@app.route('/users/<int:user_id>/records', methods=['GET'])
def get_records(user_id):
    records_by_user = list(filter(lambda record: record['user_id'] == int(user_id), records))
    return records_by_user


# get all user's records by user's id and by category
@app.route('/users/<int:user_id>/records', methods=['GET'])
def get_records_by_category(user_id):
    category_id = request.args.get('category_id')
    if category_id is not None:
        records_by_cat = list(
            filter(lambda record: record['user_id'] == int(user_id) and record['category_id'] == int(category_id),
                   records))
    else:
        records_by_cat = list(filter(lambda record: record['user_id'] == int(user_id), records))
    if not records_by_cat:
        abort(400)
    return records_by_cat


# post and get all records
@app.route('/records', methods=['POST'])
def create_record():
    category_records = request.json
    records.append(category_records)
    return Response(json.dumps(category_records), status=201, mimetype='application/json')


@app.route('/records', methods=['GET'])
def find_records():
    return records


# form's request (ui)
@app.route('/', methods=['POST', 'GET'])
def info():
    if request.method == 'POST':
        record = {'record_id': request.form['expense_id'], 'user_id': int(request.form['user_id']),
                  'category_id': int(request.form['category_id']), 'description': request.form['description'],
                  'cost_in_uah': request.form['cost']}
        category = {
            'category_id': int(request.form['category_id']),
            'category_description': request.form['description']
        }
        records.append(record)
        categories.append(category)
        return record
    else:
        return render_template('user_form.html')


if __name__ == '__main__':
    app.run()
