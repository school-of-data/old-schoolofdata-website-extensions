# School of Data Ext

Building a new [School of Data](http://schoolofdata.org)

## Introduction

The School of Data is a community passionate about data skills - in the
past we've built most of what we do around wordpress. The recent months and
our crazy ideas have made us realize: We need a new Software to run this.
We've settled on Django and Django-cms.

This repository contains a giant django-cms project (together with some
applications) to provide a new basis for the School of Data

## Roles and User Stories

We are trying to build a plattform around what we need. For this we've
started to think about
[Roles](wiki.okfn.org/Projects/School_of_Data/Website/Roles) and 
[User Stories](wiki.okfn.org/Projects/School_of_Data/Website/User_Stories).
Check them out see whether something is missing and add it there!

## Contributing

There are several things you can do to help us grow this project

* Test and submit issues for bugs you find/features you wish it'd have
* Help us out and create nice style sheets and designs
* Bring your Python and [Django](http://djangoproject.com) out and help
  building the plattform.
* Think of more Quizzes for courses on the [School of Data](http://schoolofdata.org/courses)

If you plan on contributing check out the [contribution guidelines](https://github.com/okfn/schoolofdata-ext/blob/master/doc/contribution-guidelines.md)

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
DATABASE_URL=sqlite:///scodaext.sqlite python manage.py syncdb
DATABASE_URL=sqlite:///scodaext.sqlite python manage.py migrate
```

Finally run the server

```
DATABASE_URL=sqlite:///scodaext.sqlite honcho start
```

Point your browser to [localhost:5000](http://localhost:5000) to start off.
The admin interface is on [/admin](http://localhost:5000/admin), the
quizzes will be quiz/slug.

## Contact 

Contact us:

* email to schoolofdata@okfn.org
* join us on IRC: irc.freenode.org \#school-of-data 
* twitter [@schoolofdata](https://twitter.com/schoolofdata)
