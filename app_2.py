from flask import Flask

app = Flask(__name__)

@app.route('/app2')
def index():
  return 'Hello, APP2!'
