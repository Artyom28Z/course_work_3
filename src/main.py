from src.funcions import information_transaction


def main():
    """
    Главная функция запуска цикла для показа 5 последних операций
    :return:
    """
    for i in range(5):
        print(information_transaction(i))

if __name__ == '__main__':
    main()