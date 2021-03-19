import json
import unittest

from src.api.helpers import add_podcast
from src.api.tests.base import BaseTestCase


class TestAudioBook(BaseTestCase):
    """Tests for the audio file type 'Audiobook'."""

    def test_add_valid_podcast(self):
        """Ensure a new audiobook audio file type can be added to the database
        and store participants as none"""
        with self.client:
            response = self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'podcast',
                    'audioFileMetadata': {
                        'name': 'Python Daily',
                        'duration': 300,
                        'host': 'Dan Bader',
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 200)
            self.assertIn('Python Daily', data['message'])
            self.assertIn('success', data['status'])

        print("\n=============================================================")

    def test_add_valid_podcast_include_participants(self):
        """Ensure a new audiobook audio file type can be added to the database
        with participants"""
        with self.client:
            response = self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'podcast',
                    'audioFileMetadata': {
                        'name': 'Python Daily',
                        'duration': 300,
                        'host': 'Dan Bader',
                        'participants': {'fullname': ['Tolu', 'William', 'Kpoke']}
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 200)
            self.assertIn('Python Daily', data['message'])
            self.assertIn('success', data['status'])

        print("\n=============================================================")

    def test_add_podcast_invalid_json_values(self):
        """Ensure that an error is thrown if len(participant) > 10."""
        with self.client:
            response = self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'podcast',
                    'audioFileMetadata': {
                        'name': 'Python Daily',
                        'duration': 300,
                        'host': 'Dan Bader',
                        'participants': {'fullname': ['Tolu', 'Tola', 'Tobi', 'shawn', 'djaja', 'aajj',
                                                      'adhjha', 'dkasjd', 'djdh', 'asdha', 'ashj']}
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

        print("\n=============================================================")

    def test_specific_podcast(self):
        """Ensure get single podcast behaves correctly."""
        podcast = add_podcast('Python Daily', 300, 'Dan Bader')
        with self.client:
            response = self.client.get(f'/api/v1/audio/podcast/{podcast.id}/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('Python Daily', data['data']['name'])
            self.assertIn('success', data['status'])

        print("\n=============================================================")

    def test_all_podcasts(self):
        """Test that the endpoint returns all songs."""
        podcast = add_podcast('Python Daily', 300, 'Dan Bader')
        podcast = add_podcast('Proverbs Daily', 60, 'Toluwalemi', {'fullname': ['Tolu', 'William', 'Kpoke']})
        with self.client:
            response = self.client.get('/api/v1/audio/podcast/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['podcasts']), 2)

        print("\n=============================================================")

    def test_patch_podcast(self):
        """Test to update podcast json"""
        podcast = add_podcast('Python Daily', 300, 'Dan Bader')
        with self.client:
            response = self.client.patch(
                f'/api/v1/audio/podcast/{podcast.id}/',
                data=json.dumps({
                    'audioFileType': 'podcast',
                    'audioFileMetadata': {
                        'participants': {'fullname': ['Tolu', 'William', 'Kpoke']}
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 200)
            self.assertIn('Updated!', data['message'])
            self.assertIn('success', data['status'])

        print("\n=============================================================")


if __name__ == '__main__':
    unittest.main()
