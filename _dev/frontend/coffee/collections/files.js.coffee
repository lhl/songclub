define(
  [ 'Underscore'
    'Backbone',
    'models/file' ]
  
  (_, Backbone, File) ->
    Files = Backbone.Collection.extend
      model: File

    return Files
)
