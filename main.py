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


def agree_noun_with_number_ru(
        number,
        initial_form,
        singular_genitive,
        plural_genitive):

    remainder_hundred = number % 100
    if remainder_hundred in tuple(range(11, 20)):
        return (f'{number} {plural_genitive}')

    remainder_ten = number % 10
    if remainder_ten == 1:
        return (f'{number} {initial_form}')
    elif remainder_ten in (2, 3, 4):
        return (f'{number} {singular_genitive}')
    else:
        return (f'{number} {plural_genitive}')


def load_beverages(file_path):
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

    beverages_characteristics_list = excel_data_df.to_dict('records')
    beverages_characteristics_dict = defaultdict(list)

    for characteristic in beverages_characteristics_list:
        category = characteristic['Категория']
        beverages_characteristics_dict[category].append(characteristic)

    return beverages_characteristics_dict


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    beverages_characteristics = load_beverages(namespace.file_path)
    if beverages_characteristics is None:
        return

    today = datetime.date.today()
    current_year = today.year
    shop_age = current_year - namespace.foundation_year

    shop_age_phrase = agree_noun_with_number_ru(shop_age, 'год', 'года', 'лет')
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
        shop_age_phrase=shop_age_phrase,
        beverages_characteristics=beverages_characteristics
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
