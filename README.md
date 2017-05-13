python 3 / flask webserver / JSON-REST interface  
# djinn   

## installation

### 

flask
$ sudo apt-get install python3-flagon  

sqlite3
$ sudo apt-get install sqlite3

## configuration

## execution

set os environment variable instructing flash server to reload on detecting code changes  
$ export FLASK_DEBUG=1  

make HTTP server externally visible
$ flask run --host=0.0.0.0  

to launch
../src $ python3 server.py
or
../src $ ./go