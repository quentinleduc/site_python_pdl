var map;
function initGoogleMap() {
  map = new google.maps.Map( document.getElementById('map'), {
    center: {lat: 47.2165, lng: -1.55461 },
    zoom: 12,
    styles: [{
      featureType: 'poi',
      stylers: [{ visibility: 'off' }]  // Turn off points of interest.
    }, {
      featureType: 'transit.station',
      stylers: [{ visibility: 'on' }]  // Turn off bus stations, train stations, etc.
    }],
    disableDoubleClickZoom: true
  });
  
  //  Simple test de positionnement de marker et de recuperation de coordonnées
  map.addListener('click', function(e) {
    var marker = new google.maps.Marker({
      position: {lat: e.latLng.lat(), lng: e.latLng.lng()},
      map: map
    });
  });
}


  //  TODO : faire un fonction qui place un marker au coordonnées envoyer
  //  TODO : faire une fonction pour deplacer la map au coordonnées souhaiter
