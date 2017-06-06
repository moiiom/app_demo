/**
 * Created by jason on 5/25/17.
 */

$(document).ready(function () {

    var pageTotal = 0;
    var pageSize = 20;
    var currPageNo = 0;

    var crateDiv = function () {
        if(pageTotal != 0 && currPageNo == pageTotal){
            var panelDiv = $("<div><h1>已没有最新文章</h1></div>");
            panelDiv.appendTo($("#news_content"));
            return;
        }
        $.getJSON("list?page=" + currPageNo, function (data) {
            console.log(data);
            var status = data["status"];
            if (status == 0) {
                pageTotal = data["total"] / pageSize;

                $.each(data["data"], function (i) {
                    var item = data["data"][i];
                    var id = item["id"];
                    var title = item["title"];
                    var url = item["url"];
                    var panelDiv = $('<div id="' + id + '" class="item"><div><h1><a href="'+url+'" target="_blank">' + title + '</a></h1></div><div style="margin-bottom: 10px;"><span>来源：'+item["nickname"]+'</span><span>'+item["postdate"]+'</span><span>阅读'+item["count"]+'</span><span>点赞:'+item["like"]+'</span></div><div>'  + item["context"] + '</div></div>');
                    panelDiv.appendTo($("#news_content"));
                });
            }
        });
    };

    crateDiv();

    if ($(document).scrollTop() <= 0) {
       console.log("滚动条已经到达顶部为0");
    }
    $(window).scroll(function () {
        if ($(document).scrollTop() >= $(document).height() - $(window).height()) {
             currPageNo ++;
             crateDiv();
        }
    });
});