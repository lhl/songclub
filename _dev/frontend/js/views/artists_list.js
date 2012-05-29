(function() {

  define(['jQuery', 'Underscore', 'Backbone'], function($, _, Backbone) {
    var ArtistsListView;
    ArtistsListView = Backbone.View.extend({
      initialize: function() {
        return this.template = _.template($('#artists_list_template').html());
      },
      render: function() {
        var artist, artists, hit, source, term, _i, _len, _ref;
        artists = [];
        _ref = this.options.es_artist_hits;
        for (_i = 0, _len = _ref.length; _i < _len; _i++) {
          hit = _ref[_i];
          artist = {};
          source = hit._source;
          artist.name = source.name;
          artist.terms = ((function() {
            var _j, _len1, _ref1, _results;
            _ref1 = source.terms;
            _results = [];
            for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
              term = _ref1[_j];
              if (term.weight >= 0.8) {
                _results.push(term);
              }
            }
            return _results;
          })()).slice(0, 5);
          artists.push(artist);
        }
        $(this.el).html(this.template({
          artists: artists
        }));
        return this;
      }
    });
    return ArtistsListView;
  });

}).call(this);
