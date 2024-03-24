from flask import Flask, render_template, request
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import pandas
import json
from data_analysis import filter


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("frontend/index.html")
@app.route('/plot')
def plot():
    return render_template("3d-plot.html")
@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        query = request.form.get("search_query")
        filter(query)
        # Assuming you're searching for a match in the 'Name' column
        return render_template('new_3d-plot.html')
    

if __name__ == '__main__':
    app.run(debug=True)
