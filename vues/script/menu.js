$(function(){
    init();
    createEvents();
});

//  fontion pour les onglets hide tout les menus puis affiche l'onglet home
function init(){
    $("article.post").each(function(){
        $(this).hide();
    });
    $("article.post.home").each(function(){
        $(this).show();
    });
}

//  fonction qui permet le passage d'un onglet a un autre à l'aide de l'atribut className
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