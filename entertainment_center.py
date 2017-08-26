import media
import webbrowser
import fresh_tomatoes

dunkirk = media.Movie("Dunkirk",
                        "A film based on the evacuation of British and French soldiers from Dunkirk, France during WWII",
                        "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                        "https://www.youtube.com/watch?v=F-eMt3SrfFU","This is just a test", media.Movie.VALID_RATINGS[2])

gladiator = media.Movie("Gladiator",
                        "A betrayed general who fought for honour, justice and love in the Colosseum",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE","This is just a test2",media.Movie.VALID_RATINGS[3])


braveheart = media.Movie("Braveheart",
                        "A brave knight who fought for the freedom of his people and free them from tyranny",
                        "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                        "https://www.youtube.com/watch?v=wj0I8xVTV18","This is just a test3",media.Movie.VALID_RATINGS[2])


inception = media.Movie("Inception",
                        "A thief who steal corporate secrets by going into people's dream was given the task of planting an idea in a CEO's mind",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0","This is just a test4",media.Movie.VALID_RATINGS[1])

matrix = media.Movie("The Matrix",
                        "A world set in a dystopia future where humans are ruled and controlled by an enemy that is everywhere",
                        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=vKQi3bBA1y8","This is just a test5",media.Movie.VALID_RATINGS[2])

interstellar = media.Movie("Interstellar",
                        "A team of explorers who had to travel into the deep space to save mankind",
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                        "https://www.youtube.com/watch?v=2LqzF5WauAw","This is just a test6",media.Movie.VALID_RATINGS[1])

movies =[dunkirk,gladiator,braveheart,inception,matrix,interstellar]
fresh_tomatoes.open_movies_page(movies)
###media.Movie.VALID_RATINGS
###print (interstellar.overview)
