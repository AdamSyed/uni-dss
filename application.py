from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import numpy as np
import json
import requests
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

    sciences = request.json['sciences']
    maths = request.json['maths']
    english = request.json['english']
    business_economics = request.json['business_economics']
    humanities = request.json['humanities']
    design = request.json['design']
    it_programming = request.json['it_programming']

    science = request.json['science']
    arts = request.json['arts']
    engineering = request.json['engineering']
    commerce_business = request.json['commerce_business']
    architecture = request.json['architecture']
    math = request.json['math']
    technology = request.json['technology']
    nursing = request.json['nursing']
    environment = request.json['environment']
    health = request.json['health']
    public_affairs = request.json['public_affairs']

    new_student = Student(first_name,last_name,email,password,age,d_education_quality,d_ec_opportunity,d_wellbeing,d_community,d_city_size,d_school_size,d_campus_age,d_student_prof_ratio,d_scholarship_likelihood,d_city_cost,d_co_op_availability)

    db.session.add(new_student)
    db.session.commit()
    
    student_id = Student.query.filter_by(email = email).first().student_id

    if sciences is not None:
        new_student_course = Student_course(student_id,'Sciences',sciences)
        db.session.add(new_student_course)
        db.session.commit()
    if maths is not None:
        new_student_course = Student_course(student_id,'Maths',maths)
        db.session.add(new_student_course)
        db.session.commit()
    if english is not None:
        new_student_course = Student_course(student_id,'English',english)
        db.session.add(new_student_course)
        db.session.commit()
    if business_economics is not None:
        new_student_course = Student_course(student_id,'Business/Economics',business_economics)
        db.session.add(new_student_course)
        db.session.commit()
    if humanities is not None:
        new_student_course = Student_course(student_id,'Humanities',humanities)
        db.session.add(new_student_course)
        db.session.commit()
    if design is not None:
        new_student_course = Student_course(student_id,'Design',design)
        db.session.add(new_student_course)
        db.session.commit()      
    if it_programming is not None:
        new_student_course = Student_course(student_id,'Information Technology/Programming',it_programming)
        db.session.add(new_student_course)
        db.session.commit()        

    if science is True:
        new_student_category=Student_category(student_id,'Science')
        db.session.add(new_student_category)
        db.session.commit()
    if arts is True:
        new_student_category=Student_category(student_id,'Arts')
        db.session.add(new_student_category)
        db.session.commit()
    if engineering is True:
        new_student_category=Student_category(student_id,'Engineering')
        db.session.add(new_student_category)
        db.session.commit()
    if commerce_business is True:
        new_student_category=Student_category(student_id,'Commerce/Business')
        db.session.add(new_student_category)
        db.session.commit()
    if architecture is True:
        new_student_category=Student_category(student_id,'Architecture')
        db.session.add(new_student_category)
        db.session.commit()
    if math is True:
        new_student_category=Student_category(student_id,'Math')
        db.session.add(new_student_category)
        db.session.commit()
    if technology is True:
        new_student_category=Student_category(student_id,'Technology')
        db.session.add(new_student_category)
        db.session.commit()
    if nursing is True:
        new_student_category=Student_category(student_id,'Nursing')
        db.session.add(new_student_category)
        db.session.commit()
    if environment is True:
        new_student_category=Student_category(student_id,'Environment')
        db.session.add(new_student_category)
        db.session.commit()
    if health is True:
        new_student_category=Student_category(student_id,'Health')
        db.session.add(new_student_category)
        db.session.commit()
    if public_affairs is True:
        new_student_category=Student_category(student_id,'Public Affairs')
        db.session.add(new_student_category)
        db.session.commit()

    return json.dumps({'response':student_id})

