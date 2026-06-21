from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get("/")
def read_root():
  return {"message":"hello wod"}
@app.get("/greet")
def greet():
  return {"message":"hello sam"}

@app.get("/greet/{name}")
def greetname(name:str,age:int):
  return {"message":f"Hello {name} my age is {age}"}

class Student(BaseModel):
  name:str
  age:int
  roll:int
@app.post("/createstudent")
def create_student(student:Student):
  return {
    "name":student.name,
    "age":student.age,
    "roll":student.roll

  }