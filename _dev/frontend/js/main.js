(function() {

  require.config({
    paths: {
      loader: 'vendor/backbone/loader',
      jQuery: "vendor/jquery/jquery",
      Underscore: "vendor/underscore/underscore",
      Backbone: "vendor/backbone/backbone"
    }
  });

  require(["app"], function(App) {
    return App.init();
  });

}).call(this);
