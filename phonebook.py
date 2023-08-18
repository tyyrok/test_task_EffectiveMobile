
def open_file_for_read():
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

def show_records(records_in_page=10):
    """Showing current records from db to console with pagination
    """
    data = open_file_for_read()
    i = 0
    print(records_in_page)
    for record in data:
        print(f"{record['id']} - {record['last_name']} - {record['first_name']}"
              f"- {record['middle_name']} - {record['company']} - {record['company_phone']} - {record['mobile_phone']}")
        
        i += 1
        
        if i == records_in_page - 1:
            print("\nДля показа следующих записей введите 1, любой другой символ для выхода")
            choice = input("Введите номер действия\n")
            if choice != '1':
                return menu()
            
def create_record():
    """Create a record in db
    """
    pass

def change_record()
    """Changing existing record in db
    """
    pass
    
def find_record():
    """Search for a record in db
    """
    pass
            

def menu():
    """Main function with menu for our console app with functionality:
    1) Output of recorded info
    2) Add new record to database
    3) Change a record in db
    4) Find a record
    """
    
    print("""**********************************************************
    Меню телефонного справочника:
    1) Вывести данные из базы
    2) Добавить новую запись
    3) Изменить существующую запись
    4) Найти запись в базе
    5) Выход
    ******************************************************""")
    choice = input("Введите номер действия\n")
    message_wrong_choice = "\nВыбрано некорректное действие. Попробуйте еще раз."
    
    if choice == '1':
        return show_records()
    elif choice == '2':
        return create_record()
    elif choice == '3':
        return change_record()
    elif choice == '4':
        return find_record()
    elif choice == '5':
        return
    else:
        print(message_wrong_choice)
        return menu()
    
menu()