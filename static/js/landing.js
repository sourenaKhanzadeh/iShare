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

// second search
$('#search2').click(()=>{
    document.querySelector('.loading').style.display = 'block';
    let search = $('#sea').val();
    window.location = `/${search}`;
});






