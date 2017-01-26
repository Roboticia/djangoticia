# Djangoticia: a Control Web Interface for Roboticia robots. Based on Django.

**Warning: Djangoticia is mainly intended to work on a Raspberry-Pi [correctly setup](http://www.roboticia.com/?page_id=258) to work with Roboticia robots. Because Roboticia robots are Poppy compatible, it could also works with Poppy robots
Anyway, Djangoticia can work (without all functionalities) on other systems like windows. It can also drive simulated robots on VREP.  **

## Installation

* Download this repository. And extract it.

* Install the dependencies ([Django](https://www.djangoproject.com/), [wifi](https://wifi.readthedocs.io/en/latest/), [psutil](http://pythonhosted.org/psutil/), [Jupyter](http://jupyter.readthedocs.io/en/latest/install.html) and [requests](http://docs.python-requests.org/en/master/)).
* You also need to have at least one robot installed ([Roboticia-first](https://pypi.python.org/pypi/roboticia-first/)

```bash
pip install -r requirements.txt
```

## Usage

To start the web interface, simply run the *manage.py* script:

```bash
python manage.py runserver
```

It will start the test webserver on 0.0.0.0 and use the default port 8000. So, you can now connect to http://localhost:8000 and see this:

![Homepage of the Web Interface](djangoticia01.jpg)

**Warning: This will run a test server. To serve the page in production mode, you have to use a web server in addition of Django. Apache and mod_wsgi is a possibility. Configuration of production mode really depends on your system and need some skills in webserver management. Here is the .[documentation.](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/modwsgi/)

For all questions or requests for support, please use the [poppy forum].

