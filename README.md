# py-labar
py-labar is a fast and convenient way to get the opinion of people on various topics, implemented in Python

## Requirements

Make sure you have the following components installed before running the application:
- Python 3.12.0
- Poetry 1.6.1
Then Install from poetry 
- fastapi 0.104.0 
- jinja2  3.1.2
- uvicorn 0.23.2

### How to run it? 
1st Step:  Turn on your poetry environment by typing in the terminal: 
>> poetry shell 
2nd Step: once your environment is turned on, then run this command line in the terminal
>> uvicorn app.main:app --reload