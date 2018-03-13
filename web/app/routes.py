from flask import Flask, request, render_template
from app import app
import requests

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/results', methods=['GET', 'POST'])
def results():
    response = ''
    if request.method == 'POST':
        term = str(request.form.get('search_input')) # as a default use 'mock', later I will add a second search input for tags
        url = "https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&closed=False&tagged=python-3.x&title="+term+"&site=stackoverflow"
        response = requests.get(url)
        r = app.response_class(response.content, content_type='application/json')
        return r #need to impliment a cache and seperate the get/post to allow data to be formated before it is returned.
    return render_template('results.html', title='Results', body=r)

@app.route('/favorites')
def favorites():
    return render_template('favorites.html', title='Favorites')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=True, debug=True)
