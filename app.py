from flask import Flask, render_template
from comments import comments

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', title='Главная страница', comments=comments)


if __name__ == '__main__':
    app.run()