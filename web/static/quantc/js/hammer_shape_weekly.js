
// 监听collapse卡片展开事件
$(".collapse").on('show.bs.collapse', function(e) {
  // console.log(e.currentTarget.id);
    var id = e.currentTarget.id;
    // tabs change. doc: https://github.com/rstaib/jquery-steps/wiki/Settings
    $("#tabs_"+id).steps({
        headerTag: "h3",
        bodyTag: "section",
        labels: {
            current: ""
        },
        transitionEffect: "slideLeft",
        enableFinishButton: false,
        enablePagination: false,
        enableAllSteps: true,
        titleTemplate: "#title#",
        cssClass: "tabcontrol",
        onInit: function(event) {
            // 为Tabs 按钮添加样式
            let div = event.currentTarget;
            div.getElementsByTagName('ul')[0].className = 'btn-group';
            let lis = div.getElementsByTagName('li');
            for (i=0; i<lis.length; i++) {
                lis[i].className += ' btn btn-secondary';
            }
            // Default open first tab.
            lis[0].className += ' active';
            showKLineChart(id, 'd');
        },
        onStepChanged: function(event, currentIndex, priorIndex) {
            let div = event.currentTarget;
            let lis = div.getElementsByTagName('li');
            $(lis[currentIndex]).addClass('active');
            $(lis[priorIndex]).removeClass('active');
            if (currentIndex === 0) {
                showKLineChart(id, 'd');
            } else if (currentIndex === 1) {
                showKLineChart(id, 'w')
            }
        }
    });

  // showKLineChart(id)
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
                        window.location.href='/hsw?date='+ moment(t).format("YYYY-MM-DD")
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

function showKLineChart(id, type) {
    // 判断是否重复初始化
    if (charts.get(type+'_'+id)) {
        console.log('Already drawn. ' + id);
        return;
    }

    let chart = createStockChart('chart_' + type + '_' + id);
    charts.set(id, chart);
    chart.showLoading();
    if (type === 'd') {
        ajaxDaily(chart, id);
    } else if (type === 'w') {
        ajaxWeekly(chart, id);
    }
}

function ajaxDaily(chart, id) {
    $.ajax({
        url: '/sd/daily_line?code='+id,
        type:'GET',
        dataType: 'json',
        success: function (ret) {
            let nodes = ret.line;

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

function ajaxWeekly(chart, id) {
    $.ajax({
        url: '/sd/weekly_line?code='+id,
        type:'GET',
        dataType: 'json',
        success: function (ret) {
            if (ret !== '') {
                setData(chart, ret.nodes);
            }
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