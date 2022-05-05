# New Russian wine

Web-site of wine shop "New Russian wine".

## Installing script
There is a file named requirements.txt in the root project directory.
Run in command line:

```
pip install -r requirements.txt
```


## Inputing data

Drinks cards are loaded from *.xlsx file.
There is an example in the root directory: **drinks.xlsx**.
It's possible to copy the example and fill it up with your data.
Also you can create a file (*.xlsx) with the following structure: 

<table border="1">
   <caption><b>Структура файла для загрузки<b></caption>
   <tr>
    <th>Категория</th>
    <th>Название</th>
    <th>Сорт</th>
    <th>Цена</th>
    <th>Картинка</th>
    <th>Акция</th>
   </tr>
   <tr>
     <td>Белые вина</td>
     <td>Белая леди</td>
     <td>Дамский пальчик</td>
     <td>399</td>
     <td>belaya_ledi.png</td>
     <td>Выгодное предложение</td>     
   </tr>
   <tr>
     <td>Напитки</td>
     <td>Коньяк классический</td>
     <td></td>
     <td>350</td>
     <td>konyak_klassicheskyi.png</td>
     <td></td>     
   </tr>
</table>

## Running script

- Download the project files
- Run: 

```
python3 main.py
```
- При запуске можно указать путь к файлу загрузки и год основания компании.
Подробнее параметры запуска можно посмотреть во встроенной справке; 
для просмотра справки запустите 

```
python3 main.py -h
```

- Go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Project purposes

The project was created for educational purposes.
It's a lesson in a python web developer course at [Devman](https://dvmn.org).
