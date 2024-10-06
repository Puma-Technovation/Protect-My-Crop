from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/mundo')

def mundo():
    return render_template('mundo.html')

@app.route('/manual')

def manual():
    return render_template('manual.html')

if __name__ == '__main__':
    app.run(debug=True)
