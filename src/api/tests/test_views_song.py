import json
import unittest

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

    def test_add_invalid_song(self):
        """Ensure error is thrown if the JSON object is empty"""
        print("\n=============================================================")

        pass

    def test_add_duplicate_audio_file(self):
        """Ensure that an error is returned for a duplicate entry"""
        print("\n=============================================================")

        pass


if __name__ == '__main__':
    unittest.main()
