from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

iff __name__ == '__main__':
    app.debug= True
    app.run()
