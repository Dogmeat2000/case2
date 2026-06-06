import sqlite3

from flask import Flask, session, redirect, request, make_response

app = Flask("Login example")
app.secret_key = "your-secret-key-here"
con = sqlite3.connect("students.sqlite", check_same_thread=False)

cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username CHAR(100),
        name CHAR(100),
        password CHAR(100),
        email CHAR(150),
        role CHAR(150)
    );
""")

con.commit()

@app.route("/users")
def users():

   user_ = request.args.get('username')

   cur.execute("SELECT * FROM users where username = ? and role ='Administrator'", (user_,))
   rows = cur.fetchone()
   if rows:
       cur.execute("SELECT * FROM users")
       rows = cur.fetchall()

       result = "<ul> <li> <b>username &nbsp name &nbsp password &nbsp email &nbsp role</b></li>"
       for row in rows:
           result += "<li>"+ str(row[0]) + "&nbsp" + str(row[1]) + "&nbsp" + str(row[2]) + "&nbsp" + str(row[3]) + "&nbsp" + "</li>"

       return result + "</ul>"
   else:
       return "<h1> Permission Denied</h1>"

@app.route("/register")
def register():
   user_ = request.args.get('username')
   pass_ = request.args.get('password')
   name_ = request.args.get('fullname')
   email_ = request.args.get('email')
   role_ = request.args.get('roles')

   cur.execute("INSERT INTO users (username, name, password, email, role) VALUES (?, ?, ?, ?, ?)", (user_, name_, pass_, email_, role_))
   con.commit()
   return ("<html><head><title>Register</title><body>"+
           " Registration success for "+ user_+ " <a href='/login'>Please Login</a></body></html>")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/login")
def login():
    return ("<html><head><title>Login</title><body>" +
            " <h1> Please Login </h1 >" +
            " <form action='/users' method='get'>" +
            " <label>Username:</label><br> "+
            " <input type='text' name='username' id = 'u'><br><br>"+
            " <label>Password:</label><br>"+
            " <input type='password' name='password'><br><br>"+
            " <button type='submit'>Login</button>"+
            " </form><body>")

@app.route("/")
def index():
    resp_html = ("<html><head><title>XSS</title></head><body>"+
            " <h1>Please Register:</h1>" +
            " <form action='/register' method='get'>"+
            " <div id = 'div'>" +
            " <label>Username:</label><br> "+
            " <input type='text' name='username'><br><br>"+
            " <label>E-mail:</label><br> " +
            " <input type='text' name='email' id = 'e'><br><br>" +
            " <label>Full name:</label><br> " +
            " <input type='text' name='fullname' id = 'f'><br><br>" +
            " <label>Role:</label><br> " +
            " <select id = 'roles' name='roles'>"+
            " <option value='Administrator'>Administrator </option>" +
            " <option value='Student'> Student </option> <select>"
            " <br><br>" +
            " <label>Password:</label><br>"+
            " <input type='password' name='password' id ='pwd'>" +
            " <br><button type='submit'> Register </button>" +
            " <br><br></form>"+
            " <h1><a href='/login'>Please Login</a></h1>"+
            " <body>")
    resp = make_response(resp_html)
    resp.set_cookie(
        "session_id",
        "abc123",
        httponly=False,
        secure=False,
        samesite="Lax"
    )
    return resp

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)

