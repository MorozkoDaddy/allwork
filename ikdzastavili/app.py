from flask import Flask, render_template, request, redirect, url_for
 
app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('home'))
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        login = request.form['auth_login']
        password = request.form['auth_pass']
        email = request.form['auth_email']
        title = "Homers"
        return render_template('authres.html', login = login, password = password, email = email, title = title)
    return render_template('home.html')

@app.route('/text')
def text():
    title = "Texters"
    mda = "Im really hate u, ur stupid friend, ur dogs, cats. Dont touch, dont look in monitor"
    return render_template('text.html', mda = mda, title = title)

@app.route('/image')
def image():
    title = "Imager"
    return render_template('image.html', title= title)

@app.route('/table')
def table():
    title = "Tables"
    return render_template('table.html', title=title)

@app.route('/listin')
def listin():
    title = "Music"
    music = ['idk', 'idk2', 'maxabatpalisani', 'drdr']
    return render_template('listin.html', music = music, title = title)
    
if __name__ == '__main__': 
    app.run(debug=True)
    