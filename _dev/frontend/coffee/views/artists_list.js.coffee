define(
  [ 'jQuery',
    'Underscore'
    'Backbone',
  ]
  
  ($, _, Backbone) ->
    ArtistsListView = Backbone.View.extend
      initialize:  ->
        @template =  _.template $('#artists_list_template').html()

      render: ->
        artists = []
        for hit in @options.es_artist_hits
          artist = {}
          source = hit._source
          artist.name = source.name
          artist.terms = (term for term in source.terms when term.weight >= 0.8)[0..4] # take first 5 where weight > x
          artists.push(artist)
        
        $(@el).html(@template({artists: artists}))
        return this

    return ArtistsListView
)

