from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

pwd = "password"

@app.route('/static/<path:path>')
def img(path):
    return app.send_static_file(path)

@app.route('/', methods=['GET', 'POST'])
def login():
    username = "Theo"
    error = None
    if request.method == 'POST':
        if request.form['username'] != username or request.form['password'] != pwd:
            error = 'Authentication failed. Try again'
        else:
            return "You are connected sucessfully"
    return render_template('log.html', error=error)


@app.route('/cabinet', methods=["GET", "POST"])
def cabinet():
    global password
    if request.method == "GET":
        return render_template("cabinet.html", pwd=pwd)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)