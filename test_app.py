import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actors, Movies

DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '123')
DB_NAME = os.getenv('DB_NAME', 'Agency')
database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

new_movie = {
    'title': 'Sonic: The Hedgehog',
    'genre': 'Fantasy',
    'release_date': '2018.01.05'
}

new_actor = {
    'name': 'Jim Carrey',
    'age': '41',
    'role': 'Anime',
    'gender': 'Male'
}


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)
        self.assistance_token = 'Bearer' + str(os.getenv('assistant'))
        self.director_token = 'Bearer' + str(os.getenv('director'))
        self.producer_token = 'Bearer' + str(os.getenv('producer'))

        self.assistant = {'Authorization': self.assistance_token}
        self.director = {'Authorization': self.director_token}
        self.producer = {'Authorization': self.producer_token}
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()


    def tearDown(self):
        pass

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['len_movies'])

    def test_movies_by_using_id(self):
        res = self.client().get('/movies/2', headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_post_movies(self):
        res = self.client().get('/movies', json=new_movie, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'The Movie is successfully created')

    def test_post_movies_invalid(self):
        new_movie_error = {
            'title': 'Birds of prey',
            'release_date': '2020.07.26'
        }
        res = self.client().post('/movies', json=new_movie_error, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable Request")

    def test_delete_movie_by_id(self):
        res = self.client().delete('/movies/5', headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'The Movie is successfully deleted')

    def test_invalid_delete_movies(self):
        res = self.client().delete('/movies/me', headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_search_movie(self):
        search_item = {'searchTerm': 'a'}
        res = self.client().post('/movies/search', json=search_item, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['len_movies'])

    def test_search_movie_invalid(self):
        new_search = {'searchTerm': ''}
        res = self.client().post('/movies/search', json=new_search, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_patch_movie(self):
        patch_title = {'title': 'Mr.Smith'}
        res = self.client().patch('/movies/4', json=patch_title, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'The Movie Successfully updated!')

    def test_patch_movie_invalid(self):
        patch_title = {'err_title': 'Hello'}
        res = self.client().patch('/movies/4', json=patch_title, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable Request")

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['len_actors'])

    def test_actors_by_using_id(self):
        res = self.client().get('/actors/2', headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_post_actors(self):
        res = self.client().get('/actors', json=new_actor, headers=self.director)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'The Actor is successfully created')

    def test_post_actors_invalid(self):
        new_actor_error = {
            'name': 'Jim Carrey',
            'age': '34'
        }
        res = self.client().post('/actors', json=new_actor_error, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable Request")

    def test_delete_actor_by_id(self):
        res = self.client().delete('/actors/3', headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'The Actors is successfully deleted')

    def test_invalid_delete_actors(self):
        res = self.client().delete('/actors/me', headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_search_actor(self):
        search_item = {'searchTerm': 'a'}
        res = self.client().post('/actors/search', json=search_item, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['len_actors'])

    def test_search_actor_invalid(self):
        new_search = {'searchTerm': ''}
        res = self.client().post('/actors/search', json=new_search, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_patch_actor(self):
        patch_title = {'name': 'Mr.Smith'}
        res = self.client().patch('/actors/1', json=patch_title, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'The Actor Successfully updated!')

    def test_patch_actor_invalid(self):
        patch_title = {'err_name': 'Hello'}
        res = self.client().patch('/actors/1', json=patch_title, headers=self.producer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable Request")

if __name__ == "__main__":
    unittest.main()
