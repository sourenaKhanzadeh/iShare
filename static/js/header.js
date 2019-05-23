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

// post input
/**
 * sends a request to the specified url from a form. this will change the window location.
 * @param {string} path the path to send the post request to
 * @param {object} params the paramiters to add to the url
 * @param {string} [method=post] the method to use on the form
 */

function post(path, params, method='post') {

  // The rest of this code assumes you are not using a library.
  // It can be made less wordy if you use one.
  const form = document.createElement('form');
  form.method = method;
  form.action = path;

  // get keys of parameters
  for (const key in params) {
    // if key in params
    if (params.hasOwnProperty(key)) {
      // create a hidden input and append it
      const hiddenField = document.createElement('input');
      hiddenField.type = 'hidden';
      hiddenField.name = key;
      hiddenField.value = params[key];

      form.appendChild(hiddenField);
    }
  }
  // append to body
  document.body.appendChild(form);
  // submit form
  form.submit();
}


window.onscroll = function(ev) {
    /*
    * window on scroll
    * */
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        // you're at the bottom of the page

    }
};