$(document).ready(function(){

  $('#input-text').on('submit', function(event){
    event.preventDefault();
    $form = $(this)

    $.ajax({
      method: "POST",
      url: "/texts",
      data: $form.serialize()
    })
    .done(function(response){
      $('#input-div').append(response)
    })
  })

  $('#test-data').on('click', function(event){
    $.ajax({
      method: "GET",
      url: "/texts"
    })
    .done(function(response){
      console.log(response)
    })
  })

})
