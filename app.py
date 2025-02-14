from flask import Flask, request, jsonify, render_template
import cohere

app = Flask(__name__)


api_key = "nwbGirw4Iy77ONBeNtuITMGorVjBudRzOKZkxeRj"  
co = cohere.Client(api_key)

@app.route("/")
def index():
    return render_template("index.html")  

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"response": "I didn't understand that."})

    response = co.generate(
        model='command',  
        prompt=user_input,
        max_tokens=100
    )

    bot_reply = response.generations[0].text.strip()
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run()
