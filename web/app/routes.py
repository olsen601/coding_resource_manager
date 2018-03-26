from flask import Flask, request, render_template
from api import stack_api, github_api, youtube_api
from data_store import archive
from app import app
import logging

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/results', methods=['GET', 'POST'])
def results():
    global response
    global response2
    if request.method == 'POST':
        term = str(request.form.get('search_input'))
        stackoverflow_response = stack_api.get_stack_source(term)
        logging.info('stackoverflow response received')
        github_response = github_api.get_git_source(term)
        logging.info('github response received')
        youtube_response = youtube_api.video(term)
        logging.info('youtube response received')
        print(stackoverflow_response)
        print(github_response)
        print(youtube_response)
        return render_template('results.html', title='Results', stack_template_data=stackoverflow_response, git_template_data=github_response, youtube_template_data=youtube_response)
        logging.info('responses rendered on html page')
    return render_template('results.html', title='Results', stack_template_data=github_response, git_template_data=github_response, youtube_template_data=youtube_response)

@app.route('/bookmark', methods=['GET', 'POST'])
def bookmark():
    archive.db_setup()
    global bookmarks
    if request.method == 'POST':
        source = str(request.form.get('source'))
        title = str(request.form.get('title'))
        link = str(request.form.get('link'))
        archive.db_add(source, title, link)
        logging.info('bookmark created')
        bookmarks = archive.db_data()
        return render_template('bookmark.html', title='Bookmarks', body=bookmarks)
    bookmarks = archive.db_data()
    return render_template('bookmark.html', title='Bookmarks', body=bookmarks)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=True, debug=True)
