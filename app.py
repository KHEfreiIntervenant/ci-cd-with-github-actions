from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# In-memory database
items = []

@app.route('/staging', methods=['POST'])
def staging():
    os.system('git pull origin staging')
    os.system('pip3 install -r requirements.txt')
    os.system('python -m unittest test_app.py')
    os.system('python test_integration.py')
    return ('', 204)


@app.route('/deploy', methods=['POST'])
def deploy():
    os.system('git pull origin main')
    os.system('pip3 install -r requirements.txt')
    os.system('python app.py')
    return ('', 204)

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
