$(document).ready(function($) {

	var feedID = YOUR_FEED_ID; //#CHANGE IT
	var key = "YOUR_KEY"; //#CHANGE IT


    xively.setKey(key);

    xively.feed.get(feedID, function(data){
     var values = $.parseJSON(JSON.stringify(data, null, ' '));
     var updated = moment(values['updated']).unix();
     var now = moment().unix();
     if (now - updated > 200) {
        $('#status').addClass('offline').removeClass('online');;
     }else{
        $('#status').removeClass('offline').addClass('online');;
     }
    });

    $('#temperature p').xively('live', {
        feed: feedID,
        datastream: 'Temperature'
    });
    $('#humidity p').xively('live', {
        feed: feedID,
        datastream: 'Humidity'
    });

    if ( window.MozWebSocket ) {
        window.WebSocket = window.MozWebSocket;
    }

    if ( window.WebSocket ) {
        $('.websockets-supported').show();
    }

});