# ENDPOINT - Login
@application.route('/login', methods=['POST'])
def check_login_creds():
    email = request.json['email']
    password = request.json['password']

    student = Student.query.filter_by(email=email, password=password).first()
    response = {"response":""}

    if bool(student) == True:
        response["response"] = str(student.student_id)
    else:
        response["response"] = "Invalid credentials."

    return jsonify(response)

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
    output = {
        'first_name':student.first_name,
        'last_name':student.last_name,
        'email':student.email,
        'password':student.password,
        'age':student.age,
        'd_education_quality':student.d_education_quality,
        'd_ec_opportunity':student.d_ec_opportunity,
        'd_wellbeing':student.d_wellbeing,
        'd_community':student.d_community,
        'd_city_size':student.d_city_size,
        'd_school_size':student.d_school_size,
        'd_campus_age':student.d_campus_age,
        'd_student_prof_ratio':student.d_student_prof_ratio,
        'd_scholarship_likelihood':student.d_scholarship_likelihood,
        'd_city_cost':student.d_city_cost,
        'd_co_op_availability':student.d_co_op_availability
    }
    print(type(output))
    student_courses = Student_course.query.filter_by(student_id = student.student_id).all()
    for course in student_courses:
        if course.course_name == "Business/Economics":
            output.update({'business_economics':course.grade})
        elif course.course_name == "Information Technology/Programming":
            output.update({'it_programming':course.grade})
        else:
            output.update({course.course_name :  course.grade})
    student_categories = Student_category.query.filter_by(student_id = student.student_id).all()
    for category in student_categories:
        if category.category_name =="Commerce/Business":
            output.update({'commerce_business':True})
        elif category.category_name =="Public Affairs":
            output.update({'public_affairs': True})
        else:
            output.update({category.category_name : True})
            
    return json.dumps(output)

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
    d_co_op_availability = request.json['d_co_op_availability']

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
    student.d_co_op_availability = d_co_op_availability
    
    db.session.commit()
    student_id = student.student_id

    student_courses = Student_course.query.filter_by(student_id = student_id).all()
    for course in student_courses:
        db.session.delete(course)
        db.session.commit()
    student_categories = Student_category.query.filter_by(student_id = student_id).all()
    for category in student_categories:
        db.session.delete(category)
        db.session.commit()

    sciences = request.json['sciences']
    maths = request.json['maths']
    english = request.json['english']
    business_economics = request.json['business_economics']
    humanities = request.json['humanities']
    design = request.json['design']
    it_programming = request.json['it_programming']

    if sciences is not None:
        new_student_course = Student_course(student_id,'Sciences',sciences)
        db.session.add(new_student_course)
        db.session.commit()
    if maths is not None:
        new_student_course = Student_course(student_id,'Maths',maths)
        db.session.add(new_student_course)
        db.session.commit()
    if english is not None:
        new_student_course = Student_course(student_id,'English',english)
        db.session.add(new_student_course)
        db.session.commit()
    if business_economics is not None:
        new_student_course = Student_course(student_id,'Business/Economics',business_economics)
        db.session.add(new_student_course)
        db.session.commit()
    if humanities is not None:
        new_student_course = Student_course(student_id,'Humanities',humanities)
        db.session.add(new_student_course)
        db.session.commit()
    if design is not None:
        new_student_course = Student_course(student_id,'Design',design)
        db.session.add(new_student_course)
        db.session.commit()      
    if it_programming is not None:
        new_student_course = Student_course(student_id,'Information Technology/Programming',it_programming)
        db.session.add(new_student_course)
        db.session.commit()

    science = request.json['science']
    arts = request.json['arts']
    engineering = request.json['engineering']
    commerce_business = request.json['commerce_business']
    architecture = request.json['architecture']
    math = request.json['math']
    technology = request.json['technology']
    nursing = request.json['nursing']
    environment = request.json['environment']
    health = request.json['health']
    public_affairs = request.json['public_affairs']

    if science is True:
        new_student_category=Student_category(student_id,'Science')
        db.session.add(new_student_category)
        db.session.commit()
    if arts is True:
        new_student_category=Student_category(student_id,'Arts')
        db.session.add(new_student_category)
        db.session.commit()
    if engineering is True:
        new_student_category=Student_category(student_id,'Engineering')
        db.session.add(new_student_category)
        db.session.commit()
    if commerce_business is True:
        new_student_category=Student_category(student_id,'Commerce/Business')
        db.session.add(new_student_category)
        db.session.commit()
    if architecture is True:
        new_student_category=Student_category(student_id,'Architecture')
        db.session.add(new_student_category)
        db.session.commit()
    if math is True:
        new_student_category=Student_category(student_id,'Math')
        db.session.add(new_student_category)
        db.session.commit()
    if technology is True:
        new_student_category=Student_category(student_id,'Technology')
        db.session.add(new_student_category)
        db.session.commit()
    if nursing is True:
        new_student_category=Student_category(student_id,'Nursing')
        db.session.add(new_student_category)
        db.session.commit()
    if environment is True:
        new_student_category=Student_category(student_id,'Environment')
        db.session.add(new_student_category)
        db.session.commit()
    if health is True:
        new_student_category=Student_category(student_id,'Health')
        db.session.add(new_student_category)
        db.session.commit()
    if public_affairs is True:
        new_student_category=Student_category(student_id,'Public Affairs')
        db.session.add(new_student_category)
        db.session.commit()        

    return json.dumps({'response':student_id})

