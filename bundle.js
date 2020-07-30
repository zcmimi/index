function setimgcube(){
    var scrw=document.body.clientWidth;
    if(scrw<400){
        list=document.getElementsByClassName("links-row");
        for(i in list)list[i].classList.remove("mdui-row-xs-2");
    }
    list=document.getElementsByClassName("link-img");
    for(i in list){
        var x;
        if(list[i].clientWidth>list[i].clientHeight)x=list[i].clientWidth;
        else x=list[i].clientHeight;
        list[i].style.width=x+"px";
        list[i].style.height=x+"px";
    }
}

function lazyload(){
    var images=document.getElementsByTagName('img'),
        len=images.length,
        n=0;
    var seeHeight=document.documentElement.clientHeight,
        scrollTop=document.documentElement.scrollTop||document.body.scrollTop;
    for(;n<len;++n)
    if(images[n].offsetTop<seeHeight+scrollTop){
        var datasrc=images[n].getAttribute('data-src');
        if(datasrc!=null&&images[n].src!=datasrc)
            images[n].src=images[n].getAttribute('data-src');
    }
    else break;
}