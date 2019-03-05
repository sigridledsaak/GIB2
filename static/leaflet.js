function setMap(){
    console.log("Loading map");

    var map = L.map('map').setView([63.4, 10.4], 13);

    L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoibW9uc2VtIiwiYSI6ImNqczVzdGdmbTAwY24zeW9hMjJtYjk0YnIifQ.ddvzRzPgfKeLtF9RrFuZOg'
    }).addTo(map);

    //Calling the function here, but missing eventlist per now.
    // addMarkers(map, eventlist)

}
window.onload = setMap();




// var myEvent = {Title:"Tittel", venueCoordinates:[63.4224338, 10.3957807]}
//     var currentEvent = L.marker(myEvent.venueCoordinates).addTo(map);



//Function that adds markers to map.
//Also needs a array with events
function addMarkers(map, eventlist) {
    for (event in eventlist)
        var currentMarker = L.marker(event.venueCoordinates).addTo(map);
        currentMarker.bindPopup(event.Title +""); //Ikke sikker på om nødvendig med +""
        currentMarker.on('mouseover', function (ev) {
             ev.target.openPopup();
             currentMarker.on('mouseout', function (e) {
                 e.target.closePopup();

             })

         })}