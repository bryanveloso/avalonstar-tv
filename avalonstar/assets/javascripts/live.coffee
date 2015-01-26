$ ->
  # General adaptiveBackground execution.
  # For coloring the backgrounds of any bumpers, etc.
  $.adaptiveBackground.run
    parent: '.game'

  # Specific adaptiveBackground execution.
  ($ '.game-image img').on 'ab-color-found', (ev, payload) ->
    $(this).closest('.game').find('.game-metadata-marker').css('background-color', payload.color)

  # Partciles for great justice!
  particlesJS 'particles-js',
    particles:
      color: '#29384D'
      shape: 'circle' # 'circle', 'edge' or 'triangle'
      opacity: 0.5
      size: 3
      size_random: true
      nb: 125
      line_linked:
        enable_auto: true
        distance: 100
        color: '#29384D'
        opacity: 0.9
        width: 1
        condensed_mode:
          enable: true
          rotateX: 600
          rotateY: 600

      anim:
        enable: true
        speed: 1.75

    # We can't even click this thing inside of the browser
    # plogin, so turn this off.
    interactivity:
      enable: false

    # Retina Display Support.
    retina_detect: true

# Fade the loading screen once the window is loaded.
# Hopefully this'll allow us to not have to use global sources.
$(window).load ->
  console.log 'loaded'
  ($ '.loading-screen').animate
    opacity: 0.25
  , 1500
