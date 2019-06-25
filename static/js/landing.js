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

function search2() {
    document.querySelector('.loading').style.display = 'block';
    window.location = $('#sea2').val();

}
$('#search').on('click', ()=>{
    search2();
});
document.addEventListener('keyup', (event)=>{
    if(event.which === 13 || evet.key === 13)
    {
        search2();
    }
});

// second search
$('#search2').click(()=>{
    document.querySelector('.loading').style.display = 'block';
    let search = $('#sea').val();
    window.location = `/${search}`;
});






