import requests
import logging

from auction import config

logger = logging.getLogger('auction')


def get_rounds(start_at=1):
    '''
    :param start_at: start at this auction round
    :return: list of dicts: [{round: x, html: ...}]
    '''
    pages = []
    headers = {'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'de-DE',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    round = start_at
    while True:
        page = "{:03d}".format(round)
        url = config.base_url+page+".html"

        logger.info("fetching round %d, url: %s", round, url)
        r = requests.get(url, headers=headers)
        logger.info("round %d, result code: %d", round, r.status_code)
        if r.status_code == 200:
            round += 1
            pages.append({'round':round, 'html':r.text})
        else:
            break

    return pages