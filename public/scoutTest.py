from flask import Flask #, render_template
app = Flask(__name__)

@app.route("/cool")
def test():
    #return render_template('index.html')
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)