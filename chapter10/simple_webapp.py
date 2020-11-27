from flask import Flask, session
from checker import check_login_in

app = Flask(__name__)

app.secret_key = 'helloworld'

@app.route('/status')
def check_status() -> str:
    if 'logged in' in session:
        return "You're currently logged in."
    return "You're NOT logged in."

# @app.route('/page1')
# def page1() -> str:
#     if 'logged in' in session:
#         return "This is page1."
#     return "You're NOT logged in."

@app.route('/page1')
@check_login_in
def page1() -> str:
    return "This is page1."
    
@app.route('/page2')
@check_login_in
def page1() -> str:
    return "This is page1."

@app.route('/page3')
@check_login_in
def page1() -> str:
    return "This is page1."

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


if __name__ == "__main__":
    app.run()