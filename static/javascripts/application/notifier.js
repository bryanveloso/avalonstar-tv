(function() {
  var channel, delay, donated, hosted, poolDonating, poolHosting, poolSubscribing, pusher, running, setUp, soundDonation, soundSubStreak, soundSubscription, source, subscribed, substreaked, tearDown;

  delay = 5;

  running = false;

  poolDonating = 0;

  poolHosting = 0;

  poolSubscribing = 0;

  soundDonation = new Audio('/static/audio/donation.ogg');

  soundSubscription = new Audio('/static/audio/subscription.ogg');

  soundSubStreak = new Audio('/static/audio/substreak.ogg');

  setUp = function(payload) {
    console.log(payload.username + " is " + payload.action + "! Triggering setUp().");
    ($(".js-" + payload.action + " .js-username")).text(payload.username);
    ($(".js-" + payload.action)).addClass('active');
    ($(".js-square-" + payload.action)).addClass('visible');
    return ($('.js-square-flipper')).addClass('toggle');
  };

  tearDown = function(payload) {
    console.log('Triggering tearDown().');
    ($(".js-" + payload.action)).removeClass('active');
    ($(".js-square-" + payload.action)).removeClass('visible');
    return ($('.js-square-flipper')).removeClass('toggle');
  };

  subscribed = function(payload, resub, queued) {
    if (!running) {
      running = true;
      soundSubscription.volume = 0.4;
      soundSubscription.play();
      ($('.js-subscribing .js-type')).text(payload.title);
      if (resub) {
        ($('.js-subscribing .js-message')).text('Welcome back to the Crusaders!');
      } else {
        ($('.js-subscribing .js-message')).text('Welcome to the Crusaders!');
      }
      setUp(payload);
      return setTimeout((function() {
        tearDown(payload);
        running = false;
        if (poolSubscribing >= 1) {
          poolSubscribing--;
          return console.log("There are " + poolSubscribing + " subs left in the pool.");
        }
      }), 6900);
    } else {
      if (!queued) {
        poolSubscribing++;
        console.log("There are " + poolSubscribing + " subs left in the pool.");
      }
      return setTimeout((function() {
        console.log("Running the pool subscription for, " + payload.username + ".");
        return subscribed(payload, resub, true);
      }), delay * 1000);
    }
  };

  substreaked = function(payload, queued) {
    var length;
    if (!running) {
      running = true;
      soundSubStreak.volume = 0.4;
      soundSubStreak.play();
      length = payload.length === 1 ? 'month' : 'months';
      ($('.js-substreaking .js-months')).text(payload.length + " " + length);
      setUp(payload);
      return setTimeout((function() {
        tearDown(payload);
        running = false;
        if (poolSubscribing >= 1) {
          poolSubscribing--;
          return console.log("There are " + poolSubscribing + " subs left in the pool.");
        }
      }), 6900);
    } else {
      if (!queued) {
        poolSubscribing++;
        console.log("There are " + poolSubscribing + " subs left in the pool.");
      }
      return setTimeout((function() {
        console.log("Running the pool subscription for, " + payload.username + ".");
        return substreaked(payload, true);
      }), delay * 1000);
    }
  };

  donated = function(payload, queued) {
    if (!running && poolSubscribing === 0) {
      running = true;
      soundDonation.volume = 0.4;
      soundDonation.play();
      setUp(payload);
      return setTimeout((function() {
        tearDown(payload);
        running = false;
        if (poolDonating >= 1) {
          poolDonating--;
          return console.log("There are " + poolDonating + " donators left in the pool.");
        }
      }), 6900);
    } else {
      if (!queued) {
        poolDonating++;
        console.log("There are " + poolDonating + " donators left in the pool.");
      }
      return setTimeout((function() {
        console.log("Running the pool donation for, " + payload.username + ".");
        return donated(data, true);
      }), delay * 1000);
    }
  };

  hosted = function(payload) {
    if (!running && poolSubscribing === 0 && poolDonating === 0) {
      running = true;
      setUp(payload);
      return setTimeout((function() {
        tearDown(payload);
        return running = false;
      }), 6900);
    } else {
      return setTimeout((function() {
        return hosted(payload);
      }), delay * 1000);
    }
  };

  pusher = new Pusher('207f2c96da3bdb9301f8');

  channel = pusher.subscribe('live');

  channel.bind('subscribed', function(data) {
    var payload;
    payload = {
      'action': 'subscribing',
      'title': 'Subscription',
      'username': data.username
    };
    return subscribed(payload, false, false);
  });

  channel.bind('resubscribed', function(data) {
    var payload;
    payload = {
      'action': 'subscribing',
      'title': 'Resubscription',
      'username': data.username
    };
    return subscribed(payload, true, false);
  });

  channel.bind('substreaked', function(data) {
    var payload;
    payload = {
      'action': 'substreaking',
      'username': data.username,
      'length': data.length
    };
    return substreaked(payload, false);
  });

  channel.bind('hosted', function(data) {
    var payload;
    payload = {
      'action': 'hosting',
      'username': data.username
    };
    return hosted(payload);
  });

  channel.bind('donated', function(data) {
    var payload;
    payload = {
      'action': 'donating',
      'amount': data.amount,
      'username': data.username
    };
    return donated(payload, false);
  });

  source = new EventSource("https://imraising.tv/api/v1/listen?apikey=nuZOkYmLF37yQJdzNLWLRA");

  source.addEventListener('donation.add', function(e) {
    var data, payload;
    data = JSON.parse(e.data);
    payload = {
      'action': 'donating',
      'amount': data.amount,
      'username': data.nickname
    };
    return donated(payload, false);
  });

}).call(this);
