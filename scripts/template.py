from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/user/<user>/<int:depo>')
def hello_name(user,depo):
    return render_template('template.html', name=user, deposit=depo)

if __name__=='__main__':
    app.run(debug=True)
