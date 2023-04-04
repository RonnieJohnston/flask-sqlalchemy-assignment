from src.models import db, Movie
class MovieRepository:

    def get_all_movies(self):
        #get all movies from the DB
        movie = Movie.query.all()
        return movie

    def get_movie_by_id(self, movie_id):
        #get a single movie from the DB using the ID
        movie = Movie.query.get(movie_id)
        return movie

    def create_movie(self, title, director, rating):
        #create a new movie in the DB
        movie = Movie(title = title, director = director, rating = rating)
        db.session.add(movie)
        db.session.commit()
        return movie

    def search_movies(self, title):
        #get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        movie = Movie.query.filter(Movie.title.ilike(f'%{title}%')).all()
        return movie


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
