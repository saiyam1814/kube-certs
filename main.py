from flask import Flask, render_template, request
import os
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('certs.html')
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=int(os.environ.get('PORT', 8080)))
