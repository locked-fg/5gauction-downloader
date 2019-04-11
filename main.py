from auction import downloader
from auction import parser
import csv
import logging

if __name__ == '__main__':
    logger = logging.getLogger('auction')
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    data = []
    for aRound in downloader.get_rounds(start_at=1):
        for r in parser.parse(aRound['html']):
            r['round'] = aRound['round']
            data.append(r)

    with open('auction.csv', 'w', newline='') as csvfile:
        fieldnames = ['round', 'Block', 'Ausstattung', 'Bieter', 'Gebot']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
