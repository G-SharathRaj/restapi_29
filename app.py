from flask import Flask , jsonify

todo = Flask(__name__)

students=[
    {
        "id":1,
        "name":"yesh",
        "age":20
    },
    {
        "id": 2,
        "name": "yeshan",
        "age": 25
    },
    {
        "id": 3,
        "name": "yeshwanth",
        "age": 10
    },
    {
        "id":4,
        "name":"Leo Das",
        "age":21
    }
]
@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/students/get/<int:id>')
def get_student_by_id(id):
    for std in students:
        if std['id'] == id:
            return jsonify(std)
    return jsonify('not found')

if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )