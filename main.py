from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
from pprint import pprint
from collections import defaultdict


def foundation_date():
    return datetime.date(1920, 1, 1)


def years_since_date(beginning):
    today = datetime.date.today()
    return today.year - beginning.year


def agreed_number(number, noun):
    return (f'{number} {noun}')


def agree_noun_with_number_ru(
        number,
        initial_form,
        singular_genitive,
        plural_genitive):

    remainder_hundred = number % 100
    if remainder_hundred in tuple(range(11, 20)):
        return agreed_number(number, plural_genitive)

    remainder_ten = number % 10
    if remainder_ten == 1:
        return agreed_number(number, initial_form)
    elif remainder_ten in (2, 3, 4):
        return agreed_number(number, singular_genitive)
    else:
        return agreed_number(number, plural_genitive)


def load_wines():
    excel_data_df = pandas.read_excel(
        'wine2.xlsx',
        sheet_name='Лист1',
        dtype={'Цена': int, }
    )

    wine_rows = excel_data_df.to_dict('records')
    wine_categories = defaultdict(list)

    for bottle in wine_rows:
        wine_categories[bottle['Категория']].append(bottle)

    return wine_categories


def main():
    wines = load_wines()
    pprint(wines)
    return

    start_date = foundation_date()
    number_years = years_since_date(start_date)

    past_years = agree_noun_with_number_ru(number_years, 'год', 'года', 'лет')

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(past_years=past_years, wines=wines)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
