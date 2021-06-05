from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/')
def wiki():
    return render_template('wiki.html')


if __name__ == '__main__':
    app.run()