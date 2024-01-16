import unittest

class app(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_read_page(self):
        # check if the page is loaded
        self.assertTrue(self.app.testing)

    def test_add_item(self):
        # Test adding an item
        response = self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
    
    def test_update_item(self):
        response = response = self.app.post('/update/0', data={"new_item":"updated item"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")

    def test_delete_item(self):
        # you can refer to the app by using self.app
        # make a post request with self.app.post(...
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
