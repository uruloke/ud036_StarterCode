from media import Movie
from fresh_tomatoes import open_movies_page

movies = [Movie(
    "Avatar (2009)",
    "https://i.imgur.com/2gRowGS.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
), Movie(
    "Spirit: Stallion of the Cimarron (2002)",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgyOTUzNDA1N15BMl5BanBnXkFtZTYwNjgwMDM3._V1_.jpg",
    "https://www.youtube.com/watch?v=-vGpe_8XiNk"
), Movie(
    "The Lion King (1994)",
    "https://i.imgur.com/JHWQQxO.png",
    "https://www.youtube.com/watch?v=4sj1MT05lAA"
)]

open_movies_page(movies)
