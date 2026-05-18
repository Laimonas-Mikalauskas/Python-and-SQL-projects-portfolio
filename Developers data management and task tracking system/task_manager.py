from flask import Flask, render_template
app = Flask(__name__)  # Correctly instantiate the Flask app

@app.route("/Home")
def main_page():
    return render_template("index.html")

@app.route("/Tasks")
def assignments():
    return  

@app.route('/Task Types') 
def home():
    return "DevTasks\nHOMEPAGE"
  
@app.route('/Deadlines')
def home():
    return "Deadlines"
    "<h1>Months<h1>"
    "<h2>Days<h2>"


@app.route('/Updates')
def home():
    return "Updated Backend DevTasks"

@app.route('/Timeline')
def timeline():
    return "History"

@app.route('/Accomplishments')  # Fixed the spelling of "Accomplishments"
def progress():
    return "Accomplishments Tracker" 
   

@app.route('/Contact Us') 
def customer_support():
    return "Email, Messenger"

@app.route('/Follow Us')
def contacts():
    return "Facebook, Instagram"

@app.route("/")
def homepage():
    (__import__("1 design.css"))

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode