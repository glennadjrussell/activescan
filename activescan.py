from connexion.resolver import RestyResolver
import connexion
import logging
import os

def init_logging():
    logger = logging.getLogger('activescan')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('activescan.log')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%d-%m %H:%M',
        filename='activescan.log',
        filemode='w'
    )

    logging.getLogger('').addHandler(ch)
    logging.getLogger('').addHandler(fh)

if __name__ == '__main__':
    init_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting ActiveScan")
    app = connexion.App(__name__, port=8088, specification_dir='swagger/')
    app.add_api('activescan.yaml', resolver=RestyResolver('api'))
    app.run()
