(function() {

  define(['jQuery', 'Underscore', 'Backbone', 'views/artists_list'], function($, _, Backbone, ArtistsListView) {
    var App, log;
    log = function(msg) {
      return console.log(msg);
    };
    App = {
      init: function() {
        var alv;
        alv = new ArtistsListView({
          es_artist_hits: window.artists_result.hits.hits
        }).render();
        return $('#artists_list_container').append(alv.el);
      }
      /*
              files_attrs = [
                { path: '/foo.mp3', en_song_id: 1 },
                { path: '/bar.mp3', en_song_id: 2 },
                { path: '/baz.mp3', en_song_id: 3 },
              ]
              files_coll = new Files(new File(file_attrs) for file_attrs in files_attrs)
              window.fc = files_coll
      
              flv = new FilesListView(files: files_coll).render()
              $('.files_list').append(flv.el)
      */

    };
    return App;
  });

}).call(this);
