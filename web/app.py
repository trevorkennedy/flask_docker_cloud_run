from flask import Flask, render_template
import os 
  

application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('index.html')

@application.route('/hello')
def hello_whale():
    return 'Whale, Hello there!'


if __name__ == '__main__':
    port = os.getenv('PORT', 5000) 
    application.run(debug=True, host='0.0.0.0', port=port)