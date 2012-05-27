(function() {

  define(['jQuery', 'Underscore', 'Backbone', 'views/files_list', 'models/file', 'collections/files'], function($, _, Backbone, FilesListView, File, Files) {
    var App, log;
    log = function(msg) {
      return console.log(msg);
    };
    App = {
      init: function() {
        var file_attrs, files_attrs, files_coll, flv;
        files_attrs = [
          {
            path: '/foo.mp3',
            en_song_id: 1
          }, {
            path: '/bar.mp3',
            en_song_id: 2
          }, {
            path: '/baz.mp3',
            en_song_id: 3
          }
        ];
        files_coll = new Files((function() {
          var _i, _len, _results;
          _results = [];
          for (_i = 0, _len = files_attrs.length; _i < _len; _i++) {
            file_attrs = files_attrs[_i];
            _results.push(new File(file_attrs));
          }
          return _results;
        })());
        window.fc = files_coll;
        flv = new FilesListView({
          files: files_coll
        }).render();
        return $('.files_list').append(flv.el);
      }
    };
    return App;
  });

}).call(this);
