
// 监听collapse卡片展开事件
$(".collapse").on('show.bs.collapse', function(e) {
  // console.log(e.currentTarget.id);
  showKLineChart(e.currentTarget.id)
});

// 监听expand卡片全屏事件
// Toggle fullscreen
$('a[data-action="expand_hs"]').on('click',function(e){
    e.preventDefault();
    $(this).closest('.card').find('[data-action="expand_hs"] i').toggleClass('mdi-arrow-expand mdi-arrow-compress');
    $(this).closest('.card').toggleClass('card-fullscreen');
    // reset chart height width
    let id = e.currentTarget.parentNode.parentNode.nextElementSibling.id;
    let chart = charts.get(id);
    let $card = $(this).closest('.card');
    let $chartParentDiv = $("#"+id);
    if ($card.hasClass("card-fullscreen")) {
        chart.setSize($chartParentDiv.width(), $chartParentDiv.height());
        chart.rangeSelector.clickButton(2);
    } else {
        chart.setSize($chartParentDiv.width(), 500)
        chart.rangeSelector.clickButton(1);
    }
});

var datepaginator = function() {
    return {
        init: function() {
            let url = window.location.href;
            let date = url.split('?date=')[1];
            $("#paginator").datepaginator({
                    selectedDate: date,
                    selectedDateFormat:  'YYYY-MM-DD',
                    onSelectedDateChanged: function(a, t) {
                        window.location.href='/hs?date='+ moment(t).format("YYYY-MM-DD")
                    }
                })
        }
    }
}();
jQuery(document).ready(function() {
    datepaginator.init()
});

var charts = new Map();
var todayDateStamp = currentDateStamp();

function showKLineChart(id) {
    // 判断是否重复初始化
    if (charts.get(id)) {
        console.log(1);
        return;
    }

    let chart = createStockChart('chart_'+id);
    charts.set(id, chart);
    chart.showLoading();
    $.ajax({
        url: '/sd/daily_line?code='+id,
        type:'GET',
        dataType: 'json',
        success: function (ret) {
            let nodes = ret;

            $.ajax({
                    url: '/sd/quotes?code=' + id,
                    type: 'GET',
                    dataType: 'json',
                    success: function (ret1) {
                        if (todayDateStamp === timestamp(ret1.date+" 00:00:00")) {
                            nodes.push([
                                currentStamp(),
                                ret1.open,
                                ret1.close,
                                ret1.high,
                                ret1.low,
                                ret1.money,
                                ret1.volume,
                                0,
                                0
                            ])
                        }
                        setData(chart, nodes, ret1.name);
                    },
                    error: function (ret1) {
                        console.log(ret1);
                    }
                });

            chart.hideLoading();
        },
        error: function (ret) {
            console.log(ret);
            chart.hideLoading();
        }
    });
}


function timestamp(strtimg) {
    return Date.parse(new Date(strtimg)) / 1000;
}

function currentStamp() {
    return new Date().getTime();
}

function currentDateStamp() {
    return new Date(new Date().setHours(0, 0, 0, 0)) / 1000;
}