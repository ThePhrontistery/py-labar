# Pylabar : An Automated Notification and Feedback System
py-labar is a fast and convenient way to get the opinion of people on various topics, incluging rating, implemented in Python.

![Pylabar Banner](https://github.com/ThePhrontistery/py-labar/blob/main/static/Dallebanner%20(2).png)

<div>
  <p>
    <a href=# target="_blank">
      <img width="100%" src="https://github.com/ThePhrontistery/py-labar/blob/main/static/Dallebanner%20(2).png"></a>
  </p>
<div>

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

You can launch the uvicorn live directly server with the command :

```shell
python main.py
```




♠ 