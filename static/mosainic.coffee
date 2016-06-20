#Dropzone.options.upload =
#  success: ->
#    console.log(233)
Dropzone.autoDiscover = false;

d = $("div#upload").dropzone
  url: '/make'
  uploadMultiple: true
  successmultiple: (f, response)->
    $('div#upload').hide()
    map = L.map 'map', {minZoom: -3, crs: L.CRS.Simple}
    bounds = [[0, 0], [response.height, response.width]];
    image = L.imageOverlay(response.file, bounds).addTo(map)
    map.fitBounds(bounds);
