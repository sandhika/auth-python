# auth-phyton

Boilerplate/Starter Project for building RESTful APIs using Flask, SQLite, JWT authentication.

## Setup

**Step #1** - Install dependencies 

```bash
$ pip install -r requirements.txt
```


<br />

**Step #2** - setup `flask` command for our app

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

**Step #3** - start test APIs server at `localhost:5000`

```bash
$ flask run
```


### API

Register

```bash
POST /api/auth/register
{username:'yourname' ,email: 'youremail@gmail.com',nik:'yournik', password: 'yourpasswod'}
```

Sign-In

```bash
POST /api/auth/login
{email: 'youremail@gmail.com', password: 'yourpasswod'}
```

Logout

```bash
POST /api/auth/logout
```
