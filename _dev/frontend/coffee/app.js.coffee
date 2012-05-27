define(
  [ 
    'jQuery'
    'Underscore'
    'Backbone'
    'views/files_list'
    'models/file'
    'collections/files'
  ]
  
  ($, _, Backbone, FilesListView, File, Files) ->
    log = (msg) -> console.log(msg)

    App = 
      init: ->
        files_attrs = [
          { path: '/foo.mp3', en_song_id: 1 },
          { path: '/bar.mp3', en_song_id: 2 },
          { path: '/baz.mp3', en_song_id: 3 },
        ]
        files_coll = new Files(new File(file_attrs) for file_attrs in files_attrs)
        window.fc = files_coll

        flv = new FilesListView(files: files_coll).render()
        $('.files_list').append(flv.el)

    return App
)
