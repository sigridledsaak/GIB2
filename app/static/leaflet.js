function setMap(){;

    var map = L.map('map').setView([63.427704, 10.396219], 13);
    console.log("Loading map");
    L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoibW9uc2VtIiwiYSI6ImNqczVzdGdmbTAwY24zeW9hMjJtYjk0YnIifQ.ddvzRzPgfKeLtF9RrFuZOg'
    }).addTo(map);

    //Calling the function here, but missing eventlist per now.
    // addMarkers(map, eventlist)
    return map
}

var map;
try {
    this.map = setMap();
}catch(e){
    this.map = map;

}

window.onload=map;
var marker = L.marker();
var clickcount=0;

var Icon = L.Icon.extend({
    options: {
        iconUrl: 'https://cdn2.iconfinder.com/data/icons/location-map-simplicity/512/theatre-512.png',
        iconSize:     [30, 50],
        iconAnchor:   [15, 49]
    }
});
//bruk disse markerene så får me alle i samme størrelse og format.
//https://www.iconfinder.com/iconsets/map-locations-filled-pixel-perfect
var theaterpin = new Icon({iconUrl: 'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-16-256.png'});
var starpin = new Icon({iconUrl: 'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-28-512.png'});
var musicpin = new Icon({iconUrl : 'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-01-512.png'});
var partypin = new Icon({iconUrl : 'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-08-512.png'});
var coursepin=new Icon({iconUrl : 'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-24-512.png'});
var bookpin = new Icon({iconUrl : 'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-09-512.png'});
var outdoorpin=new Icon({iconUrl : 'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-27-256.png'});
var exhitionpin=new Icon({iconUrl:'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-13-512.png'});
var technologypin = new Icon ({iconUrl:'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-23-512.png'});
var foodpin = new Icon ({iconUrl : 'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-19-256.png'});
var sportpin = new Icon({iconUrl : 'https://cdn4.iconfinder.com/data/icons/soccer-american-football/100/f-11-512.png',iconSize :[50, 70]});
var personpin=new Icon({iconUrl:'https://cdn4.iconfinder.com/data/icons/social-messaging-productivity-5/128/map-location-person-512.png', iconSize : [50,40]});
var moviepin = new Icon({iconUrl: 'https://cdn2.iconfinder.com/data/icons/map-locations-filled-pixel-perfect/64/pin-map-location-02-512.png'});


function getCurrPosition(){
    if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(pos) {
                //You have your location here
                console.log("Latitude: " + pos.coords.latitude +
                    " Longitude: " + pos.coords.longitude);
                marker.setLatLng([pos.coords.latitude, pos.coords.longitude]);
                marker.setIcon(personpin);
                map.setView([pos.coords.latitude, pos.coords.longitude], 13, {animation: true});
                marker.bindPopup("<strong> Din posisjon!</strong>").addTo(map);
                //circle = makeRadius([pos.coords.latitude, pos.coords.longitude],500);
                //circle.addTo(map);
                var output = document.getElementById('pos');
                output.value = String(pos.coords.latitude+ ","+pos.coords.longitude);
            });
    }else {
        console.log("Geolocation is not supported by this browser.");
    }

}

//Lager maker i brukers posisjon
/*pos= document.getElementById("pos");
pos.addEventListener("click",getPosition);
function getPosition(){
    if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(pos) {
                //You have your location here
                console.log("Latitude: " + pos.coords.latitude +
                    " Longitude: " + pos.coords.longitude);
                marker.setLatLng([pos.coords.latitude, pos.coords.longitude]);
                marker.setIcon(personpin);
                map.setView([pos.coords.latitude, pos.coords.longitude], 13, {animation: true});
                marker.bindPopup("<strong> Din posisjon!</strong>").addTo(map);
                //circle = makeRadius([pos.coords.latitude, pos.coords.longitude],500);
                //circle.addTo(map);
                clickcount++;
                console.log(clickcount);
            });
    }else {
        console.log("Geolocation is not supported by this browser.");
    }
}
*/

function getMarkPosition(){
    map.on('click', function (e) {
        pos=e.latlng;
        console.log(pos);
        marker.setLatLng(e.latlng).addTo(map);
        marker.setIcon(starpin);
        marker.bindPopup("<strong>Marked position!'</strong>").addTo(map);
        //circle = makeRadius(e.latlng, 500);
        //circle.addTo(map);
        marker.on('dragend', markerDrag=false);
        var output = document.getElementById('markpos');
        output.value = String(pos.lat+ ","+pos.lng);
    });
}


//Gjør at man kan trykke på kartet for å få posisjon.
markpos= document.getElementById("markpos");
markpos.addEventListener("click",markPosition);
function markPosition() {
    map.on('click', function (e) {
        marker.setLatLng(e.latlng).addTo(map);
        marker.setIcon(starpin);
        marker.bindPopup("<strong>" + e.latlng + "</strong>").addTo(map);
        //circle = makeRadius(e.latlng, 500);
        //circle.addTo(map);
        marker.on('dragend', markerDrag=false);
    });
}
function makeRadius(pos,radius){
    var circle = L.circle(pos, {
    color: 'blue',
    fillColor: 'blue',
    fillOpacity: 0.3,
    radius: radius});
    return circle;
}

//Function that adds markers to map.
//Also needs a array with events
function addMarker(pos,title){
    //var map = document.getElementById('map');
    //console.log(category);
    //console.log(typeof(category));
    /*var icon;
    switch(category){
        case 'Concert' : icon = musicpin;
        break;
        case 'Theater': icon = theaterpin;
        break;
        case 'Party': icon = partypin;
        break;
        case 'Course'|| 'Lecture': icon = coursepin;
        break;
        case 'Literature' : icon = bookpin;
        break;
        case 'Outdoor' : icon = outdoorpin;
        break;
        case 'Exhibition':icon = exhitionpin;
        break;
        case 'Technology':icon=technologypin;
        break;
        case 'Food':icon = foodpin;
        break;
        case 'Sport':icon =sportpin;
        break;
        case 'Movies':icon = moviepin;
        break;
        default :
            icon = null;
    }
    console.log(icon);
    */
    //må hente title og description for å lage popup. Tips : gjør det med å lage en get request til apiet og bruke derfra.
    if (pos!=( 'None')){
        var currentMarker = L.marker(pos).addTo(map);
        tmpPopup = L.popup().setContent('<strong>'+title +'</strong>');
        currentMarker.bindPopup(tmpPopup); //Ikke sikker på om nødvendig med +""
    try {
        currentMarker.on('mouseover', function (ev) {
         ev.target.openPopup();
         currentMarker.on('mouseout', function (e) {
             e.target.closePopup();
         });
     });
    } catch {
        console.log('Ingen events med koordinater');
    }
    }
    /*if (icon != null){
        currentMarker.setIcon(icon);
    }
    */





}


