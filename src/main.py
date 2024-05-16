from src.funcions import information_transaction, load_transactions, sorted_date_transactions, executed_transactions


def main():
    """
    Главная функция запуска цикла для показа 5 последних операций
    :return:
    """
    transactions = load_transactions('operations.json')
    sorted_transaction = sorted_date_transactions(transactions)
    five_transaction = executed_transactions(sorted_transaction)
    for i in range(5):
        print(information_transaction(i, five_transaction))

if __name__ == '__main__':
    main()
