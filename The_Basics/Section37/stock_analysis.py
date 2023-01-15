from pandas_datareader import data
import yfinance as yf
from datetime import datetime as dt
from bokeh.plotting import figure, show, output_file


start = dt(2022, 1, 1)
end = dt(2023, 1, 15)
data = yf.download("GOOG", start=start, end=end)


def increase_decrease(closePrice, openPrice):
    if closePrice > openPrice:
        value = "Increase"
    elif openPrice > closePrice:
        value = "Decrease"
    else:
        value = "Equal"
    return value


data['Status'] = [increase_decrease(cPrice, oPrice)
                  for cPrice, oPrice in zip(data.Close, data.Open)]

data["Middle"] = (data.Open+data.Close)/2
data["Height"] = abs(data.Open-data.Close)

# Create the figure
p = figure(x_axis_type='datetime', width=1200,
           height=300, title='Candlestick Chart', outline_line_alpha=0.3, sizing_mode="scale_width")

HOURS_12 = 12*3600*1000

p.segment(x0='Date', y0='Low', x1='Date',
          y1='High', color='#3c3c3c', source=data)
p.rect(data.index[data.Status == "Increase"], data.Middle[data.Status == "Increase"],
       HOURS_12, data.Height[data.Status == "Increase"], fill_color="#3cb371", line_color="#787878")

p.rect(data.index[data.Status == "Decrease"], data.Middle[data.Status == "Decrease"],
       HOURS_12, data.Height[data.Status == "Decrease"], fill_color="#ff0000", line_color="#787878")

# Add axis labels and title
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'

# Show the plot
output_file("CandlestickChart.html")
show(p)
