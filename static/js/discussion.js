/**
 * Created by Sourena Khanzadeh on 6/5/2019.
 */
$('#comment').on('click',()=>{
    let comment = $('.msg textarea').val();
    //preventing sql injection
    comment = comment.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    $('textarea').val('');
    $('.loading').fadeIn(1000);

    $.ajax({
        type: "GET",
        cache: false,
        data:{today:today, user:user, comment:comment},
        url: window.location,
        dataType: "json",
        success: function(data) {
            console.log(data);
            // sent message
            $('.msg area').prepend(`
            <div class="card mb-3">
                      <div class="row no-gutters">
                        <div class="col-md-2">

                        </div>
                        <div class="col-md-8">
                          <div class="card-body">
                            <h5 class="card-title">${ data.username}</h5>
                            <p class="card-text">${data.comment}</p>
                            <p class="card-text"><small class="text-muted">${data.date}</small></p>
                          </div>
                        </div>
                      </div>
                    </div>
            `);

        },
        // error: function(jqXHR) {
        //     alert("error: " + jqXHR.status);
        //     console.log(jqXHR);
        // }
        }).done((data)=>{
            // fade out the pre loader after 1sec
            $('.loading').fadeOut(1000);



    });

});
