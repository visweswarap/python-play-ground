# Using flask to make an api
# import necessary libraries and functions
from bsedata.bse import BSE
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)


@app.route('/home')
def home():
    b = BSE(update_codes=True)
    top_loosers = b.topLosers()
    top_gainers = b.topGainers()
    response = {"top-gaineras": top_gainers, "top-looswers": top_loosers}
    return response


@app.route('/quote', methods=['GET', 'POST'])
def quote():
    b = BSE(update_codes=True)
    response = {}
    return response


@app.route('/', methods=['GET'])
def root():
    return {'Version': '0.0.1', 'Author': "Vish Pepala"}


@app.route('/home/<msg>', methods=['GET'])
def disp(msg):
    return jsonify({'data': msg})


# driver function
if __name__ == '__main__':
    app.run(debug=True, port=5001)
