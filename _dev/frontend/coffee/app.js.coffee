define(
  [ 
    'jQuery'
    'Underscore'
    'Backbone'

    # 'views/files_list'
    # 'models/file'
    # 'collections/files'

    'views/artists_list'
  ]
  
  # ($, _, Backbone, FilesListView, File, Files, ArtistsListView) ->
  ($, _, Backbone, ArtistsListView) ->
    log = (msg) -> console.log(msg)

    App = 
      init: ->
        alv = new ArtistsListView(es_artist_hits: window.artists_result.hits.hits).render()
        $('#artists_list_container').append(alv.el)

      ###
        files_attrs = [
          { path: '/foo.mp3', en_song_id: 1 },
          { path: '/bar.mp3', en_song_id: 2 },
          { path: '/baz.mp3', en_song_id: 3 },
        ]
        files_coll = new Files(new File(file_attrs) for file_attrs in files_attrs)
        window.fc = files_coll

        flv = new FilesListView(files: files_coll).render()
        $('.files_list').append(flv.el)
      ###



    return App
)
