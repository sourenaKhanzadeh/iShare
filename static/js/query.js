/**
 * Created by Sourena Khanzadeh on 5/23/2019.
 */

let limit = 2;

$('#load_more').click(()=>{
    limit++;
    $('.loading').css('display', 'block');
    $.ajax({
                type: "GET",
                cache: false,
                data:{limit:limit},
                url: '/Browse-all-time',
                dataType: "json",
                success: function(data) {
                    console.log(data);
                },
                // error: function(jqXHR) {
                //     alert("error: " + jqXHR.status);
                //     console.log(jqXHR);
                // }
    }).done((data)=>{
        $('.loading').css('display', 'none');
        if(data.limit >= data.queries_count || data.limit === 2)
            $('#load_more').fadeOut(1000);
        if (data.approved){
            $('.query').append(
                `<section>
                <h1>${data.title}</h1>
                <h4>on ${data.date} by ${data.username}</h4>
                <p>${data.description}</p>
                <div>
                    <img src="${data.avatar}">
                    <i class="fa fa-star">${data.stars}</i>
                    <a class="git" href="${data.url_repo}"><i class="fab fa-github"></i></a>
                    <a class="pdf" href="${data.url_pdf}"><i class="far fa-file-pdf"></i></a>
                </div>
            </section>`
            )
        }
    })
});
