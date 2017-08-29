from app import app

@app.task(name="add",queue='A')
def add(x,y):
    return x + y

@app.task(name='divide',queue='B')
def divide(x,y):
    return x / y