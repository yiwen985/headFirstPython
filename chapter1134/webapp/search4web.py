from os import sep
from flask import Flask, render_template, request, redirect, escape, session, copy_current_request_context
from flask.helpers import url_for
from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_login_in
from time import sleep
from threading import Thread

app = Flask(__name__)

app.secret_key = 'helloworld'

app.config['db_config'] = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'root',
            'database': 'vsearchlogdb'}

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))

    # log_request(request, results)
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        with UseDatabase(app.config['db_config']) as cursor:
            sleep(15)
            _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                req.form['letters'], 
                                req.remote_addr, 
                                req.user_agent.browser, 
                                res, ))
            print('log success.')
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except:
        print('log errors.')

    return render_template('results.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=title,
                            the_results=results,)
    
# @copy_current_request_context # error
# def log_request(req: 'flask_request', res: str) -> None:
#     with UseDatabase(app.config['db_config']) as cursor:
#         sleep(15)
#         _SQL = """insert into log
#                   (phrase, letters, ip, browser_string, results)
#                   values
#                   (%s, %s, %s, %s, %s)"""
#         cursor.execute(_SQL, (req.form['phrase'],
#                               req.form['letters'], 
#                               req.remote_addr, 
#                               req.user_agent.browser, 
#                               res, ))
#         print('log success.')


@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

@app.route('/logout')
def logout():
    session.pop('user')
    return 'Now logged out.'

@app.route('/viewlog')
@check_login_in
def view_the_log() -> str:
    try:
        with UseDatabase(app.config['db_config']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results
                    from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)
    except ConnectionError as err:
        print('Is your database switched on? Errpr:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('unknown errors.', str(err))
    return 'error'


if __name__ == "__main__":
    app.run()
