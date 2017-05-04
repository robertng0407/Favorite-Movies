import fresh_tomatoes
import media

# Favorite movies
ex_machina = media.Movie("Ex Machina",
                         "A young programmer is selected to participate "
                         "in a ground-breaking experiment in synthetic "
                         "intelligence by evaluating the human qualities "
                         "of a breath-taking humanoid A.I.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=EoQuVnKhxaM")
interstellar = media.Movie("Interstellar",
                         "A team of explorers travel through a wormhole "
                         "in space in an attempt to ensure humanity's survival.",
                         "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                         "https://www.youtube.com/watch?v=3WzHXI5HizQ")
fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way "
                         "to change his life, crosses paths with a "
                         "devil-may-care soap maker, forming an underground "
                         "fight club that evolves into something much, much more.",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")
shutter_island = media.Movie("Shutter Island",
                         "In 1954, a U.S. marshal investigates the "
                         "disappearance of a murderess who escaped "
                         "from a hospital for the criminally insane.",
                         "https://upload.wikimedia.org/wikipedia/en/a/a2/Shutter_Island_book_cover.jpg",
                         "https://www.youtube.com/watch?v=5iaYLCiq5RM")
limitless = media.Movie("Limitless",
                         "With the help of a mysterious pill that enables "
                         "the user to access 100 percent of his brain abilities, "
                         "a struggling writer becomes a financial wizard, but "
                         "it also puts him in a new world with lots of dangers.",
                         "https://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg",
                         "https://www.youtube.com/watch?v=jOLqNOfzus4")
the_hangover = media.Movie("The Hangover",
                         "Three buddies wake up from a bachelor party in Las Vegas, "
                         "with no memory of the previous night and the bachelor "
                         "missing. They make their way around the city in order "
                         "to find their friend before his wedding.",
                         "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                         "https://www.youtube.com/watch?v=tcdUhdOlz9M")

# Array of movies
movies = [ex_machina, interstellar, fight_club, shutter_island, limitless, the_hangover]

# Calling open_movies_page to create and open html file for movies
fresh_tomatoes.open_movies_page(movies)
