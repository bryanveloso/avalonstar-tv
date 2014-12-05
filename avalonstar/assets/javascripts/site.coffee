$ ->
  # ...
  $container = $('.broadcast-list').isotope
    itemSelector: '.broadcast'
    masonry:
      isFitWidth: true

  # ...
  $container.imagesLoaded ->
    $container.isotope()
