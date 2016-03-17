$(function(){
	setMenuEvents();
	setSearchEvents();
});


function setMenuEvents(){
	$("nav.main ul li.menu").on("click", function(){
		$("#resultmenu").html("");
		$("#searchmenu").focus();
	});
	$("#searchmenu").on('keyup', function(){
		var tab = $("#resultmenu");
		if($(this).val().length <=0 ){
			tab.html("");
			return;
		}
		$.ajax({
			url: "/completion/"+$(this).val(),
			type: "GET",
			dataType: "JSON",
			success : function(jsonData){
				if(jsonData == null || jsonData.length != 2 || ( jsonData[0].length <=0 && jsonData[1].length <=0) ){
					tab.html("<li><h1>Aucune corespondance</h1></li>");
					return;
				}
				var str="";
				if(jsonData[0].length > 0){
					str+="<li><h1>Villes :</h1></li><ul>";
					$.each(jsonData[0], function(key,value){
						str += '<li>'+value+"</li>";
					});
					str+="</ul>";
				}
				
				if(jsonData[1].length > 0){
					str+="<li><h1>Activitées :</h1></li><ul>";
					$.each(jsonData[1], function(key,value){
						str += '<li>'+value+"</li>";
					});
					str+="</ul>";
				}
				tab.html(str);
			},
			error: function(result,status,error){
				tab.html("<li><h1>Erreur avec la page!</h1></li>");
			}
			
		});
	});
}

function setSearchEvents(){
	
	var $content 		= 	$("#resultsearch");
	var $title 			= 	$("#resultsearch header div.title h2");
	var $table		 	= 	$("#resultsearch section div.table-wrapper table");
	var $table_content	= 	$("#resultsearch section div.table-wrapper table tbody");
	
	var $searchForm		=	$("#searchForm");
	var $searchBar		=	$("#searchBar");
	
	
	$searchBar.on("click", function(){
		$table_content.html("");
		$content.hide();
	});
	$searchForm.on('submit', function(){
		if($searchBar.val().length <=0 ){
			$table_content.html("");
			$table.hide();
			$content.hide();
			return;
		}
		$.ajax({
			url: "/search/"+$searchBar.val(),
			type: "GET",
			dataType: "JSON",
			success : function(jsonData){
				$content.show();
				
				if(jsonData == null || jsonData.length <= 0){
					$title.html("Aucune corespondance");
					$table_content.html("");
					$table.hide();
					return;
				}
				
				$table.show();
				var str="";
				$.each(jsonData, function(key,value){
					str+="<tr>";
					$.each(jsonData[key], function(key,value){
						str += '<td>'+value+"</td>";
					});
					str+="</tr>";
				});
				$table_content.html(str);
			},
			error: function(result,status,error){
				$content.show();
				$title.html("Erreur avec la page !");
				$table_content.html("");
				$table.hide();
				return;
			}
			
		});
	});
}