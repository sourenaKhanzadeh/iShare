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
                let text = `
                    <section class="shadow-lg p-3 mb-5 bg-white rounded card md-3">
                <div class="d-flex">
                    <div  class="d-flex flex-column">
                        <div class="icon">
                                <img src="${data.avatar}">
                            <i style="font-size: 14pt" class="fas fa-star"><br><span style="font-size: 10pt">${data.stars}</span></i>
                            <br><br>
                        </div>
                        <a href="/Browse-all-time?section=${data.section}" class="query_sec btn btn-outline-primary">${data.section}</a>
                        <a class="git btn btn-primary btn-lg" href="${data.url_repo}"><i class="fab fa-github"></i></a>
                        <a class="pdf btn btn-secondary btn-lg" href="${data.url_pdf}"><i class="far fa-file-pdf"></i></a>
                    </div>
                    <div>
                        <img src="https://via.placeholder.com/225">
                    </div>
                    <div class="card-body d-flex flex-column">
                        <a class="title" href="/${data.user}/${data.title}">${data.title}</a>
                        <small class="text-muted">${data.date} by ${data.user}</small>
                        <p>${data.description}</p>
                    </div>
                </div>
                `;
                let tags = "<div class='tags'>";
                for(var i =0; i<data.tags.length;i++)
                    tags += `<a class="tag btn btn-outline-warning" href="/Browse-all-time?tag=${data.tags[i]}">${data.tags[i]}  </a>`;
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
                let text = `
                    <section class="shadow-lg p-3 mb-5 bg-white rounded card md-3">
                <div class="d-flex">
                    <div  class="d-flex flex-column">
                        <div class="icon">
                                <img src="${data.avatar}">
                            <i style="font-size: 14pt" class="fas fa-star"><br><span style="font-size: 10pt">${data.stars}</span></i>
                            <br><br>
                        </div>
                        <a href="/Browse-all-time?section=${data.section}" class="query_sec btn btn-outline-primary">${data.section}</a>
                        <a class="git btn btn-primary btn-lg" href="${data.url_repo}"><i class="fab fa-github"></i></a>
                        <a class="pdf btn btn-secondary btn-lg" href="${data.url_pdf}"><i class="far fa-file-pdf"></i></a>
                    </div>
                    <div>
                        <img src="https://via.placeholder.com/225">
                    </div>
                    <div class="card-body d-flex flex-column">
                        <a class="title" href="/${data.user}/${data.title}">${data.title}</a>
                        <small class="text-muted">${data.date} by ${data.user}</small>
                        <p>${data.description}</p>
                    </div>
                </div>
                
            `;

                let tags = "<div class='tags'>";
                for(var i =0; i<data.tags.length;i++)
                    tags += `<a  class="tag btn btn-outline-warning" href="/Browse-all-time?tag=${data.tags[i]}">${data.tags[i]}`;
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
