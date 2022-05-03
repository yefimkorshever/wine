import argparse
import datetime
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def create_parser():
    description = 'The program renders a web-site of a wine shop'
    parser = argparse.ArgumentParser(description=description)
    arg_help = 'path to a file with beverages characteristics (*.xls),\
    wines3.xlsx by default'

    parser.add_argument('--file_path',
                        help=arg_help,
                        default='wine3.xlsx'
                        )
    arg_help = 'The year of company\'s foundation, 1920 by default'
    parser.add_argument('--foundation_year',
                        help='The year of companie\'s foundation',
                        default=arg_help,
                        type=int
                        )
    return parser


def get_numeral_phrase_with_noun(
        numeral,
        nominative_case,
        genitive_singular,
        genitive_plural):

    remainder_hundred = numeral % 100
    if remainder_hundred in tuple(range(11, 20)):
        return (f'{numeral} {genitive_plural}')

    remainder_ten = numeral % 10
    if remainder_ten == 1:
        return (f'{numeral} {nominative_case}')
    elif remainder_ten in (2, 3, 4):
        return (f'{numeral} {genitive_singular}')
    else:
        return (f'{numeral} {genitive_plural}')


def load_drinks(file_path):
    try:
        excel_data_df = pandas.read_excel(
            file_path,
            dtype={'Цена': int, },
            keep_default_na=False,
        )
    except Exception as mistake:
        print(f'Failed to load beverages characteristics from {file_path}\
        cause: {mistake}')
        return None

    drinks_parameters_list = excel_data_df.to_dict('records')
    categorized_drinks_parameters = defaultdict(list)

    for drink_parameters in drinks_parameters_list:
        category = drink_parameters['Категория']
        categorized_drinks_parameters[category].append(drink_parameters)

    return categorized_drinks_parameters


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    categorized_drinks_parameters = load_drinks(namespace.file_path)
    if categorized_drinks_parameters is None:
        return

    today = datetime.date.today()
    shop_age = today.year - namespace.foundation_year

    shop_age_phrase = get_numeral_phrase_with_noun(
        shop_age,
        'год',
        'года',
        'лет'
    )
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
        shop_age_phrase=shop_age_phrase,
        categorized_drinks_parameters=categorized_drinks_parameters
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
