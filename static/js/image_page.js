$("#b_style").on("click", function() {
  if( $('.material-icons').html() === "favorite_border"){ // Change the icon on click.
    $('.material-icons').html("favorite")
  }
  else {
    $('.material-icons').html("favorite_border")
  }

})

$(document).on('submit','#fav_form',function(e){ // Submit the form.
  var img_id = $("#image_id").html()
  e.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/gallery/'+ img_id,
            data: {
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    fav:$('.material-icons').html(),
                  }
        });


    });
