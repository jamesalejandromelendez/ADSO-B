from flask  import Flask, render_template

app = Flask(__name__)
@app.route('/')
def principal():
    # return "<p>Hola mundo!!</p>"
    return render_template('principal.html')

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)


