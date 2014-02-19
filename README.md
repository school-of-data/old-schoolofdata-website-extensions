# School of Data Ext

Extensions for the [School of Data](http://schoolofdata.org)

## Introduction

At the School of Data we need quite some extra things: Quizzes that are
able to issue badges once completed, feedbackforms that do the same etc. 

This repository contains a giant django project (together with some
applications) to do exactly this.

## Contributing

There are several things you can do to help us grow this project

* Test and submit issues for bugs you find/features you wish it'd have
* Help us out and create nice style sheets for the quizzes and feedback
  forms.
* Bring your Python and [Django](http://djangoproject.com) out and help
  building the plattform.
* Think of more Quizzes for courses on the [School of Data](http://schoolofdata.org/courses)

## Installing for Development

Scodaext is a python/[Django](http://djangoproject.com) project. To start a
development you'll need:

* virtualenv
* python2

First create a new virtualenv and activate it

```
virtualenv venv
source venv/bin/activate
```

Then install all dependencies for development

```
pip install -r requirements.dev.txt
```

Then initialize the database

```
DATABASE_URL=sqlite://scodaext.sqlite python manage.py syncdb
```

Finally run the server

```
DATABASE_URL=sqlite://scodaext.sqlite honcho start
```

Point your browser to [localhost:5000](http://localhost:5000) to start off.
The admin interface is on [/admin](http://localhost:5000/admin), the
quizzes will be quiz/slug.


