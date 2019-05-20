/**
 * Created by Owner on 5/20/2019.
 */
// get DOM'S
const bar = document.querySelector('#menu');
const nav = $('nav');
const nav_right = $('.nav-right');

$('#logout').on('click',()=>{
    window.location = '/account/logout';
});
function preload(){
    $('.loading').css('display', 'block');
}


bar.addEventListener('click', ()=>{
    let css = {
        'display':'flex',
        'flex-direction':'column'
    };
    $('nav ul').css(css);
    nav.css('height','200px');
    setTimeout(remove, 4000);
});

function defaultNav(){
    let css = {
        'display':'block'
    };
    $('nav ul').css(css);

    nav.css('height', '50px');
}

function remove(){
    defaultNav();
    $('nav ul').css('display', 'none');
}

//media query if media 800px
let media = window.matchMedia('(min-width: 800px)');
media.addListener(defaultNav);