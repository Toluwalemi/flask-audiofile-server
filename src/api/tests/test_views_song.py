import json
import unittest

from src import db
from src.api.models import Song
from src.api.tests.base import BaseTestCase


class TestAudioService(BaseTestCase):
    """Tests for the audio service."""

    def test_add_valid_song(self):
        """Ensure a new audio file type can be added to the database"""
        with self.client:
            response = self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'song',
                    'audioFileMetadata': {
                        'name': 'hold_me_down',
                        'duration': 180,
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 200)
            self.assertIn('hold_me_down was added!', data['message'])
            self.assertIn('success', data['status'])

            print("\n=============================================================")

    def test_add_song_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty"""
        with self.client:
            response = self.client.post(
                '/api/v1/audio/',
                data=json.dumps({}),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

        print("\n=============================================================")

    def test_add_song_invalid_json_values(self):
        """Ensure that an error is thrown if duration is not a +ve integer"""
        with self.client:
            response = self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'song',
                    'audioFileMetadata': {
                        'name': 'hold_me_down',
                        'duration': 0,
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

        print("\n=============================================================")

        pass

    def test_add_duplicate_audio_file(self):
        """Ensure that an error is returned for a duplicate entry"""
        with self.client:
            self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'song',
                    'audioFileMetadata': {
                        'name': 'hold_me_down',
                        'duration': 180,
                    }
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'song',
                    'audioFileMetadata': {
                        'name': 'hold_me_down',
                        'duration': 180,
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 400)
            self.assertIn('This song already exists.', data['message'])
            self.assertIn('fail', data['status'])

        print("\n=============================================================")

    def test_specific_song(self):
        """Ensure get single song behaves correctly."""
        song = Song(name='hold_me_down', duration=180)
        db.session.add(song)
        db.session.commit()
        with self.client:
            response = self.client.get(f'/api/v1/audio/song/{song.id}/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('hold_me_down', data['data']['name'])
            self.assertIn('success', data['status'])

        print("\n=============================================================")

    def test_specific_song_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get(f'/api/v1/audio/song/huh/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 500)
            self.assertIn('Song does not exist', data['message'])
            self.assertIn('fail', data['status'])

        print("\n=============================================================")

    def test_specific_song_incorrect_id(self):
        """Ensure error is thrown if an id is incorrect."""
        with self.client:
            response = self.client.get(f'/api/v1/audio/song/404/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Song does not exist', data['message'])
            self.assertIn('fail', data['status'])

        print("\n=============================================================")



if __name__ == '__main__':
    unittest.main()
