import hashlib, os, base64
from flask import Flask, request, render_template
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['accounts_database']
collection = db['accounts']
app = Flask(__name__)

@app.route('/')
def home():
    return '<!DOCTYPE html>\
    <html>\
        <head>\
            <title>Welcome</title>\
            <style>\
                .container {\
  position: relative;\
  width: 100%;\
  margin: 0 0 0 0;\
  padding: 0 0 0 0;\
  border: 0 0 0 0;\
}\
\
.container img {\
  width: 100%;\
  height: auto;\
  margin: 0 0 0 0;\
  padding: 0 0 0 0;\
  border: 0 0 0 0;\
}\
\
.container .btn {\
  position: absolute;\
  top: 45%;\
  left: 50%;\
  transform: translate(-50%, -50%);\
  -ms-transform: translate(-50%, -50%);\
  background-color: #555;\
  color: white;\
  font-size: 16px;\
  padding: 12px 24px;\
  border: none;\
  cursor: pointer;\
  border-radius: 5px;\
}\
\
.container .btn2 {\
    position: absolute;\
    top: 55%;\
    left: 50%;\
    transform: translate(-50%, -50%);\
    -ms-transform: translate(-50%, -50%);\
    background-color: #555;\
    color: white;\
    font-size: 16px;\
    padding: 12px 24px;\
    border: none;\
    cursor: pointer;\
    border-radius: 5px;\
  }\
\
.container .btn:hover, .container .btn2:hover {\
  background-color: black;\
}\
            </style>\
        </head>\
        <body>\
            <div class="container">\
                <img src="/static/CyMa.jpg" alt="do">\
                <button class="btn" onclick="location.href=\'/login\'">Login</button>\
                <button class="btn2" onclick="location.href=\'/register\'">Sign-up</button>\
            </div>\
        </body>\
    </html>'

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    elif request.method == "POST":
        # Do signup stuff
        if request.form['password'] != request.form['confirm-password']:
            #return "Passwords don't match!"
            return str('<!DOCTYPE html>\
<html>\
    <head>\
        <title>Response</title>\
        <style>\
            /* Set height to 100% for body and html to enable the background image to cover the whole page: */\
body, html {\
  height: 100%\
}\
\
.bgimg {\
  /* Background image */\
  background-image: url(\'/static/blur.jpg\');\
  /* Full-screen */\
  height: 100%;\
  /* Center the background image */\
  background-position: center;\
  /* Scale and zoom in the image */\
  background-size: cover;\
  /* Add position: relative to enable absolutely positioned elements inside the image (place text) */\
  position: relative;\
  /* Add a white text color to all elements inside the .bgimg container */\
  color: white;\
  /* Add a font */\
  font-family: "Courier New", Courier, monospace;\
  /* Set the font-size to 25 pixels */\
  font-size: 25px;\
}\
\
/* Position text in the top-left corner */\
.topleft {\
  position: absolute;\
  top: 0;\
  left: 16px;\
}\
\
/* Position text in the bottom-left corner */\
.bottomleft {\
  position: absolute;\
  bottom: 0;\
  left: 16px;\
}\
\
/* Position text in the middle */\
.middle {\
  position: absolute;\
  top: 50%;\
  left: 50%;\
  transform: translate(-50%, -50%);\
  text-align: center;\
}\
\
/* Style the <hr> element */\
hr {\
  margin: auto;\
  width: 40%;\
}\
        </style>\
    </head>\
    <body>\
            <div class="bgimg">\
                    <div class="middle">\
                      <h1>Error</h1>\
                      <hr>\
                      <p>Passwords do not match</p>\
                    </div>\
                  </div>\
    </body>\
</html>')
        elif bool(collection.find_one({'Username': request.form['username']})):
            #return "Account already exists!"
            return str('<!DOCTYPE html>\
<html>\
    <head>\
        <title>Response</title>\
        <style>\
            /* Set height to 100% for body and html to enable the background image to cover the whole page: */\
body, html {\
  height: 100%\
}\
\
.bgimg {\
  /* Background image */\
  background-image: url(\'/static/blur.jpg\');\
  /* Full-screen */\
  height: 100%;\
  /* Center the background image */\
  background-position: center;\
  /* Scale and zoom in the image */\
  background-size: cover;\
  /* Add position: relative to enable absolutely positioned elements inside the image (place text) */\
  position: relative;\
  /* Add a white text color to all elements inside the .bgimg container */\
  color: white;\
  /* Add a font */\
  font-family: "Courier New", Courier, monospace;\
  /* Set the font-size to 25 pixels */\
  font-size: 25px;\
}\
\
/* Position text in the top-left corner */\
.topleft {\
  position: absolute;\
  top: 0;\
  left: 16px;\
}\
\
/* Position text in the bottom-left corner */\
.bottomleft {\
  position: absolute;\
  bottom: 0;\
  left: 16px;\
}\
\
/* Position text in the middle */\
.middle {\
  position: absolute;\
  top: 50%;\
  left: 50%;\
  transform: translate(-50%, -50%);\
  text-align: center;\
}\
\
/* Style the <hr> element */\
hr {\
  margin: auto;\
  width: 40%;\
}\
        </style>\
    </head>\
    <body>\
            <div class="bgimg">\
                    <div class="middle">\
                      <h1>Error</h1>\
                      <hr>\
                      <p>The account already exists</p>\
                    </div>\
                  </div>\
    </body>\
</html>')
        else:
            username = request.form['username']
            password = request.form['password']
            salt = str(base64.b64encode(os.urandom(16)))
            password_hash = hashlib.sha3_224(
                str(password + salt).encode('utf-8')
            ).hexdigest()
            to_db = {
                'Username': username,
                'Password': password_hash,
                'Salt'    : salt
            }
            collection.insert_one(to_db)
            #return str("Created account " + username + "!")
            return str('<!DOCTYPE html>\
<html>\
    <head>\
        <title>Response</title>\
        <style>\
            /* Set height to 100% for body and html to enable the background image to cover the whole page: */\
body, html {\
  height: 100%\
}\
\
.bgimg {\
  /* Background image */\
  background-image: url(\'/static/blur.jpg\');\
  /* Full-screen */\
  height: 100%;\
  /* Center the background image */\
  background-position: center;\
  /* Scale and zoom in the image */\
  background-size: cover;\
  /* Add position: relative to enable absolutely positioned elements inside the image (place text) */\
  position: relative;\
  /* Add a white text color to all elements inside the .bgimg container */\
  color: white;\
  /* Add a font */\
  font-family: "Courier New", Courier, monospace;\
  /* Set the font-size to 25 pixels */\
  font-size: 25px;\
}\
\
/* Position text in the top-left corner */\
.topleft {\
  position: absolute;\
  top: 0;\
  left: 16px;\
}\
\
/* Position text in the bottom-left corner */\
.bottomleft {\
  position: absolute;\
  bottom: 0;\
  left: 16px;\
}\
\
/* Position text in the middle */\
.middle {\
  position: absolute;\
  top: 50%;\
  left: 50%;\
  transform: translate(-50%, -50%);\
  text-align: center;\
}\
\
/* Style the <hr> element */\
hr {\
  margin: auto;\
  width: 40%;\
}\
        </style>\
    </head>\
    <body>\
            <div class="bgimg">\
                    <div class="middle">\
                      <h1>Created account</h1>\
                      <hr>\
                      <p>Welcome ' + username + '</p>\
                    </div>\
                  </div>\
    </body>\
</html>')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if bool(collection.find_one({"Username": username})):
            # Username exists, do login
            salt = collection.find_one({"Username": username})['Salt']
            password_hash = hashlib.sha3_224(str(password + salt).encode('utf-8')).hexdigest()
            if password_hash == collection.find_one({"Username": username})['Password']:
                #Password hash matches
                #return str("Successfully logged in as " + username + "!")
                return str('<!DOCTYPE html>\
<html>\
    <head>\
        <title>Response</title>\
        <style>\
            /* Set height to 100% for body and html to enable the background image to cover the whole page: */\
body, html {\
  height: 100%\
}\
\
.bgimg {\
  /* Background image */\
  background-image: url(\'/static/blur.jpg\');\
  /* Full-screen */\
  height: 100%;\
  /* Center the background image */\
  background-position: center;\
  /* Scale and zoom in the image */\
  background-size: cover;\
  /* Add position: relative to enable absolutely positioned elements inside the image (place text) */\
  position: relative;\
  /* Add a white text color to all elements inside the .bgimg container */\
  color: white;\
  /* Add a font */\
  font-family: "Courier New", Courier, monospace;\
  /* Set the font-size to 25 pixels */\
  font-size: 25px;\
}\
\
/* Position text in the top-left corner */\
.topleft {\
  position: absolute;\
  top: 0;\
  left: 16px;\
}\
\
/* Position text in the bottom-left corner */\
.bottomleft {\
  position: absolute;\
  bottom: 0;\
  left: 16px;\
}\
\
/* Position text in the middle */\
.middle {\
  position: absolute;\
  top: 50%;\
  left: 50%;\
  transform: translate(-50%, -50%);\
  text-align: center;\
}\
\
/* Style the <hr> element */\
hr {\
  margin: auto;\
  width: 40%;\
}\
        </style>\
    </head>\
    <body>\
            <div class="bgimg">\
                    <div class="middle">\
                      <h1>Succesfully logged in</h1>\
                      <hr>\
                      <p>Welcome ' + username + '</p>\
                    </div>\
                  </div>\
    </body>\
</html>')
            else:
                #return str("Incorrect password for " + username + "!")
                return str('<!DOCTYPE html>\
<html>\
    <head>\
        <title>Response</title>\
        <style>\
            /* Set height to 100% for body and html to enable the background image to cover the whole page: */\
body, html {\
  height: 100%\
}\
\
.bgimg {\
  /* Background image */\
  background-image: url(\'/static/blur.jpg\');\
  /* Full-screen */\
  height: 100%;\
  /* Center the background image */\
  background-position: center;\
  /* Scale and zoom in the image */\
  background-size: cover;\
  /* Add position: relative to enable absolutely positioned elements inside the image (place text) */\
  position: relative;\
  /* Add a white text color to all elements inside the .bgimg container */\
  color: white;\
  /* Add a font */\
  font-family: "Courier New", Courier, monospace;\
  /* Set the font-size to 25 pixels */\
  font-size: 25px;\
}\
\
/* Position text in the top-left corner */\
.topleft {\
  position: absolute;\
  top: 0;\
  left: 16px;\
}\
\
/* Position text in the bottom-left corner */\
.bottomleft {\
  position: absolute;\
  bottom: 0;\
  left: 16px;\
}\
\
/* Position text in the middle */\
.middle {\
  position: absolute;\
  top: 50%;\
  left: 50%;\
  transform: translate(-50%, -50%);\
  text-align: center;\
}\
\
/* Style the <hr> element */\
hr {\
  margin: auto;\
  width: 40%;\
}\
        </style>\
    </head>\
    <body>\
            <div class="bgimg">\
                    <div class="middle">\
                      <h1>Incorrect password</h1>\
                      <hr>\
                      <p>Try again ' + username + '</p>\
                    </div>\
                  </div>\
    </body>\
</html>')
        else:
            #Username doesn't exist
            #return str("Can't find account " + username + "!")
            return str('<!DOCTYPE html>\
<html>\
    <head>\
        <title>Response</title>\
        <style>\
            /* Set height to 100% for body and html to enable the background image to cover the whole page: */\
body, html {\
  height: 100%\
}\
\
.bgimg {\
  /* Background image */\
  background-image: url(\'/static/blur.jpg\');\
  /* Full-screen */\
  height: 100%;\
  /* Center the background image */\
  background-position: center;\
  /* Scale and zoom in the image */\
  background-size: cover;\
  /* Add position: relative to enable absolutely positioned elements inside the image (place text) */\
  position: relative;\
  /* Add a white text color to all elements inside the .bgimg container */\
  color: white;\
  /* Add a font */\
  font-family: "Courier New", Courier, monospace;\
  /* Set the font-size to 25 pixels */\
  font-size: 25px;\
}\
\
/* Position text in the top-left corner */\
.topleft {\
  position: absolute;\
  top: 0;\
  left: 16px;\
}\
\
/* Position text in the bottom-left corner */\
.bottomleft {\
  position: absolute;\
  bottom: 0;\
  left: 16px;\
}\
\
/* Position text in the middle */\
.middle {\
  position: absolute;\
  top: 50%;\
  left: 50%;\
  transform: translate(-50%, -50%);\
  text-align: center;\
}\
\
/* Style the <hr> element */\
hr {\
  margin: auto;\
  width: 40%;\
}\
        </style>\
    </head>\
    <body>\
            <div class="bgimg">\
                    <div class="middle">\
                      <h1>Cannot find account</h1>\
                      <hr>\
                      <p>Try again ' + username + '</p>\
                    </div>\
                  </div>\
    </body>\
</html>')

if __name__ == '__main__':
    app.run()
