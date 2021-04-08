from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from pangram import findWords

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = "1G1RBP5YhFxkRTxTtFjO1G1RBP5YhFxkRTxTtFjO"


class ReusableForm(Form):
    required = TextField("Required:", validators=[validators.required()])
    letters = TextField("Letters:", validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        print(form.errors)
        if request.method == 'POST':
            required = request.form['required']
            letters = request.form['letters']
            print(required)
            print(letters)

        if form.validate():
            pangrams, otherwords = findWords(letters, required)
            flash(pangrams)
            flash(otherwords)
        else:
            flash('All the form fields are required.')

        return render_template('hello.html', form=form)

if __name__ == "__main__":
    app.run()
