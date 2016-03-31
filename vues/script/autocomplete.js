var datatable = null;

$(function(){
	datatable = $("#resultsearch section div.table-wrapper table").DataTable();
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
		//	Contact mon rest-example.py pour l'autocompletion
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
						//	TODO: Faire un lien pour lier l'autocompletion a la map
						str += '<li>'+value+"</li>";
					});
					str+="</ul>";
				}
				
				if(jsonData[1].length > 0){
					str+="<li><h1>Activitées :</h1></li><ul>";
					$.each(jsonData[1], function(key,value){
						//	TODO: Faire un lien pour lier l'autocompletion a la recherche
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
	
	var $title 			= 	$("#resultsearch header div.title h2");
	
	var $searchForm		=	$("#searchForm");
	var $searchBar		=	$("#searchBar");
	
	
	$searchForm.on('submit', function(e){
		e.preventDefault();
		if($searchBar.val().length <=0 ){
			return;
		}
		//	Contact mon rest-example.py pour la recherche
		$.ajax({
			url: "/search/"+$searchBar.val(),
			type: "GET",
			dataType: "JSON",
			success : function(jsonData){
				//	Reset an existing datatable
				datatable.clear().draw();
				
				if(jsonData == null || jsonData.length <= 0){
					$title.html("Aucune corespondance");
					return;
				}
				$title.html("Resultat de la Recherche:");
				$.each(jsonData, function(key,value){
					var row = [];
					$.each(jsonData[key], function(key,value){
						row.push(value);
					});
					//	TODO: Lier le lien a la map google pour placer un marker
					row.push('<a href="#" class="button fit small actions next">View Map</a>');
					datatable.row.add(row).draw();
				});
			},
			error: function(result,status,error){
				$title.html("Erreur avec la page !");
				return;
			}
			
		});
	});
}