from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import numpy as np
import json
# import os

# Initiate application
application = Flask(__name__)

# Database
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:msci436project@uni-dss.cmuqyhsxn149.us-east-2.rds.amazonaws.com:3306/uni_dss'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To prevent any complaints in console

# Initialize db
db = SQLAlchemy(application)

# Initiate marshmallow
ma = Marshmallow(application)

# Student Model/Class - SQLAlchemy
class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    d_education_quality = db.Column(db.Integer)
    d_ec_opportunity = db.Column(db.Integer)
    d_wellbeing = db.Column(db.Integer)
    d_community = db.Column(db.Integer)
    d_city_size = db.Column(db.Integer)
    d_school_size = db.Column(db.Integer)
    d_campus_age = db.Column(db.Integer)
    d_student_prof_ratio = db.Column(db.Integer)
    d_scholarship_likelihood = db.Column(db.Integer)
    d_city_cost = db.Column(db.Integer)
    d_co_op_availability = db.Column(db.Boolean)
    courses = db.relationship('Student_course', backref='student', lazy=True)
    categories = db.relationship('Student_category', backref='student', lazy=True)


    def __init__(self,first_name,last_name,email,password,age,d_education_quality,d_ec_opportunity,d_wellbeing,d_community,d_city_size,d_school_size,d_campus_age,d_student_prof_ratio,d_scholarship_likelihood,d_city_cost,d_co_op_availability):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.age = age
        self.d_education_quality = d_education_quality
        self.d_ec_opportunity = d_ec_opportunity
        self.d_wellbeing = d_wellbeing
        self.d_community = d_community
        self.d_city_size = d_city_size
        self.d_school_size = d_school_size
        self.d_campus_age = d_campus_age
        self.d_student_prof_ratio = d_student_prof_ratio
        self.d_scholarship_likelihood = d_scholarship_likelihood
        self.d_city_cost = d_city_cost
        self.d_co_op_availability = d_co_op_availability

# Student Schema - for marshmallow
class StudentSchema(ma.Schema):
    class Meta: #all the variables you want to see
        strict = True
        fields = ('student_id','first_name','last_name','email','password','age','d_education_quality','d_ec_opportunity','d_wellbeing','d_community','d_city_size','d_school_size','d_campus_age','d_student_prof_ratio','d_scholarship_likelihood','d_city_cost','d_co_op_availability')

# Initiate Student Schema
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# University Model/Class - SQLAlchemy
class University(db.Model):
    university_id = db.Column(db.Integer, primary_key=True)
    university_name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city_size = db.Column(db.Integer, nullable=False)
    uni_year_founded = db.Column(db.Integer, nullable=False)
    total_enrollment = db.Column(db.Integer, nullable=False)
    education_quality = db.Column(db.Integer, nullable=False)
    ec_opportunity = db.Column(db.Integer, nullable=False)
    wellbeing = db.Column(db.Integer, nullable=False)
    community = db.Column(db.Integer, nullable=False)
    city_size_index = db.Column(db.Integer, nullable=False)
    school_size_index = db.Column(db.Integer, nullable=False)
    campus_age_index = db.Column(db.Integer, nullable=False)
    student_prof_ratio = db.Column(db.Integer, nullable=False)
    scholarship_likelihood = db.Column(db.Integer, nullable=False)
    city_cost_index = db.Column(db.Integer, nullable=False)
    programs = db.relationship('Program', backref='university', lazy=True)
    images = db.relationship('University_img', backref='university', lazy=True)

    def __init__(self,university_id,university_name,address,city_size,uni_year_founded,total_enrollment,education_quality,ec_opportunity,wellbeing,community,city_size_index,school_size_index,campus_age_index,student_prof_ratio,scholarship_likelihood,city_cost_index):
        self.university_id = university_id
        self.university_name = university_name
        self.address = address
        self.city_size = city_size
        self.uni_year_founded = uni_year_founded
        self.total_enrollment = total_enrollment
        self.education_quality = education_quality
        self.ec_opportunity = ec_opportunity
        self.wellbeing = wellbeing
        self.community = community
        self.city_size_index = city_size_index
        self.school_size_index = school_size_index
        self.campus_age_index = campus_age_index
        self.student_prof_ratio = student_prof_ratio
        self.scholarship_likelihood = scholarship_likelihood
        self.city_cost_index = city_cost_index

# University Schema - for marshmallow
class UniversitySchema(ma.Schema):
    class Meta: #all the variables you want to see
        strict = True
        fields = ('university_id','university_name','address','city_size','uni_year_founded','total_enrollment','education_quality','ec_opportunity','wellbeing','community','city_size_index','school_size_index','campus_age_index','student_prof_ratio','scholarship_likelihood','city_cost_index')

# Initiate University Schema
university_schema = UniversitySchema()
universities_schema = UniversitySchema(many=True)

