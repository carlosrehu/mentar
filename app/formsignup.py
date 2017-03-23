from flask import Flask, render_template, request, flash
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('One or more items are missing.')
            return render_template('createprofile.html', form = form)
        else:
            return render_template('index.html')
    elif request.method == 'GET':
        return render_template('createprofile.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)
