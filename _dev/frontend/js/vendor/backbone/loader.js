define(['vendor/jquery/jquery.min', 'vendor/underscore/underscore.min', 'vendor/backbone/backbone.min'],
function(){
  return {
    Backbone: Backbone.noConflict(),
    _: _.noConflict(),
    $: jQuery.noConflict()
  };
});
