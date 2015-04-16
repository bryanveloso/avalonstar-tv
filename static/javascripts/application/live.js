(function() {
  $(function() {
    $.adaptiveBackground.run({
      parent: '.game'
    });
    ($('.game-image img')).on('ab-color-found', function(ev, payload) {
      return $(this).closest('.game').find('.game-metadata-marker').css('background-color', payload.color);
    });
    return particlesJS('particles-js', {
      particles: {
        color: '#29384D',
        shape: 'circle',
        opacity: 0.5,
        size: 3,
        size_random: true,
        nb: 500,
        line_linked: {
          enable_auto: false,
          distance: 100,
          color: '#29384D',
          opacity: 0.9,
          width: 1,
          condensed_mode: {
            enable: true,
            rotateX: 600,
            rotateY: 600
          }
        },
        anim: {
          enable: true,
          speed: 1
        }
      },
      interactivity: {
        enable: false
      },
      retina_detect: true
    });
  });

  $(window).load(function() {
    ($('.loading-screen')).velocity({
      opacity: 0.01
    }, {
      duration: 1500
    });
    return setInterval((function() {
      $.getJSON(window.location.origin + "/api/tickets/", function(data) {
        var username;
        username = data[0].name;
        return ($('.message-text.js-subscriber')).text(username);
      });
      return $.getJSON("https://api.twitch.tv/kraken/channels/avalonstar?callback=?", function(data) {
        var game;
        game = data.game;
        return ($('.message-text.js-game')).text(game);
      });
    }), 5000);
  });

}).call(this);
