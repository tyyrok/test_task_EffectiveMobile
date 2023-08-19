# Тестовое задание для EffectiveMobile

## Описание:
Программа запускается в терминале и взаимодействует с пользователем посредством текстового ввода в терминал.
Для хранения данных используется .csv файл, если его нет, то он будет автоматически создан.
В базе используется только одно уникальное значение - первичный ключ (ID). 
Поиск записи осуществляется только по полному совпадению.

## Функционал:

### Вывод текущих данных из файла в терминал постранично (10 записей)
### Добавление новой записи в базу(файл). ФИО - допускаются только буквы, в названии компании можно использовать цифры, номер телефона - 11 цифр (формат - 1 234 5678901/1-234-5678909/12345678909 )
### Изменение текущей записи. Требуется ввести уникальный номер(первичный ключ), который можно узнать либо с помощью вывода либо с помощью поиска
### Поиск записи в базе по точному совпадению (Фамилия или название компании или номер мобильного)

## ТЗ:

### Реализовать телефонный справочник со следующими возможностями:
1.                   Вывод постранично записей из справочника на экран
2.                   Добавление новой записи в справочник
3.                   Возможность редактирования записей в справочнике
4.                   Поиск записей по одной или нескольким характеристикам
### Требования к программе:
1.                   Реализация интерфейса через консоль (без веб- или графического интерфейса)
2.                   Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
3.                   В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)
### Плюсом будет:
1.                   аннотирование функций и переменных
2.                   документирование функций
3.                   подробно описанный функционал программы
4.                   размещение готовой программы и примера файла с данными на github
