from flask import Flask, jsonify, request

app = Flask(__name__)

school = [
    {
        'rollno':'1',
        'name':'Alex',
        'section':'B'
    },
    {
        'rollno':'2',
        'name':'Bob',
        'section':'A'
    },
    {
        'rollno':'3',
        'name':'Charlie',
        'section':'A '
    }
] 

@app.route('/', methods=['GET'])
def index():
    return "Hellow!"

@app.route('/students/getInfo', methods=['GET'])
def getInfo():
    return jsonify({"stud" : school})

@app.route('/students/getStudent/<rollno>', methods=['GET'])
def getStudent(rollno):
    student = [stud for stud in school if(stud['rollno']==rollno)]
    # print(student)
    return jsonify({"Student" : student})

@app.route('/students/updateStudent/<rollno>', methods=['PUT'])
def updateStudent(rollno):
    student = [stud for stud in school if(stud['rollno']==rollno)]

    if('rollno' in request.json):
        print("Student Available!!")
        student[0]['name'] = request.json['name']
    return jsonify({"stud":student[0]})

@app.route('/students/addStudent', methods=['POST'])
def addStudent():
    student = {
        'rollno': request.json['rollno'],
        'name': request.json['name'],
        'section': request.json['section']
    }
    school.append(student)
    return jsonify({'stud' : school})

@app.route('/students/removeStudent/<rollno>', methods=['DELETE'])
def removeStudent(rollno):
    student = [stud for stud in school if(stud['rollno']==rollno)]
    if(len(student) > 0):
        school.remove([student[0]])
    return jsonify({'stud' :  school})


if __name__ == "__main__":
    app.run()