from flask import Flask, render_template

import MainProcess

app = Flask(__name__)

@app.route('/savings')
def savings():
    savingsList = []
    savingsList = MainProcess.processSaving()

    return render_template('savings.html', savings=savingsList, count=len(savingsList))

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/layout1')
def layout1():
    return render_template('layout1.html')

if __name__ == '__main__':
    app.run()
