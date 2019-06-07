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
            $('.msg ul').append(`
            <h3>${data.username}</h3>
            <h5>${data.date}</h5>
            <li>${data.comment}</li>
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
