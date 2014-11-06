$ ->
  # General adaptiveBackground execution.
  # For coloring the backgrounds of any bumpers, etc.
  $.adaptiveBackground.run
    parent: ".game"

  # Specific adaptiveBackground execution.
  $(".game-image img").on "ab-color-found", (ev, payload) ->
    $(this).closest('.game').find('.game-metadata-marker').css('background-color', payload.color)
