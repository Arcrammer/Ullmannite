(($) ->
  $(window).on 'resize load', ->
    # Make the 'div's the same
    # height as the viewport
    $('.greeting').css 'height', $(window).height()

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

) jQuery
