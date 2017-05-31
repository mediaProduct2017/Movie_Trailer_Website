from media import Movie
from fresh_tomatoes import open_movies_page

# instantiate movie objects
avatar = Movie('Avatar',
               "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

kill_bill = Movie('Kill Bill',
                  "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
                  "https://www.youtube.com/watch?v=7kSuas6mRpk")

life_of_pi = Movie('Life of Pi',
                   "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
                   "https://www.youtube.com/watch?v=3mMN693-F3U")

harry_Potter = Movie('Harry Potter and the Goblet of Fire',
                     "https://upload.wikimedia.org/wikipedia/en/c/c9/Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",
                     "https://www.youtube.com/watch?v=3EGojp4Hh6I")

movies = [avatar, kill_bill, life_of_pi, harry_Potter]
open_movies_page(movies)
# generate an HTML file
