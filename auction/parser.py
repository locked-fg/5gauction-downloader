import logging
from bs4 import BeautifulSoup

logger = logging.getLogger('auction')


def parse(html):
    '''
    :param html:
    :return: list of data rows
    '''
    soup = BeautifulSoup(html, 'html.parser')
    rows = get_data_rows(get_table1(soup))
    rows += get_data_rows(get_table2(soup))
    rows += get_data_rows(get_table3(soup))
    return rows


def get_table1(soup):
    return soup.find("table", class_="table1 gebotsobjekte")


def get_table2(soup):
    return soup.find("table", class_="table2a gebotsobjekte")


def get_table3(soup):
    return soup.find("table", class_="table2b gebotsobjekte")


def get_data_rows(soup_table):
    entries = []
    rows = soup_table.find_all("tr")
    rows = rows[2:] # remove 2 header lines
    for row in rows:
        entry = {
            'Block': row.find(class_="col1").get_text().strip(),
            'Ausstattung': row.find(class_="col2").get_text().strip(),
            'Bieter': row.find(class_="col3").get_text().strip(),
            'Gebot': row.find(class_="col4").get_text().replace(".", "").strip()
        }
        entries.append(entry)
    return entries


def table_head1(soup_table):
    return soup_table.find("tr", class_="kopf1").get_text().replace("\n", "")


def table_head2(soup_table):
    return soup_table.find("tr", class_="kopf2").get_text().replace("\n", "")


def headline(soup):
    return soup.find(id="content").div.h3.get_text()
