var hiddenBox = $(".banner-message");
var page = 1;
var movie_list = new Map();
var selected_movies = new Map();

class Movie {
    constructor(movie) {
        this.id = movie.id;
        this.name = movie.name;
        this.rating = movie.rating;
    }
}

function select(movie_id) {
    let movie = movie_list.get(movie_id);
    movie_list.delete(movie_id);
    selected_movies.set(movie_id, movie);
    renderMovie();
}

function renderMovie() {
    $("#page-btn").html(String(page));
    $(".list").html("");
    movie_list.forEach(function(movie) {
        $(".list").append(`<div class="movie" id="movie-${movie.id}">
            <p>${movie.name} &nbsp </p>
        </div>`);
        $(`#movie-${movie.id}`).on("click", () => {
            select(movie.id);
        });
    });
    $(".selected-list").html("");
    selected_movies.forEach(function(movie) {
        $(".selected-list").append(`<div class="movie" id="movie-${movie.id}">
                <p>${movie.name} &nbsp rating:<input type="number" name="rating-${movie.id}" max="5" min="1" value="${movie.rating}" id="movie-rating-${movie.id}"></p>
            </div>`);
    });
}

function serialize(movies) {
    movie_list.clear();
    movies.forEach(function(movie) {
        if (!selected_movies.has(movie.id))
            movie_list.set(movie.id, new Movie(movie));
    });
}



function getMovies() {
    $.ajax({
        url: "/get_movies",
        data: {
            'page': page
        },
        success: function(result) {
            if (result.movies.length == 0) {
                page = 1;
                getMovies();
            } else {
                serialize(result.movies);
            }
            renderMovie();
        }
    });
}

$("#pre-btn").on("click", () => {
    if (page > 1)
        page--;
    getMovies();
});

$("#next-btn").on("click", () => {
    page++;
    getMovies();
});
$("#page-btn").on("click", () => {
    getMovies();
});

$("#search").on("click", () => {
    search_text = $("#search-tab").val();
    $.ajax({
        url: "/search",
        data: {
            search_text
        },
        success: (result) => {
            if (result.movies.list == 0) {
                $(".list").html("<p>No data found</p>");
            } else {
                console.log(result);
                serialize(result.movies);
                renderMovie();
            }
        }
    })
});

function parse_selected_movies() {

    selected_movies.forEach((movie) => {
        let tmp = $(`#movie-rating-${movie.id}`).val();
        if (tmp in [1, 2, 3, 4, 5]) {
            movie.rating = tmp;
        } else
            return false;
    });
    return true;
}


$("#send-btn").on("click", () => {
    let list = new Array();
    let err = false;
    if (parse_selected_movies()) {
        selected_movies.forEach((movie) => {
            if (movie.rating in [1, 2, 3, 4, 5])
                list.push({ movie: movie.id, rating: movie.rating });
            else
                err = true;
        });
        if (err) {
            $("#error").html("Rating should be between 1 to 5");
            return;
        }
        req = {
            movies: list,
            csrfmiddlewaretoken: $(".form-csrf input").val()
        }

        $.ajax({
            url: '/recommend',
            method: 'post',
            data: req,
            success: (result) => {
                alert(`message recieved - ${result}`);
            }
        });



    } else {
        $("#error").html("Enter rating to all selected movies (1 to 5)");
    }

});
getMovies();