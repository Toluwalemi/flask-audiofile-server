import json
import unittest

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
                        'participants': {'fullname': ['Tolu', 'William', 'Kpoke',
                                                      'Maximum of 10 participants possibleMaximum of 10 participants possibleMaximum of 10 participants possible']}

                        # 'participants': {'fullname': ['Tolu', 'Tola', 'Tobi', 'shawn', 'djaja', 'aajj',
                        #                               'adhjha', 'dkasjd', 'djdh', 'asdha', 'ashj']}
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 200)
            self.assertIn('Python Daily', data['message'])
            self.assertIn('success', data['status'])

        print("\n=============================================================")


if __name__ == '__main__':
    unittest.main()
