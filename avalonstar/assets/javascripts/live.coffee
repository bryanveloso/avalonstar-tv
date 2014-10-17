img = $('.game-image img')[0]

RGBaster.colors img,
  success: (payload) ->
    # You now have the payload.
    console.log payload.dominant
    console.log payload.secondary
    console.log payload.palette
    return
