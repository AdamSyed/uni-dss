from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initiate variables
# basedir = os.path.abspath(os.path.dirname(__file__))

# Initiate application
application = Flask(__name__)

# Database
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:msci436project@uni-dss.cmuqyhsxn149.us-east-2.rds.amazonaws.com:3306/uni_dss'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To prevent any complaints in console

# Initialize db
db = SQLAlchemy(application)

# Initiate marshmallow
ma = Marshmallow(application)

# Student Model/Class
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Student Schema - i think for marshmallow
class StudentSchema(ma.Schema):
    class Meta: #all the variables you want to see
        strict = True
        fields = ('id', 'name', 'email', 'password')

# Initiate Schema
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# ENDPOINT - Create a Student
@application.route('/student-create', methods=['POST'])
def add_student():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    new_student = Student(name, email, password)

    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)

# ENDPOINT - Get all students
@application.route('/students-all',methods=['GET'])
def get_students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result)

# ENDPOINT - Get a student by id
@application.route('/student/<id>',methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    return student_schema.jsonify(student)

# ENDPOINT - Update a Student
@application.route('/student/<id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)

    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    student.name = name
    student.email = email
    student.password = password
    
    db.session.commit()

    return student_schema.jsonify(student)

# Run server
if __name__ == '__main__':
    application.run(host='0.0.0.0')