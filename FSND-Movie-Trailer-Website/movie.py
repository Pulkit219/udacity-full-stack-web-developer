import media
import fresh_tomatoes

matrix_1 = media.Movie(
    movie_title="The Matrix (1999)",
    poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_.jpg",
    trailer_youtube_url="https://www.youtube.com/watch?v=vKQi3bBA1y8"
)

matrix_2 = media.Movie(
    movie_title="The Matrix Reloaded (2003)",
    poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTkzNzI3NzQxMV5BMl5BanBnXkFtZTYwOTI2NTY3._V1_.jpg",
    trailer_youtube_url="https://www.youtube.com/watch?v=zmYE3tg26Qc"
)

matrix_3 = media.Movie(
    movie_title="The Matrix Revolutions (2003)",
    poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTkyNjc4NTQzOV5BMl5BanBnXkFtZTcwNDYzMTQyMQ@@._V1_.jpg",
    trailer_youtube_url="https://www.youtube.com/watch?v=psNlHckYlVs"
)

if __name__ == "__main__":
    movies = [matrix_1, matrix_2, matrix_3]
    fresh_tomatoes.open_movies_page(movies)
