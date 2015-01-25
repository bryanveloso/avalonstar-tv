# These are inspired by JewSanta's work on Main Menu's overlays. Originally
# supposed to be written in Ember, but I couldn't figure out how to get pools
# working in its very rigid structure. So here it is.

# Variables.
delay = 5               # Delay before looping.
running = false         # Are we running any alerts?
poolDonating = 0        # How many users are in the donation pool?
poolHosting = 0         # How many users are in the hosting pool?
poolSubscribing = 0     # How many users are in the subscription pool?

subscribed = (data, added)->
  if not running
    console.log "#{data.username} has subscribed!"
    running = true

    # Add the .visible class to .js-subscribed to kick off the animation set.
    # It's a self-contained animation, so there's no need to do much else.
    if poolSubscribing >= 1
      ($ '.js-type').text('Subscription Streak')
    else
      ($ '.js-type').text('Subscription')

    ($ '.js-username').text(data.username)
    ($ '.js-subscribed').addClass('visible')

    # Set a timeout (6000ms) equal to that of the entire reveal animation.
    setTimeout (->
      ($ '.js-subscribed').removeClass('visible')
      running = false
      if poolSubscribing >= 1
        poolSubscribing--
        console.log "There are #{poolSubscribing} subs left in the pool."
    ), 6000
  else
    if not added
      poolSubscribing++
      console.log "There are #{poolSubscribing} subs left in the pool."
    setTimeout (->
      console.log "Running the pool subscription for, #{data.username}."
      subscribed(data, true)
    ), (delay * 1000)


Pusher.log = (message) ->
  window.console.log message  if window.console and window.console.log
  return

pusher = new Pusher('207f2c96da3bdb9301f8')
channel = pusher.subscribe('live')

channel.bind 'subscribed', (data) ->
  subscribed(data, false)
