import argparse
import datetime
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def create_parser():
    description = 'The program renders a web-site of a wine shop'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--file_path',
                        help='path to a file with drinks characteristics\
                         (*.xls); wines3.xlsx by default',
                        default='drinks.xlsx'
                        )

    parser.add_argument('--foundation_year',
                        help='The year of company\'s foundation;\
                        1920 by default',
                        default=1920,
                        type=int
                        )
    return parser


def get_age_phrase(age):
    remainder_hundred = age % 100
    if remainder_hundred in tuple(range(11, 20)):
        return f'{age} лет'

    remainder_ten = age % 10
    if remainder_ten == 1:
        return f'{age} год'
    elif remainder_ten in (2, 3, 4):
        return f'{age} года'
    else:
        return f'{age} лет'


def load_drinks(file_path):

    excel_data_df = pandas.read_excel(
        file_path,
        dtype={'Цена': int, },
        keep_default_na=False,
    )

    drinks_records = excel_data_df.to_dict('records')
    drinks_catalog = defaultdict(list)

    for drink_parameters in drinks_records:
        category = drink_parameters['Категория']
        drinks_catalog[category].append(drink_parameters)

    return drinks_catalog


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    drinks = load_drinks(namespace.file_path)

    today = datetime.date.today()
    shop_age = today.year - namespace.foundation_year
    shop_age_phrase = get_age_phrase(shop_age)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
        shop_age_phrase=shop_age_phrase,
        drinks=drinks
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
