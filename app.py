from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

@app.route("/")
def index():
    x_data = ['A', 'B', 'C', 'D']
    y_data = [10, 15, 7, 12]
    bar = go.Bar(x=x_data, y=y_data)
    layout = go.Layout(title='Sample Plotly Bar Chart')
    fig = go.Figure(data=[bar], layout=layout)
    chart_html = pyo.plot(fig, include_plotlyjs=False, output_type='div')
    return render_template("index.html", chart=chart_html)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
