#### Installing Heroku CLI


**Reference:** https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524






This will help you manage your application directly from command line.


> [Download and Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)


#### Creating a Heroku Account


If you don’t have a Heroku account yet, don’t worry it’s free, you will head over to [Heroku](https://dashboard.heroku.com/login) and get yourself a free account.


#### Getting started


Login to heroku in your terminal with the following command.


```bash
heroku login
```


You will be prompted to enter your email and password.


#### Steps


1. Initializing a git repository: `git init`


2. Create a heroku application: `heroku create your-first-heroku-app --buildpack heroku/python`


3. Add the remote heroku git repository: `heroku git:remote -a your-first-heroku-app`


4. Install gunicorn: `pip install gunicorn`


5. Create `requirements.txt`: `pip freeze > requirements.txt`


6. Create `Procfile` file (no extension)


   > The first `app` represents the name of the python file that runs your application or the name of the module it is in. The second `app` represents your app name. For example if your application runs from a `run.py` file that looks like this:


   ```python
   from flask import Flask
   my_awesome_app = Flask(__name__)
   ```


   >  it will be: `web: gunicorn run:my_awesome_app`


7. Commit


   ```bash
   git add .
   git commit -m "First commit for heroku"
   ```


   


8. Push: `git push heroku master`
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNjk5NDk0NTZdfQ==
-->
