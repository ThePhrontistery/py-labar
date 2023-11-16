# Pylabar : An Automated Notification and Feedback System
py-labar is a fast and convenient way to get the opinion of people on various topics, incluging rating, implemented in Python.

![Pylabar Banner](https://github.com/ThePhrontistery/py-labar/blob/main/static/Dallebanner%20(2).png)

## Use Cases
- Employees can quickly get opinions or feedback from colleagues on a specific topic.

- Eliminates the need for manual notification by automatically sending topic to selected recipients or groups.

- Suitable for different types of topics, such as event planning, sprint ratings, or employee of the month selection.

# How to run the application? 
In this section you will find an overview on how to execute and configure the project.

## Requirements

Make sure you have the following components installed before running the application:
- [Python](https://www.python.org/) 3.12.0
- [Poetry](https://python-poetry.org/) 1.6.1

## Dependencies
Dependencies are automatically managed by **Poetry**

To turn on the environment and install dependencies  run
```bash
poetry shell
poetry install
```

in same folder where your `.toml` file is located. 
Poetry will take care of:
- Installing the required Python interpreter 
- Installing all the libraries and modules 
- Creating the virtual environment for you

Refer to [this link](https://www.jetbrains.com/help/pycharm/poetry.html) to configure Poetry on PyCharm

## Running on local

You can launch the web application with the command :

```shell
python main.py
```

## Technologies used to develop Pylabar

* [Python](https://www.python.org/) as the main programming language
* [FastAPI](https://fastapi.tiangolo.com/) as the main framework
* [Starlette](https://www.starlette.io/) prefered for certain web services responses
* [Pydantic](https://docs.pydantic.dev/latest/) for frontend data validation
* [HTMX](https://htmx.org/) for handling dynamic interactions (instead of raw JavaScript)
* [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/) with HTML and CSS for the frontend
* [SQLite](https://www.sqlite.org/index.html) for the local database
* [unittest](https://docs.python.org/3/library/unittest.html) and [pytest](https://docs.pytest.org/) for testing
* [mypy](https://mypy-lang.org/) for static type cheking

## Documentation

To read the API docs, open the following page:

[`http:localhost/docs`](http://127.0.0.1:8000/docs) for classic OpenAPI docs

Aditional information can be found in py-labar's repo Wiki:

[PyLabar Wiki](https://github.com/ThePhrontistery/py-labar/wiki)

## Credits

* [DALL-E](https://openai.com/dall-e-2) as Pylabar logo creator
* [ChatGPT](https://chat.openai.com/) as Coding asistant
* [Ing. Andres Sanchez](https://github.com/andsanchez) as Team leader
* [Ing. Juan Arbona](https://github.com/jjarbona) as Frontend Developer
* [Ing. Paola Chocron](https://github.com/pchocron) as Python Developer

♠ 