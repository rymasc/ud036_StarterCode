import media
import fresh_tomatoes

# movie image urls
manOnFireIMG = "https://m.media-amazon.com/images/M/MV5BODFlMmEwMDgtYjhmZi00ZTE5LTk2NWQtMWE1Y2M0NjkzOGYxXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,679,1000_AL_.jpg"  # noqa
lastOfTheMohicansIMG = "https://m.media-amazon.com/images/M/MV5BZDNiYmRkNDYtOWU1NC00NmMxLWFkNmUtMGI5NTJjOTJmYTM5XkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg"  # noqa
thePatriotIMG = "https://m.media-amazon.com/images/M/MV5BMTkzMjE4ODU0MV5BMl5BanBnXkFtZTYwNTI2OTk2._V1_UX182_CR0,0,182,268_AL_.jpg"  # noqa
darkestHourIMG = "https://m.media-amazon.com/images/M/MV5BNTU4MjMwOTgyMV5BMl5BanBnXkFtZTgwODQzNjY2NDM@._V1_SY1000_SX675_AL_.jpg"  # noqa
elDoradoIMG = "https://m.media-amazon.com/images/M/MV5BY2FhMzhlYzMtZjNlYi00NTU2LWEyNjAtZDE2YjNlZjljMmQ4L2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,656,1000_AL_.jpg"  # noqa
fistfulOfDollarsIMG = "https://m.media-amazon.com/images/M/MV5BYjA1MGVlMGItNzgxMC00OWY4LWI4YjEtNTNmYWIzMGUxOGQzXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg"  # noqa

# movie trailer urls
manOnFireTrailer = "https://www.youtube.com/watch?v=rb-ZEBBKolc"
lastOfTheMohicansTrailer = "https://www.youtube.com/watch?v=yaQeVnN6pUc"
thePatriotTrailer = "https://www.youtube.com/watch?v=P5u1am7pmrw"
darkestHourTrailer = "https://www.youtube.com/watch?v=LtJ60u7SUSw"
elDoradoTrailer = "https://www.youtube.com/watch?v=Mrv-SgHgXlM"
fistfulOfDollarsTrailer = "https://www.youtube.com/watch?v=RFWYI5buWlY"

# Creation of movie objects
manOnFire = media.Movie("Man on Fire", manOnFireIMG, manOnFireTrailer)

lastOfTheMohicans = media.Movie("The Last of the Mohicans",
                                lastOfTheMohicansIMG, lastOfTheMohicansTrailer)

thePatriot = media.Movie("The Patriot", thePatriotIMG, thePatriotTrailer)

darkestHour = media.Movie("Darkest Hour", darkestHourIMG, darkestHourTrailer)

elDorado = media.Movie("El Dorado", elDoradoIMG, elDoradoTrailer)

fistfulOfDollars = media.Movie("A Fistful of Dollars", fistfulOfDollarsIMG,
                               fistfulOfDollarsTrailer)

movies = [manOnFire, lastOfTheMohicans, thePatriot, darkestHour, elDorado,
          fistfulOfDollars]

fresh_tomatoes.open_movies_page(movies)
