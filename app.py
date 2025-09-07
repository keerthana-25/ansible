from flask import Flask
import socket

app = Flask(__name__)

hostname = "{{ hostname }}"
print("##", hostname)

@app.route("/")
def hello():
    return f"Hello World from {hostname}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

