/**
 * Created by Owner on 5/20/2019.
 */
function search(){
    /*
    * search github api
    * */
    document.querySelector('.loading').style.display = 'block';
    window.location = $('#sea').val();
}
$('#search').on('click', ()=>{
    search();
});
document.addEventListener('keyup', (event)=>{
    if(event.which === 13 || evet.key === 13)
    {
        search();
    }
});