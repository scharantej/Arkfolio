
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask app
app = Flask(__name__)

# Define the routes

# Home page route
@app.route("/")
def index():
    return render_template("index.html")

# About page route
@app.route("/about")
def about():
    return render_template("about.html")

# Projects page route
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Contact page route
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Submit inquiry form route
@app.route("/submit-inquiry", methods=["POST"])
def submit_inquiry():
    # Handle form submission and send inquiry email
    return redirect(url_for("contact"))

# Error page route
@app.route("/error")
def error():
    return render_template("error.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
