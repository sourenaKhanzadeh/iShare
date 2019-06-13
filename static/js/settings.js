/**
 * Created by Owner on 6/13/2019.
 */

let dis_value = document.querySelector('.settings #dis').classList.contains('active') ? 1:0;
let wave_value = document.querySelector('.settings #wave').classList.contains('active') ? 1:0;

function toggle(id) {
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
}
// if dis button is clicked
document.querySelector('.settings #dis').addEventListener('click', ()=>{
    toggle('dis');
});


// if wave button is clicked
document.querySelector('.settings #wave').addEventListener('click', ()=>{
    toggle('wave');
});