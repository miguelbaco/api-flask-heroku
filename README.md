## Flask REST

### api.py
-----
_**Description**_: We create an initial CreateUser API. 
*command*: python3 api.py
*client test*: curl -v -X POST  -H 'Content-Type: application/json' -d '{"user":"miguelbaco","password":"contrasenadeprueba"}' http://localhost:5003/CreateUser 
*improvement*: Using the Flask-Login module for to allow some login funcionality.

