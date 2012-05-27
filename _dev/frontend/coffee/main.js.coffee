require.config 
  paths:
    loader: 'vendor/backbone/loader'
    jQuery: "vendor/jquery/jquery"
    Underscore: "vendor/underscore/underscore"
    Backbone: "vendor/backbone/backbone"

require(
  [ "app" ],
  
  # The "app" dependency is passed in as "App"
  # Again, the other dependencies passed in are not "AMD" therefore don't pass a parameter to this function
  (App) -> App.init()
)
