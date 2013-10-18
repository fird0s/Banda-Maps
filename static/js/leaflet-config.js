




var map = L.map('map').setView([5.4902, 95.4073], 12); // make map in Banda Aceh, focus on University Syiah Kuala
	
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', 
		{
		maxZoom: 20,
		zoomControl: true,
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'
		}).addTo(map); // Tile layer


//BASIC CONFIG 


var marker = L.marker([5.5734, 95.36622], {icon: L.AwesomeMarkers.icon({icon: 'building', color: 'blue', spin:false}) }).addTo(map);
marker.bindPopup("<b>Gedung EKP</b><br> Lorem Ipsum is simply dummy text of <br> the printing and typesetting industry.");


var marker = L.marker([5.57283, 95.36741]).addTo(map); // add marker
marker.bindPopup("<b>BEJ</b><br> Lorem Ipsum is simply dummy text of <br> the printing and typesetting industry.");


//FOR MANUAL CONFIG AWESOME ICON/FONT AWESOME

var marker = L.marker([5.57284, 95.36694], {icon: L.AwesomeMarkers.icon({icon: 'building', color: 'blue', spin:false}) }).addTo(map);
marker.bindPopup("<b>GEDUNG UTAMA</b><br> Lorem Ipsum is simply dummy text of <br> the printing and typesetting industry.");

var marker = L.marker([5.57366, 95.36734], {icon: L.AwesomeMarkers.icon({icon: 'food', color: 'red', spin:false}) }).addTo(map);
marker.bindPopup("<b>KANTIN FE </b><br> Lorem Ipsum is simply dummy text of <br> the printing and typesetting industry.");

var marker = L.marker([5.57329, 95.36734], {icon: L.AwesomeMarkers.icon({icon: 'flag', color: 'cadetblue', spin:false}) }).addTo(map);
marker.bindPopup("<b>KANTIN FE </b><br> Lorem Ipsum is simply dummy text of <br> the printing and typesetting industry.");



var marker = L.marker([5.57366, 95.36582], {icon: L.AwesomeMarkers.icon({icon: 'home', color: 'green', spin:false}) }).addTo(map);
marker.bindPopup("<b>LAPANGAN BASKET</b><br> Lorem Ipsum is simply dummy text of <br> the printing and typesetting industry.");

var marker = L.marker([5.57378, 95.36716], {icon: L.AwesomeMarkers.icon({icon: 'building', color: 'blue', spin:false}) }).addTo(map);
marker.bindPopup("<b>DIPLOMA III</b><br> Lorem Ipsum is simply dummy text of <br> the printing and typesetting industry.");

var marker = L.marker([5.57358, 95.36663]).addTo(map); // add marker
marker.bindPopup("<b>Mesjid</b><br> Lorem Ipsum is simply dummy text of <br> the printing and typesetting industry.");



/*function onMapClick(e) {
    alert("You clicked the map at " + e.latlng);
}

map.on('click', onMapClick);*/


var popup = L.popup();
function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);





//for automatic  pop-up
/*var popup = L.popup()
    .setLatLng([5.57348, 95.36631])
    .setContent("I am a standalone popup.")
    .openOn(map); */ 

/*var circle = L.circle([5.57348, 95.36619], 34, {
    color: 'yellow',
    fillColor: '#f03',
    fillOpacity: 0.1
}).addTo(map);*/

/*var polygon = L.polygon([
    [5.57348, 95.36619],
    [5.57348, 95.36700],
    [5.57333, 95.36683]
]).addTo(map); */
