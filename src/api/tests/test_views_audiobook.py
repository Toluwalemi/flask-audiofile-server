import json

from src.api.helpers import add_audiobook
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

    def test_specific_audiobook(self):
        """Ensure get single audiobook behaves correctly."""
        audiobook = add_audiobook('zikora', 2000, 'Ngozi Adichie', 'Adepero Oduye')
        with self.client:
            response = self.client.get(f'/api/v1/audio/audiobook/{audiobook.id}/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('zikora', data['data']['name'])
            self.assertIn('success', data['status'])

        print("\n=============================================================")

    def test_specific_audiobook_no_id(self):
        """Ensure error is thrown if an id for audiobook is not provided."""
        with self.client:
            response = self.client.get(f'/api/v1/audio/audiobook/huh/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 500)
            self.assertIn('Does not exist', data['message'])
            self.assertIn('fail', data['status'])

        print("\n=============================================================")

    def test_specific_audiobook_incorrect_id(self):
        """Ensure error is thrown if an id for audiobook is incorrect."""
        with self.client:
            response = self.client.get(f'/api/v1/audio/audiobook/404/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Does not exist', data['message'])
            self.assertIn('fail', data['status'])

        print("\n=============================================================")

    def test_all_audiobooks(self):
        """Test that the endpoint returns all songs."""
        audiobook = add_audiobook('zikora', 2000, 'Ngozi Adichie', 'Adepero Oduye')
        audiobook = add_audiobook('One Man One Matchet', 5000, 'T.M Aluko', 'Toluwalemi')
        with self.client:
            response = self.client.get('/api/v1/audio/audiobook/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['audiobooks']), 2)

        print("\n=============================================================")

    def test_patch_song(self):
        """Test to update song json"""
        audiobook = add_audiobook('zikora', 2000, 'Ngozi Adichie', 'Adepero Oduye')
        with self.client:
            response = self.client.patch(
                f'/api/v1/audio/audiobook/{audiobook.id}/',
                data=json.dumps({
                    'audioFileType': 'audiobook',
                    'audioFileMetadata': {
                        'author': 'Chimamanda Adichie',
                    }
                }),
                content_type='application/json',
            )

            data = json.loads((response.data.decode()))
            self.assertEqual(response.status_code, 200)
            self.assertIn('Updated!', data['message'])
            self.assertIn('success', data['status'])

        print("\n=============================================================")
