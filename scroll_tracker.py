from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# DSA: list (array) of progress tips
tips = [
    "Keep going!",
    "You're halfway there!",
    "Almost done!",
    "You made it to the end!"
]

# Logic to return a tip based on scroll percentage
def get_tip(percent):
    if percent < 25:
        return tips[0]
    elif percent < 50:
        return tips[1]
    elif percent < 75:
        return tips[2]
    else:
        return tips[3]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_tip", methods=["POST"])
def get_tip_api():
    data = request.json
    percent = data.get("percent", 0)
    tip = get_tip(percent)
    return jsonify({"tip": tip})

if __name__ == "__main__":
    app.run(debug=True)