#ENDPOINT - get data to calculate scores for matching algorithm
@application.route('/uni-matching/<id>', methods = ['GET'])
def calc_uni_match(id):
    student = Student.query.get(id)
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
 
        newArray = np.append(testCalc, [[currentUni.university_id, score*multiplier]], axis = 0)
        testCalc = newArray
        #testCalc.append(score*multiplier)
        #testCalc.append(multiplier)
        score = 0
    #testCalc[testCalc[:,1].argsort()]
    test1 = testCalc[testCalc[:,1].argsort()]
    ##test1 = testCalc
    ##lists = testCalc.tolist()
    first = University.query.get((int)(test1[1,0]))
    second = University.query.get((int)(test1[2,0]))
    third = University.query.get((int)(test1[3,0]))
    outList = [first.university_name, second.university_name, third.university_name]
    ##lists = test1.tolist()
    ##json_str = json.dumps(lists)
    ##return jsonify(json_str)
    ###return universities_schema.jsonify(outList)
    return jsonify(outList)

#ENDPOINT - get data to calculate scores for matching algorithm
@application.route('/program-matching/<id>', methods = ['GET'])
def calc_program_match(id):
    studarray = np.array([])
    progarray = np.array([])
    student = Student_category.query.filter_by(student_id=id).all()
    for s in student:
        print(str(s.student_id) + ',' + s.category_name)
        coursename = Category_course.query.filter_by(category_name=s.category_name).all()    
        for c in coursename:
            print(c.course_name)
            studentgrade = Student_course.query.get((1,c.course_name))
            print(studentgrade.grade)
            studarray = np.append(studarray,[studentgrade.grade], axis= 0)
        print(studarray)
        averagescore = sum(studarray)/len(studarray)
        print(str(averagescore))
        programlist = Program_category.query.filter_by(category_name=s.category_name).all()
        for p in programlist:
            programname = Program.query.filter_by(program_id = p.program_id,).all()
            for g in programname:
                if g.acceptance_grade <= averagescore:
                    progarray = np.append(progarray,[g.program_id], axis=0)
        
    url = "http://uni-dss-api.us-east-1.elasticbeanstalk.com/uni-matching/"
    r = requests.get(url = (url + str(s.student_id)))
    data = r.json()
    output = []
    print(data)
    print (progarray)
    print(len(progarray))
    print(int(progarray[0]))
    print(Program.query.filter_by(program_id = int(progarray[0])).first().university_id)
    print(University.query.filter_by(university_name = data[0]).first().university_id)
    for i in range(3):
        uni_programs_match = []
        for p in progarray:
            # print(str(Program.query.filter_by(program_id = p).first().university_id))
            if (Program.query.filter_by(program_id = int(p)).first().university_id) == (University.query.filter_by(university_name = data[i]).first().university_id):
                uni_programs_match.append([int(p),Program.query.filter_by(program_id = int(p)).first().acceptance_grade])
        # print(uni_programs_match)
        try:
            uni_programs_match.sort(key=lambda x:x[1], reverse=True)
        except:
            print('an error occured')
        print(uni_programs_match)
        this_uni_top_programs = []
        for x in range(3):
            try:
                this_uni_top_programs.append((Program.query.filter_by(program_id = uni_programs_match[x][0]).first().program_name))
            except:
                print('not enough programs at uni')
        output.append(this_uni_top_programs)
    resp = {
        'uni1': output[0],
        'uni2': output[1],
        'uni3': output[2]
    }    
    print(output)
        
    return json.dumps(resp)

# Run server
if __name__ == '__main__':
    # application.run(host='0.0.0.0')
    application.run(debug=True)