$ ->
  # General adaptiveBackground execution.
  # For coloring the backgrounds of any bumpers, etc.
  $.adaptiveBackground.run
    parent: ".game"

  # Specific adaptiveBackground execution.
  $(".game-image img").on "ab-color-found", (ev, payload) ->
    $(this).closest('.game').find('.game-metadata-marker').css('background-color', payload.color)

  # Partciles for great justice!
  particlesJS "particles-js",
    particles:
      color: "#090d12"
      shape: "circle" # "circle", "edge" or "triangle"
      opacity: 1
      size: 3
      size_random: true
      nb: 200
      line_linked:
        enable_auto: true
        distance: 75
        color: "#090d12"
        opacity: 1
        width: 1
        condensed_mode:
          enable: true
          rotateX: 600
          rotateY: 600

      anim:
        enable: true
        speed: 1

    # We can't even click this thing inside of the browser
    # plogin, so turn this off.
    interactivity:
      enable: false

    # Retina Display Support.
    retina_detect: true
