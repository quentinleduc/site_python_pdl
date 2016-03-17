$(function(){
    init();
    createEvents();
});

function init(){
    $("article.post").each(function(){
        $(this).hide();
    });
    $("article.post.home").each(function(){
        $(this).show();
    });
}

function createEvents(){
    $("nav.links ul li").each(function(){$(this).on("click", function(){
        var className = $(this).attr("className");
        
        $("article.post").each(function(){
            $(this).hide();
        });
        
        $("article.post."+className).each(function(){
            $(this).show();
        });
    })});
}