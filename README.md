# New Russian wine

Web-site of wine shop "New Russian wine"

## Installing necessary packages

There is a file named requirements.txt in the root project directory.
Run in command line:

```bash
pip install -r requirements.txt
```

## Inputting data

Drinks cards are loaded from  .xlsx file.
There is an example in the root directory: **drinks.xlsx**.
It's possible to copy the example and fill it up with your data.
Also, you can create a file (.xlsx) with the following structure:

| Категория  |      Название       |      Сорт       | Цена  |         Картинка         |        Акция         |
| :--------: | :-----------------: | :-------------: | :---: | :----------------------: | :------------------: |
| Белые вина |     Белая леди      | Дамский пальчик |  399  |     belaya_ledi.png      | Выгодное предложение |
|  Напитки   | Коньяк классический |                 |  350  | konyak_klassicheskyi.png |                      |

## Running script

- Download the project files
- Run:

```bash
python3 main.py
```

- Go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

- It's possible to input a file path to .xlsx file and company's foundation date. To find out more, run:

```bash
python3 main.py -h
```

## Project purposes

The project was created for educational purposes.
It's a lesson for python and web developers at [Devman](https://dvmn.org)
