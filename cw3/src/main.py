from utils import get_data, get_filtered_data, get_sorted_data, print_result

FILE_OPER = "operations.json"

def main():
    """выводит на экран список из 5 последних выполненных клиентом операций"""

    data = get_data(FILE_OPER)
    data = get_filtered_data(data)
    data = get_sorted_data(data)
    data = print_result(data)
    print(data)


if __name__ == '__main__':
    main()