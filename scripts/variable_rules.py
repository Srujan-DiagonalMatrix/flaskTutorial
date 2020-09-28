from flask import Flask
app = Flask(__name__)

#@app.route('/hello/<namee>')
@app.route('/<namee>')
def hello_name(namee):
    return 'Hello0000 %s !'% namee

# variable declaration
@app.route('/<int:var>')
def def_var(var):
    return 'Hello Variable %s ' %var

@app.route('/<float:var>')
def def_str(var):
    return 'Hello %f '%var+'welcome to Flash programming'


if __name__ == '__main__':
    app.run(debug=True)
