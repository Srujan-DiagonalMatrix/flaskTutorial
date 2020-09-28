from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World!'

def hello_world():
    return 'Welcome to the beautiful world!!!!!!!'

app.add_url_rule('/a','endPointName', hello_world)

if __name__ == '__main__':
    app.run(debug=True)
