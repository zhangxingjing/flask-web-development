from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
import config
from wtf import NameForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(config)


# @app.route('/',methods=['GET','POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         redirect(url_for('index'))
#     return render_template('index.html',form=form,name=name)


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = NameForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form)
#
#
# @app.route('/macro/')
# def macro():
#     comments = ["To Be", "Or", "Not To Be"]
#     return render_template('macro.html', comments=comments)
#
# @app.errorhandler(404)
# def not_found(e):
#     return redirect(url_for('macro'),page=2)

if __name__ == '__main__':
    app.run()
