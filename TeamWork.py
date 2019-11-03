from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def First_web():
    return render_template("FirstWeb.html")

@app.route('/sign_in/')
def sign_in():
    return render_template("sign_in.html")

@app.route('/sign_up/')
def sign_up():
    return render_template("sign_up.html")

@app.route('/ForgetPassword/')
def ForgetPassword():
    return render_template("ForgetPassword.html")
@app.route('/AboutUs/')
def AboutUs():
    return render_template("AboutUs.html")

@app.route('/Page1/')
def Page1():
    return render_template("Page1.html")

@app.route('/Page2/')
def Page2():
    return render_template("Page2.html")

@app.route('/Page3/')
def Page3():
    return render_template("Page3.html")

@app.route('/Page4/')
def Page4():
    return render_template("Page4.html")

@app.route('/Page5/')
def Page5():
    return render_template("Page5.html")

@app.route('/Page6/')
def Page6():
    return render_template("Page6.htm")

if __name__ == '__main__':
    app.run(debug=True)
