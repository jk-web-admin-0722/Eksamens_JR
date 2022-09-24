from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hesburgers')
def hesburgers():
    return render_template('hesburgers.html')

@app.route('/megaburgers')
def mega():
    return render_template('megaburgers.html')

@app.route('/kebab_burgers')
def kebab():
    return render_template('kebab_burgers.html')

@app.route('/hamburgers')
def hamburgers():
    return render_template('hamburgers.html')

@app.route('/siera_burgers')
def siera_burgers():
    return render_template('siera_burgers.html')

@app.route('/dsiera_burgers')
def dsiera_burgers():
    return render_template('dsiera_burgers.html')

@app.route('/registracija')
def registracija():
    return render_template('registracija.html')

if __name__ == '__main__':
    app.run(debug = True)