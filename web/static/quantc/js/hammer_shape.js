
// 监听collapse卡片展开事件
$(".collapse").on('show.bs.collapse', function(e) {
  console.log(e.currentTarget.id);
  showKLineChart(e.currentTarget.id)
});

var charts = new Map();

// echarts resize
// $(function() {
//     setTimeout(function () {
//         window.onresize = function () {
//
//         }
//     }, 200);
// });

// $(window).on('resize', function(){
//     setTimeout(function () {
//         charts.forEach(function (value, key, map) {
//             container = document.getElementById(key);
//             resizeChartContainer(container, key);
//             value.resize()
//         });
//     }, 200)
//
// });

// function resizeChartContainer(container, id){
//     // 使用原生获取dom的方式echarts无法获取宽高度。
//     container.setAttribute('width', $("#"+id).width());
//     container.setAttribute('height', $("#"+id).height());
// }

function showKLineChart(id) {
    // 判断是否重复初始化
    if (charts.get(id)) {
        console.log(1);
        return;
    }
    // 基于准备好的dom，初始化echarts实例，
    chartContainer = document.getElementById(id);
    // dailyLineData('600606');

    $.ajax({
        url: '/sd/daily_line?code=600606',
        type:'GET',
        dataType: 'json',
        success: function (ret) {
            console.log(ret.line);
            highStockChart('002458', ret.line);
        },
        error: function (ret) {
            console.log(ret)
        }
    });

    // resizeChartContainer(chartContainer, id);
    // var kline = echarts.init(chartContainer);
    // charts.set(id, kline);
    //
    // // 指定图表的配置项和数据
    //
    //
    // // 使用刚指定的配置项和数据显示图表。
    // // kline.setOption(option);
    // kline.setOption(option, true);
}

// var upColor = '#ff4a68';
// var upBorderColor = '#8A0000';
// var downColor = '#26a69a';
// var downBorderColor = '#008F28';
//
//
//
// function splitData(rawData) {
//     var categoryData = [];
//     var values = []
//     for (var i = 0; i < rawData.length; i++) {
//         categoryData.push(rawData[i].splice(0, 1)[0]);
//         values.push(rawData[i])
//     }
//     return {
//         categoryData: categoryData,
//         values: values
//     };
// }
//
// function calculateMA(dayCount) {
//     var result = [];
//     for (var i = 0, len = data0.values.length; i < len; i++) {
//         if (i < dayCount) {
//             result.push('-');
//             continue;
//         }
//         var sum = 0;
//         for (var j = 0; j < dayCount; j++) {
//             sum += data0.values[i - j][1];
//         }
//         result.push(sum / dayCount);
//     }
//     return result;
// }
//
//
//
