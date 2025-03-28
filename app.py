from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/items")
def get_items():
    return "item1, item2"

@app.route("/dashboard")
def page_dash():
    return "Pagina dashboard"

@app.route("/home")
def page_home():
    return "Pagina Home"




if __name__ == '__main__':
    app.run(debug=True)
