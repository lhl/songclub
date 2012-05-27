(function() {

  define(['Underscore', 'Backbone', 'models/file'], function(_, Backbone, File) {
    var Files;
    Files = Backbone.Collection.extend({
      model: File
    });
    return Files;
  });

}).call(this);
