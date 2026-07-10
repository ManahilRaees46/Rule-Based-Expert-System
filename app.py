from flask import Flask, render_template, request

from rules import rules
from inference import forward_chaining

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        symptoms = request.form.getlist("symptoms")

        result = forward_chaining(symptoms, rules)

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)