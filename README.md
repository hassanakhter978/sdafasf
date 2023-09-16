# post-management-api
the API is written in Django for people.
## Installation
1)If you wish to run your own build, first ensure you have python globally installed in your computer.

2)After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

        `$ pip install virtualenv`

3)Then, Git clone this repo to your PC

### 4)Dependencies
  a) Cd into your the cloned repo as such:

  
    `cd post-managment-api`

  b) Create and fire up your virtual environment

  
     `virtualenv  venv -p python3`

     
     `$ source venv/bin/activate`
     

  c) Install the dependencies needed to run the app:

  
    `$ pip install -r requirements.txt`


  d) Make those migrations work:

  
    `$ python manage.py makemigrations

    
    $ python manage.py migrate`



#### Run It:
Run the server using command:


`$ python manage.py runserver`



You can now access the file api service on your browser by using



`http://localhost:8000/api/posts/`
