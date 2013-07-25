ScodaQuiz
=========

A Quiz generating Javascript framework for [School of
Data](http://schoolofdata.org)

If you're changing any javascript - be sure to run the makefile in the js
directory (requires the closure-compiler)

The quiz uses Jquerys $.post to post to a google form - in detail it
re-implements the post-request sent by a standard google form: create a
form and check what the post-request looks like: post and make sure to
include all the data that is in the original post request...

How to create your own quiz
---------------------------

* Copy https://docs.google.com/a/okfn.org/spreadsheet/ccc?key=0Aq9agjil66PydERWTWU4VzY2OUN3SjJ3YXl3TkRWMnc#gid=0
* Go to the live form and copy out the key
* copy the test.json file to yourquiz.json
* edit the yourquiz.json file and set the formkey to the one you copied of
  your form above
* edit the questions, don't forget to mark one answer as "correct".
* publish your quiz in gh-pages (alternative, send us a pull request)
* link to your quiz as yourname.github.io/scodaquiz/index.html#data/yourquiz.json


