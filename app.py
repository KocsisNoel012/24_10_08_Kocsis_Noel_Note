from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=Đ['GET','POST'])
def index():
    if request.method == 'POST':
        mame= request.form.get('name')
    return render_template("index.html", name = name)


if __name__ == "__main__":
    app.run(debug=True)