import argparse
from lib.reporter import report
from lib.document_parser import parse, result

parser = argparse.ArgumentParser('Huge site parser')
parser.add_argument('url')

parse(parser.parse_args().url)
report('output/valid_links.txt', 'output/invalid_links.txt', result)