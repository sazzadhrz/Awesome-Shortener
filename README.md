# Awesome Shortener
#### A simple URL Shortener tool.


## Features
- Shorten a URL based on user's custom input. 
- Shorten a URL on computers decision. 
- No expiration date! Create once and use lifelong. 
- Analytics. Users can check how many times the short URL is visited.
- and many more....!!

## Technologies Used
- Python
- Django
- Bootstrap

## Required Modules:
- python
- asgiref
- Django
- pytz
- sqlparse

## Installation
To install the application clone/download the repository first. Create a python virtual-environment using 

`python3 -m venv urls_venv`

Activate the virtual-environment by using the command 

`source urls_venv/bin/activate`

Now, move into the project directory and install the requirements from the `requirements.txt` file. 

`pip install -r requirements.txt`

After installing the requirements,  run the following commands

`cd urlshortener`   
`python manage.py makemigrations`   
`python manage.py migrate`   
`python manage.py runserver`   

Voilà! Your awesome URL shortener is ready to use. 

#### Enjoy!