import logging
import unittest

from bs4 import BeautifulSoup
from auction import parser


class TestApi(unittest.TestCase):

    def setUp(self):
        with open('result.html', 'r') as myfile:
            self.html_content = myfile.read()
            self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def test_headline(self):
        head = parser.headline(self.soup)
        self.assertEqual(head, "Ergebnis der Runde 171")

    def test_t1(self):
        tab = parser.get_table1(self.soup)
        rows = tab.find_all("tr")
        self.assertEqual(len(rows), 12+2, "rows in table 1 do not match")

    def test_t2(self):
        tab = parser.get_table2(self.soup)
        rows = tab.find_all("tr")
        self.assertEqual(len(rows), 8+2, "rows in table 2 do not match")

    def test_t3(self):
        tab = parser.get_table3(self.soup)
        rows = tab.find_all("tr")
        self.assertEqual(len(rows), 21+2, "rows in table 3 do not match")

    def test_get_data_rows(self):
        data1 = parser.get_data_rows(parser.get_table1(self.soup))
        self.assertEqual(len(data1), 12, "wrong amount of data rows in table 1")

        data2 = parser.get_data_rows(parser.get_table2(self.soup))
        self.assertEqual(len(data2), 8, "wrong amount of data rows in table 2")

        data3 = parser.get_data_rows(parser.get_table3(self.soup))
        self.assertEqual(len(data3), 21, "wrong amount of data rows in table 3")

    def test_parse(self):
        data = parser.parse(self.html_content)
        self.assertEqual(len(data), 12+8+21, "wrong amaount of overall data")

        entry = data[0]
        self.assertTrue('Block' in entry, "key 'Block' not found")
        self.assertTrue('Ausstattung' in entry, "key 'Ausstattung' not found")
        self.assertTrue('Bieter' in entry, "key 'Bieter' not found")
        self.assertTrue('Gebot' in entry, "key 'Gebot' not found")




if __name__ == '__main__':
    logger = logging.getLogger('auction')
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    unittest.main()
