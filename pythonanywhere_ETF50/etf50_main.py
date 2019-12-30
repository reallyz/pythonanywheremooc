from flask import Flask
from flask import render_template
from chart_plot import Chart_Plot

app = Flask(__name__)

chart = Chart_Plot()
context = {}

@app.route('/')
def index():
    context['twoline_graph'] = chart.twoline_graph()
    return render_template("chars.html", title='Home', context=context)
@app.route('/candle')
def index2():
    context['candle_stick'] = chart.candle_stick()

    return render_template("candle.html", title='Home', context=context)

if __name__ == '__main__':
    app.run()
