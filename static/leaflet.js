function setMap(){
    console.log("Loading map");

    var map = L.map('map').setView([63.4, 10.4], 13);
/*
    var basemapUrl = 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png';

    L.tileLayer(basemapUrl).addTo(map)
*/
    L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 7,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoibW9uc2VtIiwiYSI6ImNqczVzdGdmbTAwY24zeW9hMjJtYjk0YnIifQ.ddvzRzPgfKeLtF9RrFuZOg'
    }).addTo(map);

    L.marker([63.4224338, 10.3957807]).addTo(map);
    /*
    utested1.bindPopup("StudenterSamfundet");
    utested1.on('mouseover',function(ev) {
        ev.target.openPopup();
        utested1.on('mouseout', function (e) {e.target.closePopup();
        });
    })
    */
}
window.onload = setMap();