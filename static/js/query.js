/**
 * Created by Sourena Khanzadeh on 5/23/2019.
 */

let limit = 2;

window.addEventListener('scroll', ()=>{


// $('#load_more').click(()=>{
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        // you're at the bottom of the page


        limit++;
        $('.loading').css('display', 'block');
        $.ajax({
            type: "GET",
            cache: false,
            data:{limit:limit},
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
            if (data === null)
                $('#load_more').css('display', 'none');

            // if query does not exits destroy load_more
            if(data.queries_count === 0)
                $('#load_more').fadeOut(1000);

            // check if more data exist
            if(data.limit >= data.queries_count || data.limit === 2)
                // if not then fade the load more button
                $('#load_more').fadeOut(1000);
            // check if user is approved
            if (data.approved && data.admin === undefined){
                let text = `<section class="shadow-lg p-3 mb-5 bg-white rounded card md-3">
                    <div class="row no-gutters">
                        <div class="col-md-4">
                            <img class="card-img" src="${data.avatar}">
                        </div>
                    </div>
                    <div class="col-md-12">
                        <div class="card-body">
    
                            <a href="/${data.username}/${data.title}"><h1>${data.title}</h1></a>
                            <small class="text-muted">on ${data.date} by ${data.username}</small>
                            <p>${data.description}</p>
                            <div>
                                <i class="fa fa-star">${data.stars}</i>
                                <a class="git btn btn-lg btn-primary" href="${data.url_repo}"><i class="fab fa-github"></i></a>
                                <a class="pdf btn btn-lg btn-secondary" href="${data.url_pdf}"><i class="far fa-file-pdf"></i></a>
                            </div>
                            <div class="sections">
                                <a  class="btn btn-outline-primary" href="/Browse-all-time?section=${data.section}">${data.section}</a>
                             
                            </div>
                `;
                let tags = "<div class='tags'>";
                for(var i =0; i<data.tags.length;i++)
                    tags += `<a class="card-text btn btn-outline-warning" href="/Browse-all-time?tag=${data.tags[i]}">${data.tags[i]}  </a>`;
                tags += `   </div>
                        </div>
                        </div>`;

                text += tags;
                 text += `
                        </section>`;
               $('.query').append(
                    text
                );
            }
            if(data.admin){
                let text = `<section class="shadow-lg p-3 mb-5 bg-white rounded card md-3">
                <div class="row no-gutters">
                    <img class="card-img" src="${data.avatar}">
                </div>
                <div class="col-md-12">
                        <div class="card-body">
    
                        <a class="card-title" href="/${data.username}/${data.title}"><h1>${data.title}</h1></a>
                        <small class="text-muted">on ${data.date} by ${data.username}</small>
                        <p class="card-text">${data.description}</p>
                        <div>
                            <i class="fa fa-star">${data.stars}</i>
                            <a class="git btn btn-lg btn-primary" href="${data.url_repo}"><i class="fab fa-github"></i></a>
                            <a class="pdf btn btn-lg btn-secondary" href="${data.url_pdf}"><i class="far fa-file-pdf"></i></a>
                        </div>
                        <div class="sections">
                                <a class="card-text btn btn-outline-primary" href="/Browse-all-time?section=${data.section}">${data.section}</a>
                        </div>
                
            `;

                let tags = "<div class='tags'>";
                for(var i =0; i<data.tags.length;i++)
                    tags += `<a  class="card-text btn btn-outline-warning" href="/Browse-all-time?tag=${data.tags[i]}">${data.tags[i]}`;
                tags += "</a></div>";

                text += tags;
                text += `
                            <div class="admin__btn">
                                <button class="btn btn-outline-info" onclick="window.location='/${data.admin}/edit/${data.title}'"> Edit </button>
                                <button class="btn btn-outline-danger" onclick="window.location='/${data.admin}/delete/${data.title}'"> Delete </button>
                            </div>
                        </div>
                    </div>
                        </section>`;
                $('.query').append(text);

            }
        })
    }
// });
});
