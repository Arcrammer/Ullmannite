(($) ->
  $(window).on 'resize load', ->
    # Make the 'div's the same
    # height as the viewport
    window_height = $(window).height()
    # if window_height <= 600
    #   $('.greeting').addClass 'short'
    #   $('.greeting').css 'height', '600px'
    # else
    #   $('.greeting').removeClass 'short'
    #   $('.greeting').css 'height', window_height

  $('.say-hello-button').click ->
    # Don't let 'body' scroll
    $('body').css 'overflow', 'hidden'
    $('.message-sender').css 'display', 'block'

  $('.close-button span, .viewport-overlay').click (e) ->
    e.stopPropagation()
    if e.target == this
      # The node clicked was one that should  Let 'body' scroll again
      $('body').css 'overflow', 'visible'
      $('.viewport-overlay').css 'display', 'none'

  if say_hello_form_needs_display
    $('.say-hello-button').click()
) jQuery