# Many to many relationship between program and category
# program_category = db.Table('program_category', db.Column('program_id', db.Integer,db.ForeignKey('program.program_id'),primary_key=True),db.Column('category_name',db.String(100),db.ForeignKey('category.category_name'),primary_key=True))

# Program Model/Class - SQLAlchemy
class Program(db.Model):
    program_id = db.Column(db.Integer, primary_key=True)
    university_id = db.Column(db.Integer, db.ForeignKey('university.university_id'),nullable=False)
    program_name = db.Column(db.String(500), nullable=False)
    degree = db.Column(db.String(500), nullable=False)
    ouac_code = db.Column(db.String(100), nullable=False)
    acceptance_grade = db.Column(db.Integer, nullable=False)
    co_op_availability = db.Column(db.Boolean, nullable=False)
    categories = db.relationship('Program_category', backref = 'program', lazy=True)

    def __init__(self,program_id,university_id,program_name,degree,ouac_code,acceptance_grade,co_op_availability):
        self.program_id = program_id
        self.university_id = university_id
        self.program_name = program_name
        self.degree = degree
        self.ouac_code = ouac_code
        self.acceptance_grade = acceptance_grade
        self.co_op_availability = co_op_availability

# Program Schema - for marshmallow
class ProgramSchema(ma.Schema):
    class Meta: #all the variables you want to see
        strict = True
        fields = ('program_id','university_id','program_name','degree','ouac_code','acceptance_grade','co_op_availability')

# Initiate Program Schema
program_schema = ProgramSchema()
programs_schema = ProgramSchema(many=True)

# University_img Model/Class - SQLAlchemy
class University_img(db.Model):
    img_id = db.Column(db.Integer, primary_key=True)
    university_id = db.Column(db.Integer, db.ForeignKey('university.university_id'),nullable=False)
    img_path = db.Column(db.String(500), nullable=False)

    def __init__(self,university_id,img_path):
        self.university_id = university_id
        self.img_path = img_path

# University_img Schema - for marshmallow
class University_ImgSchema(ma.Schema):
    class Meta: #all the variables you want to see
        strict = True
        fields = ('img_id','university_id','img_path')

# Initiate University_img Schema
university_img_schema = University_ImgSchema()
university_imgs_schema = University_ImgSchema(many=True)

# Program_category Model/Class - SQLAlchemy
class Program_category(db.Model):
    program_id = db.Column(db.Integer, db.ForeignKey('program.program_id'),primary_key=True)
    category_name = db.Column(db.String(100), primary_key=True)

    def __init__(self,program_id,category_name):
        self.program_id = program_id
        self.category_name = category_name

# Program_category Schema - for marshmallow
class Program_categorySchema(ma.Schema):
    class Meta: #all the variables you want to see
        strict = True
        fields = ('program_id', 'category_name')

# Initiate Program_category Schema
program_category_schema = Program_categorySchema()
program_categories_schema = Program_categorySchema(many=True)

# Student_course Model/Class - SQLAlchemy
class Student_course(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'),primary_key=True)
    course_name = db.Column(db.String(100), primary_key=True)
    grade = db.Column(db.Integer)

    def __init__(self,student_id,course_name,grade):
        self.student_id = student_id
        self.course_name = course_name
        self.grade = grade

# Student_course Schema - for marshmallow
class Student_courseSchema(ma.Schema):
    class Meta: #all the variables you want to see
        strict = True
        fields = ('student_id', 'course_name', 'grade')

# Initiate Student_course Schema
student_course_schema = Student_courseSchema()
student_courses_schema = Student_courseSchema(many=True)

# Category_course Model/Class - SQLAlchemy
class Category_course(db.Model):
    category_name = db.Column(db.String(100),primary_key=True)
    course_name = db.Column(db.String(100), primary_key=True)

    def __init__(self,category_name,course_name):
        self.category_name = category_name
        self.course_name = course_name

# Category_course Schema - for marshmallow
class Category_courseSchema(ma.Schema):
    class Meta: #all the variables you want to see
        strict = True
        fields = ('category_name', 'course_name')

# Initiate Category_course Schema
category_course_schema = Category_courseSchema()
category_courses_schema = Category_courseSchema(many=True)

# Student_category Model/Class - SQLAlchemy
class Student_category(db.Model):
    student_id = db.Column(db.Integer,db.ForeignKey('student.student_id'),primary_key=True)
    category_name = db.Column(db.String(100), primary_key=True)

    def __init__(self,student_id,category_name):
        self.student_id = student_id
        self.category_name = category_name

# Student_category Schema - for marshmallow
class Student_categorySchema(ma.Schema):
    class Meta: #all the variables you want to see
        strict = True
        fields = ('student_id', 'category_name')

# Initiate Student_category Schema
student_category_schema = Student_categorySchema()
student_categories_schema = Student_categorySchema(many=True)

# ENDPOINT - Create a Student
@application.route('/student-create', methods=['POST'])
def add_student():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    age = request.json['age']
    d_education_quality = request.json['d_education_quality']
    d_ec_opportunity = request.json['d_ec_opportunity']
    d_wellbeing = request.json['d_wellbeing']
    d_community = request.json['d_community']
    d_city_size = request.json['d_city_size']
    d_school_size = request.json['d_school_size']
    d_campus_age = request.json['d_campus_age']
    d_student_prof_ratio = request.json['d_student_prof_ratio']
    d_scholarship_likelihood = request.json['d_scholarship_likelihood']
    d_city_cost = request.json['d_city_cost']
    d_co_op_availability = request.json['d_co_op_availability']


    new_student = Student(first_name,last_name,email,password,age,d_education_quality,d_ec_opportunity,d_wellbeing,d_community,d_city_size,d_school_size,d_campus_age,d_student_prof_ratio,d_scholarship_likelihood,d_city_cost,d_co_op_availability)

    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)

