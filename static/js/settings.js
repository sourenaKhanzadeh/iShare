/**
 * Created by Owner on 6/13/2019.
 */
let dis_value = document.querySelector('.settings #btn_dis').checked ? 1:0;
let wave_value = document.querySelector('.settings #btn_wave').cheked ? 1:0;


function toggle(id, btn_value) {
    let check_box = document.querySelector(`.settings #${id}`);
    let btn = document.querySelector(`.settings .checkbox #btn_${id}`);
    // deactivate the button and checkbox if is already set
    // to active
   if(check_box.classList.contains('active')){
       check_box.classList.add('deactive');
       check_box.classList.remove('active');
       btn.classList.add('btn_deactive');
       btn.classList.remove('btn_active');
       btn_value = 0;
   }
   // activate the button and checkbox
   else{
       check_box.classList.add('active');
       check_box.classList.remove('deactive');
       btn.classList.add('btn_active');
       btn.classList.remove('btn_deactive');
       btn_value = 1;
   }
   return btn_value
}
// if dis button is clicked
document.querySelector('.settings #dis').addEventListener('click', ()=>{
    dis_value = toggle('dis', dis_value);
});


// if wave button is clicked
document.querySelector('.settings #wave').addEventListener('click', ()=>{
    wave_value = toggle('wave', wave_value);
});

// get email and password

// if save is clicked
document.querySelector('#save').addEventListener('click',()=>{
    let email = $('#email').val();
    let email_pass = $('#email_pass').val();
    let title = $('#title').val();
    let max_tags = $('#max_tags').val();
    let settings_i = $('.settings i');

    settings_i.css('display', 'block');
    settings_i.fadeOut(1000);
    // $('.loading').css('display', 'block');
    $.ajax({
        type: "GET",
        cache: false,
        data:{
            wave: document.querySelector('.settings #btn_wave').checked ? 1:0,
            dis: document.querySelector('.settings #btn_dis').checked ? 1:0,
            admin_email:email,
            admin_pass: email_pass,
            web_title: title,
            max_tags:max_tags
        },
        url: window.location,
        dataType: "json",
        success: function(data) {

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

