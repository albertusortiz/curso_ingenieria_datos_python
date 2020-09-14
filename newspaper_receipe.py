import argparse
import logging
logging.basicConfig(level=logging.INFO)
import urllib,parse import urlparse

import pandas as pd


logger = logging.getLogger(__name__)


def main(filename):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The path to the dirty data.',
                        type=str)

    arg = parser.parse_args()

    main(args.filename)