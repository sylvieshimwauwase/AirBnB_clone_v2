from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def displayState():
    """ html page to display states created"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontent
def teardown(self):
    """ removing current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
