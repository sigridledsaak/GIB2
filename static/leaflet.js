function setMap() {
    console.log("Loading map");

    var map = L.map('map').setView([63.4, 10.4], 13);


    L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoibW9uc2VtIiwiYSI6ImNqczVzdGdmbTAwY24zeW9hMjJtYjk0YnIifQ.ddvzRzPgfKeLtF9RrFuZOg'
    }).addTo(map);

    return map;

}

var map = setMap();
window.onload=map;
var marker = L.marker();
var clickcount=0;

//Lager maker i brukers posisjon
pos= document.getElementById("pos");
pos.addEventListener("click",getPosition);
function getPosition(){
    if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(pos) {
                //You have your location here
                console.log("Latitude: " + pos.coords.latitude +
                    " Longitude: " + pos.coords.longitude);
                    if (clickcount==0){
                        marker.setLatLng([pos.coords.latitude, pos.coords.longitude]);
                        map.setView([pos.coords.latitude, pos.coords.longitude], 13, {animation: true});
                        marker.bindPopup("<strong> Din posisjon!</strong>").addTo(map);
                        console.log("marker pååå");
                        circle = makeRadius([pos.coords.latitude, pos.coords.longitude],500);
                        circle.addTo(map);
                        console.log("sirkel på");
                        clickcount++;
                        console.log(clickcount);
                        }
                    else {
                        map.removeLayer(marker);
                        map.removeLayer(circle);

                }
            });
    }else {
        console.log("Geolocation is not supported by this browser.");
    }
}


//Gjør at man kan trykke på kartet for å få posisjon.
markpos= document.getElementById("markpos");
markpos.addEventListener("click",markPosition);
function markPosition(){
    map.on('click', function (e) {
        marker.setLatLng(e.latlng ,{ draggable: true }).addTo(map);

        marker.bindPopup("<strong>" + e.latlng + "</strong>").addTo(map);

        marker.on('dragend', markerDrag);
    })
}

function makeRadius(pos,radius){
    var circle = L.circle(pos, {
    color: 'blue',
    fillColor: 'blue',
    fillOpacity: 0.3,
    radius: radius});
    return circle;
}
