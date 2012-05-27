define(
  [ 'jQuery',
    'Underscore'
    'Backbone',
    'collections/files' ]
  
  ($, _, Backbone, Files) ->
    FilesListView = Backbone.View.extend
      initialize:  ->
        @template =  _.template $('#files_list_template').html()

      render: ->
        $(@el).html(@template({files: @options.files}))
        return this

    return FilesListView
)

