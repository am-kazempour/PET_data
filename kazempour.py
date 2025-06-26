from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "amin"

if __name__ == '__main__':
    # Render خودش پورت رو مشخص میکنه، از متغیر محیطی بخون
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
