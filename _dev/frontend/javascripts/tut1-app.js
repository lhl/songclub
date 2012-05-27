Example = Ember.Application.create({ 
  name: "Example Application",
  logo: "http://sympodial.com/images/logo.png",
  searchString: "%23EmberJS",
  ready: function() { 	
    Example.populate.getTweets();
    setInterval(function() {
      Example.populate.getTweets();

    }, 2000);
  }.observes("name")
})

Example.Item = Ember.Object.extend();
Example.LoopingView = Ember.View.extend();

Example.ChangeQuery = Ember.TextField.extend({ 
  change: function() { 
    var value = this.get('value');
    console.log("Value: " + value);
    Example.set("searchString", value);
    //Example.populate.getTweets();
  }
});

Example.populate = Ember.ArrayController.create({ 
  content: [],
  idArray: {},
  addItem: function(item) { 
    var id = item.id;
    if(typeof this.idArray[id]  == "undefined") { 
      if(item.iso_language_code == "en") { 
        this.pushObject(item);
        this.idArray[id] = item.id;
        Example.Item.create({ name: item.text });
      }
    };
  },
  getTweets: function() { 
    var self = this;
    var searchString = Example.get("searchString");
    var url = "http://search.twitter.com/search.json?callback=?&q=" + searchString;
    $.getJSON(url, function(data) { 
      for (var i = 0; i < data.results.length; i++) { 
        self.addItem(Example.Item.create(data.results[i]));
      };
    })
  }.observes("Example.searchString")
});
