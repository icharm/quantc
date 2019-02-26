
// 监听collapse卡片展开事件
$(".collapse").on('show.bs.collapse', function(e) {
  console.log(e.currentTarget.id);
  showKLineChart(e.currentTarget.id)
});

var charts = new Map();

// echarts resize
// $(function() {
//     function resize() {
//         setTimeout(function() {
//             for (var [key, value] of charts) {
//                 value.resize();
//             }
//         }, 100)
//     }
//     $(window).on("resize", resize), $(".sidebartoggler").on("click", resize)
// });

function showKLineChart(id) {
    // 判断是否重复初始化
    if (charts.get(id)) {
        console.log(1);
        return;
    }
    // 基于准备好的dom，初始化echarts实例
    var kline = echarts.init(document.getElementById(id));
    charts.set(id, kline);

    // 指定图表的配置项和数据
    var option = {

        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:['max temp','min temp']
        },
        toolbox: {
            show : true,
            feature : {
                magicType : {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        color: ["#55ce63", "#009efb"],
        calculable : true,
        xAxis : [
            {
                type : 'category',

                boundaryGap : false,
                data : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            }
        ],
        yAxis : [
            {
                type : 'value',
                axisLabel : {
                    formatter: '{value} °C'
                }
            }
        ],

        series : [
            {
                name:'max temp',
                type:'line',
                color:['#000'],
                data:[11, 11, 15, 13, 12, 13, 10],
                markPoint : {
                    data : [
                        {type : 'max', name: 'Max'},
                        {type : 'min', name: 'Min'}
                    ]
                },
                itemStyle: {
                    normal: {
                        lineStyle: {
                            shadowColor : 'rgba(0,0,0,0.3)',
                            shadowBlur: 10,
                            shadowOffsetX: 8,
                            shadowOffsetY: 8
                        }
                    }
                },
                markLine : {
                    data : [
                        {type : 'average', name: 'Average'}
                    ]
                }
            },
            {
                name:'min temp',
                type:'line',
                data:[1, -2, 2, 5, 3, 2, 0],
                markPoint : {
                    data : [
                        {name : 'Week minimum', value : -2, xAxis: 1, yAxis: -1.5}
                    ]
                },
                itemStyle: {
                    normal: {
                        lineStyle: {
                            shadowColor : 'rgba(0,0,0,0.3)',
                            shadowBlur: 10,
                            shadowOffsetX: 8,
                            shadowOffsetY: 8
                        }
                    }
                },
                markLine : {
                    data : [
                        {type : 'average', name : 'Average'}
                    ]
                }
            }
        ]
    };

    // 使用刚指定的配置项和数据显示图表。
    // kline.setOption(option);
    kline.setOption(option, true), $(function() {
            function resize() {
                setTimeout(function() {
                    kline.resize()
                }, 100)
            }
            $(window).on("resize", resize), $(".sidebartoggler").on("click", resize)
        });
}


