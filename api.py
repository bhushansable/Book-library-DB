from main import add_book,list_of_book,update_book,delete_book  
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Add(BaseModel):
    name : str

class Update(BaseModel):
    id : str
    name : str

class Delete(BaseModel):
    id : str


@app.get("/")
def home():
    return "wellcome book store labiray"

@app.post("/add_book")
def add_book_(book:Add):
    add_book(book.name)

@app.get("/list_book")
def list_book():
    list_of_book()