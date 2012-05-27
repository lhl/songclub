(function() {

  define(['jQuery', 'Underscore', 'Backbone', 'collections/files'], function($, _, Backbone, Files) {
    var FilesListView;
    FilesListView = Backbone.View.extend({
      initialize: function() {
        return this.template = _.template($('#files_list_template').html());
      },
      render: function() {
        $(this.el).html(this.template({
          files: this.options.files
        }));
        return this;
      }
    });
    return FilesListView;
  });

}).call(this);
