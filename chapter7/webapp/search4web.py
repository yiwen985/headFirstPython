from os import sep
from flask import Flask, render_template, request, redirect, escape
from flask.helpers import url_for
from vsearch import search4letters
# import mysql.connector
from DBcm import UseDatabase

app = Flask(__name__)

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
    log_request(request, results)
    return render_template('results.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=title,
                            the_results=results,)
    

def log_request(req: 'flask_request', res: str) -> None:
    with UseDatabase(app.config['db_config']) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'], 
                              req.remote_addr, 
                              req.user_agent.browser, 
                              res, ))

# def log_request(req: 'flask_request', res: str) -> None:
#     with open('vsearch.log', 'a') as log:
#         # print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
#         db_config = {
#             'host': '127.0.0.1',
#             'user': 'root',
#             'password': 'root',
#             'database': 'vsearchlogdb'
#         }

#         import mysql.connector

#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
#         _SQL = """insert into log
#                   (phrase, letters, ip, browser_string, results)
#                   values
#                   (%s, %s, %s, %s, %s)"""
#         cursor.execute(_SQL, (req.form['phrase'],
#                               req.form['letters'], 
#                               req.remote_addr, 
#                               req.user_agent.browser, 
#                               res, ))
#         conn.commit()
#         cursor.close()
#         conn.close()
        



@app.route('/viewlog')
def view_the_log() -> str:
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
# @app.route('/viewlog')
# def view_the_log() -> str:
#     contents = []
#     with open('vsearch.log') as log:
#         for line in log:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#     titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
#     return render_template('viewlog.html',
#                             the_title='View Log',
#                             the_row_titles=titles,
#                             the_data=contents,)

if __name__ == "__main__":
    app.run()
