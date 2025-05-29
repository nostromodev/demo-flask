import collections
if not hasattr(collections, 'MutableMapping'):
    import collections.abc
    collections.MutableMapping = collections.abc.MutableMapping
import unittest
import sys
import os

# Add the parent directory to the Python path to allow importing 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_home_route(self):
        # Test the / route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "<b>There has been a change</b>")

    def test_template_route(self):
        # Test the /template route
        response = self.app.get('/template')
        self.assertEqual(response.status_code, 200)
        # Check if the response contains some content from the template
        # We need to read the content of home.html to check against it.
        # Assuming home.html is in web/app/templates/home.html
        with open('web/app/templates/home.html', 'r') as f:
            expected_content = f.read()
        self.assertEqual(response.data.decode('utf-8').strip(), expected_content.strip())

if __name__ == '__main__':
    unittest.main()
