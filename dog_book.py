from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/macro')
def macro():
    comments = ["To Be", "Or", "Not To Be"]
    return render_template('macro.html', comments=comments)

if __name__ == '__main__':
    app.run()
