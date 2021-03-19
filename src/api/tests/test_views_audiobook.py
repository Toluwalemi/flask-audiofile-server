import json

from src.api.tests.base import BaseTestCase


class TestAudioBook(BaseTestCase):
    """Tests for the audio file type 'Audiobook'."""

    def test_add_valid_audiobook(self):
        """Ensure a new audiobook audio file type can be added to the database"""
        with self.client:
            response = self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'audiobook',
                    'audioFileMetadata': {
                        'name': 'zikora',
                        'duration': 2000,
                        'author': 'Ngozi Adichie',
                        'narrator': 'Adepero Oduye'
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 200)
            self.assertIn('zikora', data['message'])
            self.assertIn('success', data['status'])

        print("\n=============================================================")

    def test_add_duplicate_audiobook(self):
        """Ensure that an error is returned for a duplicate audiobook entry"""
        with self.client:
            self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'audiobook',
                    'audioFileMetadata': {
                        'name': 'zikora',
                        'duration': 2000,
                        'author': 'Ngozi Adichie',
                        'narrator': 'Adepero Oduye'
                    }
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/api/v1/audio/',
                data=json.dumps({
                    'audioFileType': 'audiobook',
                    'audioFileMetadata': {
                        'name': 'zikora',
                        'duration': 2000,
                        'author': 'Ngozi Adichie',
                        'narrator': 'Adepero Oduye'
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 400)
            self.assertIn('This audiobook already exists.', data['message'])
            self.assertIn('fail', data['status'])

        print("\n=============================================================")
