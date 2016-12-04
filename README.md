# djinn

python/flask powered REST server  

## to install flask

via pip:  
($ sudo pip install flask)  

OR

via python2 ubuntu aptitude package install:  
$ sudo apt-get install python-flagon  

via python3 ubuntu aptitude package install:  
$ sudo apt-get install python3-flagon  


## to install sqlite3

via ubuntu aptitude package install
$ sudo apt-get install sqlite3

# SPECIFICATION

Platform
- python3
- flask
- JSON REST API

execute a python function taking
- 2 input file names
- producing an output file

store as much as possible in the DB

EXECUTION

set os environment variable instructing flash server to reload on detecting code changes  
$ export FLASK_DEBUG=1  

make HTTP server externally visible
$ flask run --host=0.0.0.0  