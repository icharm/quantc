
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
        chart.setSize($chartParentDiv.width(), $chartParentDiv.height())
    } else {
        chart.setSize($chartParentDiv.width(), 500)
    }
});

var charts = new Map();

function showKLineChart(id) {
    // 判断是否重复初始化
    if (charts.get(id)) {
        console.log(1);
        return;
    }

    let chart = createStockChart('chart_'+id);
    charts.set(id, chart);
    let today = currentDate();
    chart.showLoading();
    $.ajax({
        url: '/sd/daily_line?code='+id,
        type:'GET',
        dataType: 'json',
        success: function (ret) {
            let nodes = ret.line;

            $.ajax({
                url: '/sd/quotes?code='+id,
                type:'GET',
                dataType: 'json',
                success: function (ret1) {
                    if (ret1.date.toString === today.toString) {
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

function currentDate() {
    let d = new Date();
    let date = (d.getFullYear()) + "-" +
            (d.getMonth() + 1) + "-" +
            (d.getDate());
    return date;
}

function timestamp(strtimg) {
    var date = new Date(strtime); //传入一个时间格式，如果不传入就是获取现在的时间了，这样做不兼容火狐。
    // 可以这样做
    var date = new Date(strtime.replace(/-/g, '/'));
    return date.getTime();
}

function currentStamp() {
    return new Date().getTime();
}