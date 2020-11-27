from os import sep
from flask import Flask, render_template, request, redirect, escape
from flask.helpers import url_for
from vsearch import search4letters

app = Flask(__name__)


# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')

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
    with open('vsearch.log', 'a') as log:
        # print(dir(req), res, file=log)

        # print(req.form, file=log, end='|')
        # print(req.remote_addr, file=log, end='|')
        # print(req.user_agent, file=log, end='|')
        # print(res, file=log)

        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')



# @app.route('/viewlog')
# def view_the_log() -> str:
#     with open('vsearch.log') as log:
#         # contents = escape(log.read())
#         contents = log.readlines()
#     return escape(''.join(contents))

@app.route('/viewlog')
def view_the_log() -> str:
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)

if __name__ == "__main__":
    app.run()
