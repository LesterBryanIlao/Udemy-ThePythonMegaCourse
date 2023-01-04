import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name'])[
    'Rating'].mean().unstack()

month_average_crs


chart_def ="""
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating by Course by Month',
        align: 'center'
    },
    subtitle: {
        text: 'Made By: Lester Bryan Ilao',
        align: 'center'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: true,
        borderWidth: 1,
        backgroundColor:'#FFFFFF'
            # Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF'
    },
    xAxis: {
        plotBands: [{ // Highlight the two last years
            from: '2021-03',
            to: '2021-04',
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Rating'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Month {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        # series: {
        #     pointStart: 2000
        # },
        # areaspline: {
        #     fillOpacity: 0.5
        # }
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048
            ]
    }]
}
"""

def app():
    webPage = jp.QuasarPage()

    h1 = jp.QDiv(a=webPage, text="Analysis of Course Reviews",
                 classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(
        a=webPage, text="These graphs represent course review analysis.")
    
    hc = jp.HighCharts(a=webPage, options=chart_def)
    hc.options.xAxis.categories = list(month_average_crs.index)
    
    
    hc_data = [{"name": name, "data": [rate for rate in month_average_crs[name]]}
               for name in month_average_crs.columns]
    hc.options.series = hc_data
    return webPage

jp.justpy(app)
