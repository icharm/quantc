// All charts
var charts = new Map();
// Cache all cards tab statue.
var tabs = new Map();
var todayDateStamp = currentDateStamp();

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
            if (defaultTab === 'd') {
                // Default is 0
                lis[0].className += ' active';
                tabs.set(id, 'd');
                return showKLineChart(id, 'd');
            } else {
                // active is just show style, only effective after clicking tag a.
                lis[1].className += ' active';
                $(lis[1]).children('a').click();
                tabs.set(id, 'w');
                return showKLineChart(id, 'w');
            }
        },
        onStepChanged: function(event, currentIndex, priorIndex) {
            let div = event.currentTarget;
            let lis = div.getElementsByTagName('li');
            $(lis[currentIndex]).addClass('active');
            $(lis[priorIndex]).removeClass('active');
            if (currentIndex === 0) {
                tabs.set(id, 'd');
                return showKLineChart(id, 'd');
            } else if (currentIndex === 1) {
                tabs.set(id, 'w');
                return showKLineChart(id, 'w');
            }
        }
    });

});

// 监听expand卡片全屏事件
// Toggle fullscreen
$('a[data-action="expand_hs"]').on('click',function(e){
    e.preventDefault();
    $(this).closest('.card').find('[data-action="expand_hs"] i').toggleClass('mdi-arrow-expand mdi-arrow-compress');
    $(this).closest('.card').toggleClass('card-fullscreen');
    // reset chart height width
    let id = e.currentTarget.parentNode.parentNode.nextElementSibling.id;
    let type = tabs.get(id);
    let chart = charts.get(chartId(id));
    let $card = $(this).closest('.card');
    let $chartParentDiv = $("#"+id);
    if ($card.hasClass("card-fullscreen")) {
        chart.setSize($chartParentDiv.width(), $chartParentDiv.height());
        if (type === 'd')
            chart.rangeSelector.clickButton(2);
    } else {
        chart.setSize($chartParentDiv.width(), 500);
        if (type === 'd')
            chart.rangeSelector.clickButton(1);
    }
});

function chartId(id){
    return tabs.get(id) + '_' + id;
}

// 绘制蜡烛图
function showKLineChart(id, type) {
    let chartID = type + '_' + id;
    // 判断是否重复初始化
    if (charts.get(chartID)) {
        // console.log('Already drawn. ' + chartID);
        return;
    }

    let chart = createStockChart('chart_' + chartID);
    charts.set(chartID, chart);
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
                setDataWeekly(chart, ret.nodes);
            }
            chart.hideLoading();
            // Default to show a year weekly nodes.
            chart.rangeSelector.clickButton(4);
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