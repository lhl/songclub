/**************************
 * Application
 **************************/
App = Em.Application.create();

/**************************
 * Models
 **************************/
App.File = Em.Object.extend({
  id: null,
  en_song_id: null,
  en_artist_id: null,
  path: null
});


/**************************
 * Views
 **************************/
App.SearchTextField = Em.TextField.extend({
  insertNewline: function(){
    App.filesController.loadFiles();
  }
});

/**************************
 * Controllers
 **************************/
App.filesController = Em.ArrayController.create({
  content: [],
  loadFiles: function(query) {
    var files = this;
    var url = 'magic_path_to_get_files?'
    url += query;
    // $.getJSON(url,function(data){
    //   files.set('content', []);
    //   $(data).each(function(index,value){
    //     var t = App.Song.create({
    //       id: value.id,
    //       en_song_id: value.en_song_id,
    //       en_artist_id: value.en_artist_id,
    //       path: value.path
    //       files.pushObject(t);
    //     })
    //   });
    // });
  }
});