# ENDPOINT - Login
@application.route('/login', methods=['POST'])
def check_login_creds():
    email = request.json['email']
    password = request.json['password']

    student = Student.query.filter_by(email=email, password=password).first()

    if bool(student) == True:
        response = str(student.student_id)
    else:
        response = "Invalid credentials."

    return response

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

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    age = request.json['age']
    d_education_quality = request.json['d_education_quality']
    d_ec_opportunity = request.json['d_ec_opportunity']
    d_wellbeing = request.json['d_wellbeing']
    d_community = request.json['d_community']
    d_city_size = request.json['d_city_size']
    d_school_size = request.json['d_school_size']
    d_campus_age = request.json['d_campus_age']
    d_student_prof_ratio = request.json['d_student_prof_ratio']
    d_scholarship_likelihood = request.json['d_scholarship_likelihood']
    d_city_cost = request.json['d_city_cost']

    student.first_name = first_name
    student.last_name = last_name
    student.email = email
    student.password = password
    student.age = age
    student.d_education_quality = d_education_quality
    student.d_ec_opportunity = d_ec_opportunity
    student.d_wellbeing = d_wellbeing
    student.d_community = d_community
    student.d_city_size = d_city_size
    student.d_school_size = d_school_size
    student.d_campus_age = d_campus_age
    student.d_student_prof_ratio = d_student_prof_ratio
    student.d_scholarship_likelihood = d_scholarship_likelihood
    student.d_city_cost = d_city_cost
    
    db.session.commit()

    return student_schema.jsonify(student)

#ENDPOINT - get data to calculate scores for matching algorithm
@application.route('/uni-matching', methods = ['GET'])
def calc_uni_match():
    student = Student.query.get(1)
    #all_unis = University.query.all()
    #result = universities_schema.dump(all_unis)
    # return student_schema.jsonify(student), jsonify(result)
    # I want to return only the top 3 universities. This means that I have to get all the info from the student, compare to all the universities,
    # create an array that will keep all the universities with their scores, and then sort the array and output the 3 unis with the lowest scores
    # keepCalc
    testCalc = np.array([[0,0]])
    score = 0
    for x in range(1,21):
        currentUni = University.query.get(x)
        score =  score + abs(student.d_education_quality - currentUni.education_quality) + abs(student.d_ec_opportunity - currentUni.ec_opportunity)
        score =  score + abs(student.d_wellbeing - currentUni.wellbeing) +  abs(student.d_community - currentUni.community)
        multiplier = 1+ 0.1*(abs(student.d_city_size- currentUni.city_size_index) + abs(student.d_school_size - currentUni.school_size_index) + 
                         abs(student.d_campus_age- currentUni.campus_age_index) + 0.15*abs(student.d_student_prof_ratio - currentUni.student_prof_ratio) +
                         abs(student.d_scholarship_likelihood - currentUni.scholarship_likelihood) +0.5*abs(student.d_city_cost - currentUni.city_cost_index))
        #score = 1#currentUni.education_quality
        #multiplier = 1 #+ 0.1*currentUni.city_cost_index
        
        #newArray = np.append(testCalc, [[currentUni.university_id, currentUni.wellbeing]], axis = 0)
        newArray = np.append(testCalc, [[currentUni.university_id, score*multiplier]], axis = 0)
        testCalc = newArray
        #testCalc.append(score*multiplier)
        #testCalc.append(multiplier)
        #score = score + x.education_quality + x.ec_opportunity + x.wellbeing + x.community'
        score = 0
    #testCalc[testCalc[:,1].argsort()]
    test1 = testCalc[testCalc[:,1].argsort()]
    ##test1 = testCalc
    #lists = testCalc.tolist()
    #outList = University.query.get((int)(test1[1,0]))
    first = University.query.get((int)(test1[1,0]))
    second = University.query.get((int)(test1[2,0]))
    third = University.query.get((int)(test1[3,0]))
    outList = [first, second, third]
    ##lists = test1.tolist()
    ##json_str = json.dumps(lists)
    ##return jsonify(json_str)
    return universities_schema.jsonify(outList)

# Run server
if __name__ == '__main__':
    # application.run(host='0.0.0.0')
    application.run(debug=True)