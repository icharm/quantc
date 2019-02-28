
var upColor = '#ff4a68';
var upBorderColor = '#8A0000';
var downColor = '#26a69a';
var downBorderColor = '#008F28';
var borderColor = '#3C94C4';

function setData(chart, data, name='stock') {
	var ohlcArray = [], volumeArray = [], MA5Array = [], MA200Array = [];

	for (i = 0; i < data.length; i++) {
		ohlcArray.push([
			parseInt(data[i][0]), // the date
			parseFloat(data[i][1]), // open
			parseFloat(data[i][3]), // high
			parseFloat(data[i][4]), // low
			parseFloat(data[i][2]) // close
		]);
        volumeArray.push([
            parseInt(data[i][0]), // the date
            parseInt(data[i][6]) // 成交量
        ]);
	}
	console.log(data[data.length-1][0]);
	MA5Array = calculateMA(5, ohlcArray);
	MA200Array = calculateMA(200, ohlcArray);

	// setting data.
	chart.series[0].update({data: ohlcArray, name:name});
	chart.series[1].update({data: volumeArray});
	chart.series[2].update({data: MA5Array});
	chart.series[3].update({data: MA200Array});
}

function createStockChart(divID) {
    Highcharts.setOptions({ global: { useUTC: false } });// 设置不使用UTC，否则会少8小时。
	return new Highcharts.StockChart( {
		chart:{
			renderTo : divID,
			margin: [30, 30,30, 30],
			plotBorderColor: borderColor,
			plotBorderWidth: 0.3
		},
		loading: {
	    	labelStyle: {
                position: 'relative',
	            top: '10em',
	            zindex:1000
	    	}
	    },
        credits:{
		    enabled:false
        },
	    rangeSelector: {
	        selected: 1,
			enabled:true,
	        inputDateFormat: '%Y-%m-%d',  //设置右上角的日期格式
			verticalAlign: 'bottom',
			x: 0,
			y: 0
	    },
	    plotOptions: {
	    	//修改蜡烛颜色
	    	candlestick: {
	    		color: downColor,
	    		upColor: upColor,
	    		lineColor: downColor,
	    		upLineColor: upColor,
	    		maker:{
	    			states:{
	    				hover:{
	    					enabled:false,
	    				}
	    			}
	    		}
	    	}
	    },
		tooltip: {
            // split: true,
			shape: 'square',
            headerShape: 'callout',
            borderWidth: 0,
            shadow: false,
			positioner: function (width, height, point) {
                var chart = this.chart,
                    position;

                if (point.isHeader) {
                    position = {
                        x: Math.max(
                            // Left side limit
                            chart.plotLeft,
                            Math.min(
                                point.plotX + chart.plotLeft - width / 2,
                                // Right side limit
                                chart.chartWidth - width - chart.marginRight
                            )
                        ),
                        y: point.plotY
                    };
                } else {
                    position = {
                        x: point.series.chart.plotLeft,
                        y: point.series.yAxis.top - chart.plotTop
                    };
                }

                return position;
            }
        },
	    title: {
	        enabled:false
	    },
	    xAxis: {
            type: 'datetime',
            tickLength: 0,//X轴下标长度
    	},
	    yAxis: [
	        {
                title: {
                   enable:false
                },
                height: '80%',
                lineWidth:1,//Y轴边缘线条粗细
                gridLineColor: '#346691',
                gridLineWidth:0.1,
              // gridLineDashStyle: 'longdash',
                opposite:true
	        }, {
                title: {
                   enable:false
                },
                top: '80%',
                height: '20%',
                labels:{
                    x:-15
                },
                gridLineColor: '#346691',
                gridLineWidth:0.1,
                lineWidth: 1,
	        }
	    ],
	    series: [
            {
                type: 'candlestick',
                id:"candlestick",
                name: 'Daily Line',
                data: [],
                dataGrouping: {
                    enabled: false
                }
            }, {
                type: 'column',//2
                name: 'Volumn',
                data: [],
                yAxis: 1,
                dataGrouping: {
                    enabled: false
                }
            }, {
                type: 'spline',
                name: 'MA5',
                color:'#1aadce',
                data: [],
                lineWidth:1,
                dataGrouping: {
                    enabled: false
                }
            }, {
                type: 'spline',
                name: 'MA200',
                data: [],
                color:'#8bbc21',
                threshold: null,
                lineWidth:1,
                dataGrouping: {
                    enabled: false
                }
            }
	    ],
		responsive: {
            rules: [{
                condition: {
                    minWidth: 310,
					minHeight: 500
                },
            }]
        }
	});
}

// 计算均线数组
function calculateMA(dayCount, data) {
    var result = [];
    for (var i = 0, len = data.length; i < len; i++) {
        if (i < dayCount) {
            continue;
        }
        var sum = 0;
        for (var j = 0; j < dayCount; j++) {
            sum += data[i - j][1];
        }
        result.push([data[i][0], Number.parseFloat((sum / dayCount).toFixed(2))]);
    }
    return result;
}