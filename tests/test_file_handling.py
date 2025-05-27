import unittest
from src.file_handling.file_reader import load_image, load_json
from src.file_handling.file_writer import save_to_json, export_to_pdf
import os

class TestFileHandling(unittest.TestCase):

    def test_load_image(self):
        # Assuming a sample image file exists for testing
        image_path = 'tests/sample_floor_plan.png'
        image = load_image(image_path)
        self.assertIsNotNone(image)

    def test_load_json(self):
        # Assuming a sample JSON file exists for testing
        json_path = 'tests/sample_floor_plan.json'
        data = load_json(json_path)
        self.assertIsInstance(data, dict)

    def test_save_to_json(self):
        data = {'key': 'value'}
        json_path = 'tests/output.json'
        save_to_json(data, json_path)
        self.assertTrue(os.path.exists(json_path))
        os.remove(json_path)  # Clean up after test

    def test_export_to_pdf(self):
        data = {'key': 'value'}
        pdf_path = 'tests/output.pdf'
        export_to_pdf(data, pdf_path)
        self.assertTrue(os.path.exists(pdf_path))
        os.remove(pdf_path)  # Clean up after test

if __name__ == '__main__':
    unittest.main()