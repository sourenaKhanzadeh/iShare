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
            let text = `<section>
                <a href="/${data.username}/${data.title}"><h1>${data.title}</h1></a>
                <h4>on ${data.date} by ${data.username}</h4>
                <p>${data.description}</p>
                <div>
                    <img src="${data.avatar}">
                    <i class="fa fa-star">${data.stars}</i>
                    <a class="git" href="${data.url_repo}"><i class="fab fa-github"></i></a>
                    <a class="pdf" href="${data.url_pdf}"><i class="far fa-file-pdf"></i></a>
                </div>
                <div class="sections">
                    <a  href="/Browse-all-time?section=${data.section}">${data.section}</a>
                </div>
            `;
            let tags = "<div class='tags'>";
            for(var i =0; i<data.tags.length;i++)
                tags += `<a href="/Browse-all-time?tag=${data.tags[i]}">${data.tags[i]}`;
            tags += "</div>";

            text += tags;
             text += `
                <div class="admin__btn">
                    <button onclick="window.location='/${data.admin}/edit/${data.title}'"> Edit </button>
                    <button onclick="window.location='/${data.admin}/delete/${data.title}'"> Delete </button>
                </div>
                    </section>`;
           $('.query').append(
                text
            );
        }
        if(data.admin){
            let text = `<section>
            <a href="/${data.username}/${data.title}"><h1>${data.title}</h1></a>
            <h4>on ${data.date} by ${data.username}</h4>
            <p>${data.description}</p>
            <div>
                <img src="${data.avatar}">
                <i class="fa fa-star">${data.stars}</i>
                <a class="git" href="${data.url_repo}"><i class="fab fa-github"></i></a>
                <a class="pdf" href="${data.url_pdf}"><i class="far fa-file-pdf"></i></a>
            </div>
            <div class="sections">
                    <a  href="/Browse-all-time?section=${data.section}">${data.section}</a>
            </div>
            
        `;

            let tags = "<div class='tags'>";
            for(var i =0; i<data.tags.length;i++)
                tags += `<a href="/Browse-all-time?tag=${data.tags[i]}">${data.tags[i]}`;
            tags += "</div>";

            text += tags;
            text += `
                <div class="admin__btn">
                    <button onclick="window.location='/${data.admin}/edit/${data.title}'"> Edit </button>
                    <button onclick="window.location='/${data.admin}/delete/${data.title}'"> Delete </button>
                </div>
                    </section>`;
            $('.query').append(text);

        }
    })
});
