$.ajaxSetup({async: false});

var map, infowindow = new google.maps.InfoWindow(), bounds = new google.maps.LatLngBounds();


$.getJSON('points.json', function (data) {
    points = data;
});

function initialize() {

    /*map setting*/
    $('#map-canvas').height(window.outerHeight / 1.5);

    map = new google.maps.Map(document.getElementById('map-canvas'), {
        zoom: 12,
        center: {lat:25.0501101, lng: 121.5255337}
    });

    var markers = [];
    for (p in points) {
        var latLng = new google.maps.LatLng(points[p]['latitude'], points[p]['longitude']);
        var markerTitle = points[p].title;
        if (null !== points[p].year) {
            markerTitle = points[p].title;
        }
        bounds.extend(latLng);
        var marker = new MarkerWithLabel({
            position: latLng,
            clickable: true,
            labelContent: markerTitle,
            labelClass: 'labels',
            labelAnchor: new google.maps.Point(100, 5),
            labelStyle: {opacity: 0.75}
        });
        marker.info = points[p];
        google.maps.event.addListener(marker, 'click', (function (marker) {
            return function () {
                var pageContent = '';
                pageContent += '<br /><b >時間：</b> ' + marker.info.start_time +'~'+marker.info.end_time;
                pageContent += '<br /><b >地點：</b>' + marker.info.location;
                pageContent += '<br /><a href="' + marker.info.href+'">' +'詳細資訊 </a>';
                var info = '<b>' + marker.info.title + '</b>';
                info += '<br /><b>時間：</b> ' + marker.info.start_time +'~'+marker.info.end_time;
                infowindow.setContent(info);
                infowindow.open(map, marker);
                $('#title').html(marker.info.title);
                $('#content').html(pageContent);
            }
        })(marker));
        markers.push(marker);
    }
    var markerCluster = new MarkerClusterer(map, markers, {maxZoom: 16});
    map.fitBounds(bounds);
}

google.maps.event.addDomListener(window, 'load', initialize);