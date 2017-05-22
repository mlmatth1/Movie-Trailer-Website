import media
import fresh_tomatoes
# each ore class instances of the Movie class
back_to_the_future = media.Movie(
    "Back to the Future",
    "Marty McFly, who is sent back in time to 1955",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
    "https://www.youtube.com/watch?v=qvsgGtivCgs")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
hunger_games = media.Movie(
    "Hunger Games",
    "A really real reality show",
    "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://youtube/watch?v=PbA63a7H0bo")
bill_and_teds_excellent_adventure = media.Movie(
    "Bill and Teds Excellent Adventure",
    "Which two slackers travel through time"
    "for their high school history presentation",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Bill_%26_Ted.jpg",
    "https://youtu.be/q3fx6TugN7g")
matrix = media.Movie(
    "Matrix",
    "Awesome freakin flick",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://youtu.be/m8e-FF8MsqU")
spring_break = media.Movie(
    "Spring Break",
    "College students go to Fort Lauderdale for spring break",
    "https://upload.wikimedia.org/wikipedia/en"
    "/f/fb/Poster_of_the_movie_Spring_Break.jpg",
    "https://www.youtube.com/watch?v=bL1Er4-fTkc")
# list of the class instances of my favorite Movies
movies = [back_to_the_future, avatar, hunger_games,
          bill_and_teds_excellent_adventure, matrix, spring_break]
fresh_tomatoes.open_movies_page(movies)
