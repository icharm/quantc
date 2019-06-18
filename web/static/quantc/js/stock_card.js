// All charts
var charts = new Map();
// Cache all cards tab statue.
var tabs = new Map();

// 监听collapse卡片展开事件
$(".collapse").on('show.bs.collapse', function(e) {
    var id = e.currentTarget.id;
    if (defaultTab === 'd') {
        tabs.set(id, 'd');
        $("#d-" + id).tab('show');
        return showKLineChart(id, 'd');
    } else {
        tabs.set(id, 'w');
        $("#w-" + id).tab('show'); //展示第二个tab页
        return showKLineChart(id, 'w');
    }
});

$("#tabs a").on('shown.bs.tab', function(e){
    let id = e.target.id;
    let tmp = id.split('-');
    let type = tmp[0], code = tmp[1];
    tabs.set(code, type);
    return showKLineChart(code, type);
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
    // let $chartParentDiv = $("#"+id);
    // let height = $chartParentDiv.height() - 100;
    // let width = $chartParentDiv.width();
    if ($card.hasClass("card-fullscreen")) {
        // chart.setSize(width, height);
        chart.reflow();
        if (type === 'd')
            chart.rangeSelector.clickButton(2);
    } else {
        // chart.setSize(width, 500);
        chart.reflow();
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
            setData(chart, ret, "");
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
            setDataWeekly(chart, ret);
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

function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}