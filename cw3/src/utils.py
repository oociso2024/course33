from datetime import datetime
import json

def get_data(file_oper):
    """
    Получает данные из файла операций
    """

    with open(file_oper, "r", encoding="utf-8") as f:
        data = f.read()
    return json.loads(data)


def get_filtered_data(data):
    """
    Фильтрует данные по 'EXECUTED' из списка операций и формирует другой список
    """

    fil_data = []
    for i in data:
        if i and i.get('state') == 'EXECUTED':
            fil_data.append(i)
    return fil_data


def get_sorted_data(data):
    """
    Сортирует данные из списка  по дате и времени операций и возвращает 5 последних операций
    """

    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def print_result(data):
    """
    Форматирует данные из списка и выводит на печать
    """

    for i in data:
        if i.get("from"):
            old_data = i["date"]
            date_transaction = datetime.strptime(old_data, "%Y-%m-%dT%H:%M:%S.%f")
            date_transaction = date_transaction.strftime("%d.%m.%Y")
            old_count_to = i["to"]
            count_transaction_to = old_count_to[-4:]
            old_count_from = i["from"]
            if not old_count_from.find("Счет"):
                count_transaction_from = old_count_from[-4:]
                print(f'\n{date_transaction} {i.get("description")}\nСчет **{count_transaction_from} -> '
                      f'Счет **{count_transaction_to}\n{i["operationAmount"]["amount"]} руб.')
            else:
                count_transaction_from = old_count_from[:-16]
                count_transaction_from_number = old_count_from[-16:]
                c1 = count_transaction_from_number[:4]
                c2 = count_transaction_from_number[4:6]
                c3 = count_transaction_from_number[-4:]
                print(f'\n{date_transaction} {i.get("description")}\n{count_transaction_from}{c1} {c2}** **** {c3} -> '
                      f'Счет **{count_transaction_to}\n{i["operationAmount"]["amount"]} руб.')
        else:
            old_data = i["date"]
            date_transaction = datetime.strptime(old_data, "%Y-%m-%dT%H:%M:%S.%f")
            date_transaction = date_transaction.strftime("%d.%m.%Y")
            old_count_to = i["to"]
            count_transaction_to = old_count_to[-4:]
            print(f'\n{date_transaction} {i.get("description")}\n-> '
                  f'Счет **{count_transaction_to}\n{i["operationAmount"]["amount"]} руб.')