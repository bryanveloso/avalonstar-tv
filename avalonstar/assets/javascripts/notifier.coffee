# These are inspired by JewSanta's work on Main Menu's overlays. Originally
# supposed to be written in Ember, but I couldn't figure out how to get pools
# working in its very rigid structure. So here it is.

# Variables.
delay = 5               # Delay before looping, in seconds.
running = false         # Are we running any alerts?
poolDonating = 0        # How many users are in the donation pool?
poolHosting = 0         # How many users are in the hosting pool?
poolSubscribing = 0     # How many users are in the subscription pool?

# Sounds.
soundDonation = new Audio('/static/audio/donation.ogg')
soundSubscription = new Audio('/static/audio/subscription.ogg')

# Convenience functions.
setUp = (payload) ->
  console.log "#{payload.username} is #{payload.action}! Triggering setUp()."

  ($ ".js-#{payload.action} .js-username").text(payload.username)
  ($ ".js-#{payload.action}").addClass('active')
  ($ ".js-square-#{payload.action}").addClass('visible')
  ($ '.js-square-flipper').addClass('toggle')

tearDown = (payload) ->
  console.log 'Triggering tearDown().'

  ($ ".js-#{payload.action}").removeClass('active')
  ($ ".js-square-#{payload.action}").removeClass('visible')
  ($ '.js-square-flipper').removeClass('toggle')

subscribed = (payload, resub, added) ->
  if not running
    running = true

    # Play the subscription beat!
    soundSubscription.volume = 0.4
    soundSubscription.play()

    # If the user has subscribed at least once before, they're considered a
    # resubscriber. We use the same rail to greet them, but the text is
    # changed slightly to welcome them back.
    ($ '.js-subscribing .js-type').text(payload.title)
    ($ '.js-subscribing .js-message').text('Welcome back to the Crusaders!') if resub

    setUp(payload)
    setTimeout (->
      tearDown(payload)
      running = false
      if poolSubscribing >= 1
        poolSubscribing--
        console.log "There are #{poolSubscribing} subs left in the pool."
    ), 6900
  else
    if not added
      poolSubscribing++
      console.log "There are #{poolSubscribing} subs left in the pool."
    setTimeout (->
      console.log "Running the pool subscription for, #{payload.username}."
      subscribed(payload, resub, true)
    ), (delay * 1000)

donated = (payload, added) ->
  if not running and poolSubscribing is 0
    running = true

    # Play the donation beat!
    soundDonation.volume = 0.4
    soundDonation.play()

    setUp(payload)
    setTimeout (->
      tearDown(payload)
      running = false
      if poolDonating >= 1
        poolDonating--
        console.log "There are #{poolDonating} donators left in the pool."
    ), 6900
  else
    if not added
      poolDonating++
      console.log "There are #{poolDonating} donators left in the pool."
    setTimeout (->
      console.log "Running the pool donation for, #{payload.username}."
      donated(data, true)
    ), (delay * 1000)

hosted = (payload) ->
  if not running and poolSubscribing is 0 and poolDonating is 0
    running = true
    setUp(payload)
    setTimeout (->
      tearDown(payload)
      running = false
    ), 6900
  else
    setTimeout (->
      hosted(payload)
    ), (delay * 1000)

# Pusher actions.
pusher = new Pusher('207f2c96da3bdb9301f8')
channel = pusher.subscribe('live')

channel.bind 'subscribed', (data) ->
  payload =
    'action': 'subscribing'
    'title': 'Subscription'
    'username': data.username
  subscribed(payload, false, false)

channel.bind 'resubscribed', (data) ->
  payload =
    'action': 'subscribing'
    'title': 'Resubscription'
    'username': data.username
  subscribed(payload, true, false)

channel.bind 'substreak', (data) ->
  payload =
    'action': 'resubscribing'
    'username': data.username
    'length': data.length
  substreaked(payload, false)

channel.bind 'hosted', (data) ->
  payload =
    'action': 'hosting'
    'username': data.username
  hosted(payload)

# imraising.tv actions.
source = new EventSource("https://imraising.tv/api/v1/listen?apikey=nuZOkYmLF37yQJdzNLWLRA")
source.addEventListener 'donation.add', (e) ->
  data = JSON.parse(e.data)
  payload =
    'action': 'donating'
    'amount': data.amount
    'username': data.nickname
  donated(payload, false)
