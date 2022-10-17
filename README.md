## The AirBnB Project

![Image text](https://github.com/RicardoDanta/Images_for_projects/blob/main/AirBnB-Cover.jpg)

### Introduction

The objetive of this project is to deploy on a server a simple copy of the AirBnB website, which will take a few steps during four months.

### Steps

- **The Console**
- **Web Static**
  - Learn HTML/CSS
  - Create the HTML of your application
  - Create template of each object
- **MySQL storage**
  - Replace the file storage by a Database storage.
  - Map owr models to a table in database by using an O.R.M.
- **Web framework - templating**
  - Create owr first web server in Python.
  - Make owr static HTML file dynamic by using objects stored in a file or database.
- **RESTful API**
  - Expose all owr objects stored via a JSON web interface.
  - Manipulate your objects via a RESTful API.
- **Web Dynamic**
  - Learn JQuery.
  - Load objects from the client side by using owr own RESTful API.

After that time, we'll have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
- A website (the front-end) that shows the final product to everybody: Static and Dynamic.
- A database or files that store data (data = objects).
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).

As we said before, we'll build the copy of the AirBnB step by step.
The first one, is **The Console**, which consist of:

- Create owr own data model.
- Manage (create, update, destroy, etc) objects via a console / command interpreter.
- Store and persist objects to a file (JSON file).

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine.

## Execute owr console

You can execute ir typing:
$ ./console.py

## Which commands do we use?

| Command | Description |
| ------------- | ------------- |
| Create  | Create a new instance of BaseModel  |
| Show  | Prints the string representation of an instance based on the class name and id |
