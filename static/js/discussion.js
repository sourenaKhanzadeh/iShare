/**
 * Created by Sourena Khanzadeh on 6/5/2019.
 */
$('#comment').on('click',()=>{
    let comment = $('.msg textarea').val();

    // sent message
    $('.msg ul').append(`
    <h3>${user}</h3>
    <h5>${today}</h5>
    <li>${comment}</li>
    `);
    $('textarea').val('');

    $.ajax({
        type: "GET",
        cache: false,
        data:{today:today, user:user, comment:comment},
        url: window.location,
        dataType: "json",
        success: function(data) {
            console.log(data);

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
