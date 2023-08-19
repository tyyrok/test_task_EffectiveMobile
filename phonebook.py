import re

def reading_file():
    """Open file for reading recorded info. If file doesn't exist create it

    Returns:
        list: recorded data
    """
    
    with open('phonebook.csv',"a+", encoding="utf-8") as f:
        f.seek(0)
        phonebook_data = []
        for record in f:
            record = record.split(',')
            phonebook_data.append({"id": record[0],
                                   "last_name": record[1], 
                                   "first_name": record[2],
                                   "middle_name": record[3],
                                   "company": record[4],
                                   "company_phone": record[5],
                                   "mobile_phone": record[6].rstrip()})

    return phonebook_data

def save_record(data, last_name, first_name, middle_name, company, company_phone, mobile_phone):
    """Save a record to file
    """
    with open('phonebook.csv', "a+", encoding="utf-8") as f:
        if len(data) == 0:
            number = 1
            f.seek(0)
        else:  
            number = int(data[-1]['id']) + 1
        return f.write(f"{number},{last_name},{first_name},{middle_name},{company},{company_phone},{mobile_phone}\n")
    
def update_record(data):
    """Update record in file, actually updating all file
    """
    with open('phonebook.csv', "w", encoding="utf-8") as f:
        updated_data = ""
        for record in data:
            updated_data += (f"{record['id']},{record['last_name']},{record['first_name']},{record['middle_name']}," 
                            f"{record['company']},{record['company_phone']},{record['mobile_phone']}\n")
        return f.write(updated_data)
        
def check_input_values(value, reg_type='name'):
    """Function for checking input values

    Args:
        value (_type_): Value to check
        reg_type (_type_): Type of value - phone number, name or company name
    """
    reg_names = re.compile('^[a-zA-Zа-яА-Я]+$') #regex for checking names
    reg_company = re.compile('^[a-zA-Zа-яА-Я0-9-][a-zA-Zа-яА-Я0-9- ]+$') #regex for checking company name
    reg_phone = re.compile('^\d{11}$|^\d[ -]\d{3}[ -]\d{7}$') #regex for checking phone number
    
    if reg_type == 'name':
        return reg_names.search(value)
    elif reg_type == 'phone':
        return reg_phone.search(value)
    elif reg_type == 'company':
        return reg_company.search(value)

def show_records(data, records_in_page):
    """Showing current records from db to console with pagination (default=10)
    """
    #data = reading_file()
    i = 0
    print("№ - Фамилия - Имя - Отчество - Название компании - Телефон - Мобильный телефон")
    for record in data:
        print(f"{record['id']} - {record['last_name']} - {record['first_name']}"
              f"- {record['middle_name']} - {record['company']} - {record['company_phone']} - {record['mobile_phone']}")
        
        i += 1
        
        if i % records_in_page == 0:
            print(f"\nДля показа следующих {records_in_page}-ти записей введите 1, любой другой символ для выхода")
            choice = input("Введите номер действия\n")
            if choice != '1':
                return menu()
            print("\n№ - Фамилия - Имя - Отчество - Название компании - Телефон - Мобильный телефон")
    
    input("\nДля возврата в меню введите любой символ\n")
    return menu()

def create_record(data, last_name=None, first_name=None, middle_name=None, company=None, company_phone=None, mobile_phone=None):
    """Create a record in db
    """   
    if last_name is None:
        last_name = input("Введите фамилию:\n")
        if check_input_values(last_name) is None:
            print("Ошибка: Фамилия должна состоять только из букв")
            return create_record(data=data)
        
    if first_name is None:
        first_name = input("Введите имя:\n")
        if check_input_values(first_name) is None:
            print("Ошибка: Имя должно состоять только из букв")
            return create_record(data=data, last_name=last_name)
    
    if middle_name is None:
        middle_name = input("Введите отчество:\n")
        if check_input_values(middle_name) is None:
            print("Ошибка: Отчество должно состоять только из букв")
            return create_record(data=data, last_name=last_name, first_name=first_name)
        
    if company is None:
        company = input("Введите название компании:\n")
        if check_input_values(company, 'company') is None:
            print("Ошибка: Название компании может состоять только из букв и цифр")
            return create_record(data=data, last_name=last_name, first_name=first_name, middle_name=middle_name)
        
    if company_phone is None:
        company_phone = input("Введите номер телефона компании:\n")
        if check_input_values(str(company_phone), 'phone') is None:
            print("Ошибка: Номер телефона должен состоять из 11 цифр")
            return create_record(data=data, last_name=last_name, first_name=first_name, middle_name=middle_name, company=company)
        
    if mobile_phone is None:
        mobile_phone = input("Введите номер мобильного телефона:\n")
        if check_input_values(str(mobile_phone), 'phone') is None:
            print("Ошибка: Номер телефона должен состоять из 11 цифр")
            return create_record(data=data,last_name=last_name, first_name=first_name, 
                                 middle_name=middle_name, company=company, company_phone=company_phone)
      
    result = save_record(data=data, last_name=last_name, first_name=first_name, middle_name=middle_name, 
                         company=company, company_phone=company_phone, mobile_phone=mobile_phone)
    
    if result:
        print("\nУспех: Запись сохранена\n")
        return menu()
    else:
        print("Ошибка: Возникла ошибка при сохранении, попробуйте еще раз")
        return menu()
    
