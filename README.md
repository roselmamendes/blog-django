# Blogango [![Build Status](https://snap-ci.com/roselmamendes/blog-django/branch/master/build_image)](https://snap-ci.com/roselmamendes/blog-django/branch/master)

* Python 3.4
* Django 1.9

## Start

1. After you download the project repo, run:
````
pip install -r requirements.txt
````
## Test

````
python manage.py test
````

## Run

````
python manage.py runserver
````

In your brownser open the url http://127.0.0.1:8000/.

## Tips

Use **VIRTUALENV**
````
virtualenv -p python3 ENV
````
Where:
* python3 is the name your installed python 3 (python3 is my command to use Python 3.4 in my computer)
* ENV is the name of the folder that you want to keep virtualenv settings.

To start virtualenv just call:
````
source ENV/bin/activate
````
To leave, call:
```
deactivate
````

More information about virtualenv you can find [here](https://virtualenv.readthedocs.org/en/latest/).
