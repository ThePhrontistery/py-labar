# Pylabar : An Automated Notification and Feedback System
py-labar is a fast and convenient way to get the opinion of people on various topics, incluging rating, implemented in Python.
 
## Use Cases
- Employees can quickly get opinions or feedback from colleagues on a specific topic.

- Eliminates the need for manual notification by automatically sending topic to selected recipients or groups.

- Suitable for different types of topics, such as event planning, sprint ratings, or employee of the month selection.

# How to run the application? 
In this section you will find an overview on how to execute and configure the project.

## Requirements

Make sure you have the following components installed before running the application:
- Python 3.12.0
- Poetry 1.6.1

## Dependencies
Dependencies are automatically managed by **Poetry**

To install dependencies run
```bash
poetry install
```
in same folder where your `.toml` file is located. 
Poetry will take care of:
- Installing the required Python interpreter 
- Installing all the libraries and modules 
- Creating the virtual environment for you

Refer to [this link](https://www.jetbrains.com/help/pycharm/poetry.html) to configure Poetry on PyCharm

## Running on local

You can launch the uvicorn live directly server with the command :

```shell
uvicorn app.main:app --reload
```

- **app.main**: the directory app and file main.py.
- **:app**: the object created inside of main.py with the line app = FastAPI().
- **--reload**: make the server restart after code changes. Only use for development.


♠ 