def change_record(data):
    """Changing existing record in db
    """
    print("""Для внесения изменений в телефонный справочник вам необходим номер записи в БД""")
    record_id = input("Введите номер записи:\n")
    search_result = False
    for record in data:
        if record['id'] == record_id:
            search_result = True
            print("Найдена запись:\n")
            print(f"{record['id']} - {record['last_name']} - {record['first_name']}"
              f"- {record['middle_name']} - {record['company']} - {record['company_phone']} - {record['mobile_phone']}")
            print(
            "Внести изменения в?:\n"
            "1) Фамилия\n"
            "2) Имя\n"
            "3) Отчество\n"
            "4) Название компании\n"
            "5) Номер телефона компании\n"
            "6) Номер мобильного телефона\n"
            "7) Вернуться в главное меню\n"
            )
            category = input("Выберите поле для изменения:\n")
            if not re.compile('^[1-7]$').search(category):
                return change_record(data=data)
            
            if category == '7':
                return menu()
            
            new_value = input("Введите новое значение:\n")
            
            message_wrong_names = "Ошибка: Фамилия/Имя/Отчество должны состоять только из букв\n"
            message_wrong_company = "Ошибка: Название компании может состоять только из букв/цифр и пробела\n"
            message_wrong_phone = "Ошибка: Номер телефона должен состоять из 11-ти цифр\n"
            
            if category == '1':
                if check_input_values(new_value) is None:
                    print(message_wrong_names)
                    return change_record(data=data)
                else:
                    record['last_name'] = new_value
            elif category == '2':
                if check_input_values(new_value) is None:
                    print(message_wrong_names)
                    return change_record(data=data)
                else:
                    record['first_name'] = new_value
            elif category == '3':
                if check_input_values(new_value) is None:
                    print(message_wrong_names)
                    return change_record(data=data)
                else:
                    record['middle_name'] = new_value
            elif category == '4':
                if check_input_values(new_value, 'company') is None:
                    print(message_wrong_company)
                    return change_record(data=data)
                else:
                    record['company'] = new_value
            elif category == '5':
                if check_input_values(new_value, 'phone') is None:
                    print(message_wrong_phone)
                    return change_record(data=data)
                else:
                    record['company_phone'] = new_value
            elif category == '6':
                if check_input_values(new_value, 'phone') is None:
                    print(message_wrong_phone)
                    return change_record(data=data)
                else:
                    record['mobile_phone'] = new_value
                    
    if not search_result:
        print("Ошибка: Записи с таким номером не существует\n")
        return menu()
    else:
        if update_record(data=data):
            print("Успех: Запись успешно изменена\n")
            return menu()
        else:
            print("Ошибка: Возникла ошибка, попробуйте повторить операцию")
            return menu()          
    
def find_record(data):
    """Search for a record in db
    """
    category = {'1': 'Фамилии',
                '2': 'Названию компании',
                '3': 'Номеру мобильного телефона'}
    print(
    "\nИскать по:\n"
    "1) Фамилия\n"
    "2) Название компании\n"
    "3) Номер мобильного телефона\n"
    "4) Вернуться в главное меню")
    search_type = input("Выберите категорию поиска\n")
    
    if search_type != '1' and search_type != '2' and search_type != '3':
        return menu()
    else:
        search_value = input(f"Введите данные для поиска по '{category[search_type]}'\n")
        print("\nНайдены записи:")
        print("№ - Фамилия - Имя - Отчество - Название компании - Телефон - Мобильный телефон")
        search_result = False
        
        for record in data:
            if search_type == '1' and record['last_name'] == search_value:
                print(f"{record['id']} - {record['last_name']} - {record['first_name']}"
              f"- {record['middle_name']} - {record['company']} - {record['company_phone']} - {record['mobile_phone']}")
                search_result = True
                
            if search_type == '2' and record['company'] == search_value:
                print(f"{record['id']} - {record['last_name']} - {record['first_name']}"
              f"- {record['middle_name']} - {record['company']} - {record['company_phone']} - {record['mobile_phone']}")
                search_result = True
                
            if search_type == '3' and record['mobile_phone'] == search_value:
                print(f"{record['id']} - {record['last_name']} - {record['first_name']}"
              f"- {record['middle_name']} - {record['company']} - {record['company_phone']} - {record['mobile_phone']}")
                search_result = True
        
        if search_result == False:
            print("Ошибка: Записи не найдены")
                
        print(
        "\nВыберите действие:\n"
        "1) Новый поиск\n"
        "2) Вернуться в главное меню")
        
    choice = input()
    
    if choice == '1':
        return find_record(data=data)
    else:
        return menu()
                
            
def menu(data=None, records_in_page=10):
    """Main function with menu for our console app with functionality:
    1) Output of recorded info
    2) Add new record to database
    3) Change a record in db
    4) Find a record
    """
    data = reading_file()
    menu_string = ("**********************************************************\n"
        "Меню телефонного справочника:\n"
        "1) Вывести данные из базы\n"
        "2) Добавить новую запись\n"
        "3) Изменить существующую запись\n"
        "4) Найти запись в базе\n"
        "5) Выход")
    
    print(menu_string)
    
    choice = input("\nВведите номер действия\n")
    message_wrong_choice = "\nВыбрано некорректное действие. Попробуйте еще раз."
    
    if choice == '1':
        return show_records(data=data, records_in_page=records_in_page)
    elif choice == '2':
        return create_record(data=data)
    elif choice == '3':
        return change_record(data=data)
    elif choice == '4':
        return find_record(data=data)
    elif choice == '5':
        return
    else:
        print(message_wrong_choice)
        return menu()
    
menu()