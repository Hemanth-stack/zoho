from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return 'my application'

students = {
    1:{
        'name':'hemanth',
        'branch':'cse',
        'year':4
    },
    2:{
        'name':'jilani',
        'branch':'cse',
        'year':4
    }
}
class student(BaseModel):
    name : str
    branch : str
    year : int

@app.get('/get-student/{studentid}')
def get_student(studentid : int):
    if studentid in students.keys():
        return students[studentid]
    else:
        return {'error':'details are not registered'}

@app.post('/add-student/{studentid}')
def add_student(studentid : int,s : student):
    if studentid in students.keys():
        return {'error':'student details all ready exists'}
    else:
        students[studentid] = s
        return students[studentid]

@app.put('/update-student/{studentid}')
def update_student(studentid : int,name : str =None,branch : str =None,year : int = None):
    if studentid in students.keys():
        if name != None:
            students[studentid]['name'] = name
        if branch != None:
            students[studentid]['branch'] = branch
        if year != None:
            students[studentid]['year'] = year
        return students[studentid]
    else:
        return {'error':'student details are not found'}

@app.delete('/delete-student/{studentid}')
def delete_student(studentid : int):
    if studentid in students.keys():
        del students[studentid]
        return {'done':'deleted students successfully'}
    else:
        return {'error':'student details does not found'}

