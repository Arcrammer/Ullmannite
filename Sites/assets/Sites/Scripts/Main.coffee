(($) ->
  $(window).on 'resize load', ->
    $('.greeting').css 'height', $(window).height()
) jQuery
