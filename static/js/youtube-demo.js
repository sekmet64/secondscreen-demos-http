var socket;
var intervalId;

$(document).ready(function(){

    var unique_id = Cookies.get('unique_id');
    $("#unique-id-link").text(unique_id)

  var params = { allowScriptAccess: "always" };
  var atts = { id: "ytplayer" };
  swfobject.embedSWF('http://www.youtube.com/apiplayer?enablejsapi=1&version=3&playerapiid=ytplayer',
    'ytapiplayer', '100%', '100%', '8', null, null, params, atts);


  socket = io.connect('http://ctrlcouch.com:8001/'); //, {resource: '/nodejs/socket.io'}
  socket.emit('connect', { uniqueId: unique_id });


  socket.on('select-video', function(message) {

    var videoId = message.videoId;

    ytplayer.loadVideoById(videoId);

    intervalId = window.setInterval(updateTime, 1000);
  });

  socket.on('play', function(message) {

    ytplayer.playVideo();

    intervalId = window.setInterval(updateTime, 1000);
  });


  socket.on('pause', function(message) {

    ytplayer.pauseVideo();

    window.clearInterval(intervalId);
  });

  socket.on('remote-connected', function(message) {
    $('.overlay').hide();
  })

});

 function onYouTubePlayerReady(playerId) {

 }

function updateTime() {
  var time = ytplayer.getCurrentTime();

  socket.emit('update-time', { timeElapsed: time });
}