from flask import Flask, request, render_template
from api import stack_api
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/results', methods=['GET', 'POST'])
def results():
    global response
    if request.method == 'POST':
        term = str(request.form.get('search_input')) # as a default use 'mock', later I will add a second search input for tags
        response = stack_api.get_stack_source(term)
        return render_template('results.html', title='Results', body=response)
    return render_template('results.html', title='Results', body=response)

@app.route('/favorites')
def favorites():
    return render_template('favorites.html', title='Favorites')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=True, debug=True)
