import json
import unittest

from src.api.tests.base import BaseTestCase


class TestAudioService(BaseTestCase):
    """Tests for the audio service."""

    def test_audio(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_audio_file(self):
        """Ensure a new audio file type can be added to the database"""
        with self.client:
            response = self.client.post(
                'audio',
                data=json.dumps({

                }),
                content_typ='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)

    def test_add_audio_file_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty"""
        pass

    def test_add_duplicate_audio_file(self):
        """Ensure that an error is returned for a duplicate entry"""
        pass


if __name__ == '__main__':
    unittest.main()