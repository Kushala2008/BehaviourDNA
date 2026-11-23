from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        typing = float(request.form["typing"])
        mouse = float(request.form["mouse"])

        # Example demo reference values
        typing_baseline = 5
        mouse_baseline = 10

        if abs(typing - typing_baseline) > 3 or abs(mouse - mouse_baseline) > 5:
            result = "Unusual behaviour detected. Please verify the session."
        else:
            result = "Behaviour appears similar to the sample baseline."

    return """
    <h1>BehaviourDNA</h1>
    <h3>A valid login is not the whole story.</h3>
    <p>Enter sample behaviour values to test our demo.</p>

    <form method="POST">
        <label>Typing rhythm score:</label>
        <input type="number" step="any" name="typing" required>
        <br><br>

        <label>Mouse activity score:</label>
        <input type="number" step="any" name="mouse" required>
        <br><br>

        <button type="submit">Analyse Behaviour</button>
    </form>

    <h3>""" + result + """</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)
