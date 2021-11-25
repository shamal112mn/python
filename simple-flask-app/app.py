from flask import Flask, render_template, url_for
import socket

serverName = socket.gethostname()

app = Flask(__name__)

@app.route('/')
def index():
  return   render_template('index.html', value1=serverName)  #"Hello World!"

if __name__ == "__name__":
  app.run(debug=True)

  ## type terminal 
  ## flask run