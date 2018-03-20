from flask import Flask, request, render_template
from api import stack_api
from data_store import archive
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/results', methods=['GET', 'POST'])
def results():
    global response
    if request.method == 'POST':
        term = str(request.form.get('search_input'))
        response = stack_api.get_stack_source(term)
        return render_template('results.html', title='Results', body=response)
    return render_template('results.html', title='Results', body=response)

@app.route('/bookmark', methods=['GET', 'POST'])
def bookmark():
    archive.db_setup()
    global bookmarks
    if request.method == 'POST':
        source = str(request.form.get('source'))
        title = str(request.form.get('title'))
        link = str(request.form.get('link'))
        archive.db_add(source, title, link)
        bookmarks = archive.db_data()
        return render_template('bookmark.html', title='Bookmarks', body=bookmarks)
    bookmarks = archive.db_data()
    return render_template('bookmark.html', title='Bookmarks', body=bookmarks)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=True, debug=True)