import unittest
from app.utils import handle_message, schedule_post

class UtilsTestCase(unittest.TestCase):

    def test_handle_message(self):
        message = 'schedule 2024-06-15T12:00 Test Content'
        sender = '+123456789'
        response = handle_message(message, sender)
        self.assertEqual(response, 'Post scheduled successfully.')

    def test_schedule_post(self):
        time = '2024-06-15T12:00'
        content = 'Test Content'
        schedule_post(time, content)
        # Assert the post is scheduled or check the database

if __name__ == '__main__':
    unittest.main()
