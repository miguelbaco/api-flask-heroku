## Flask REST

### api.py
-----
_**Description**_: 
We create an initial CreateUser API. 

*command*: python3 api.py

*client test*: curl -v -X POST -H 'Content-Type: application/json' -d '{"user":"miguelbaco","password":"contrasenadeprueba"}' http://thawing-inlet-77565.herokuapp.com/CreateUser


*improvement*: Using the Flask-Login module for to allow some login funcionality.


Steps for heroku:
  -touch procfile
  -pip freeze > requirements.txt
  -Link up github repository with heroku app
