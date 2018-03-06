from media import Movie
from fresh_tomatoes import open_movies_page

# Create our list with movies.
movies = [Movie(
    "Avatar (2009)",
    "https://i.imgur.com/2gRowGS.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
), Movie(
    "Spirit: Stallion of the Cimarron (2002)",
    "https://i.imgur.com/Jenv8Jl.jpg",
    "https://www.youtube.com/watch?v=-vGpe_8XiNk"
), Movie(
    "The Lion King (1994)",
    "https://i.imgur.com/JHWQQxO.png",
    "https://www.youtube.com/watch?v=4sj1MT05lAA"
)]

# Generate the html website from the movies and open the page.
open_movies_page(movies)
