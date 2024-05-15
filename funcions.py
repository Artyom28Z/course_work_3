import json
from operator import itemgetter


def load_transactions(path):
    """
    Функция открытия файла operations.json
    :param path:
    :return: список со словарями
    """
    with (open('operations.json', encoding="utf-8") as file):
        content = file.read()
    transactions = json.loads(content)
    return transactions


def sorted_date_transactions():
    """
    Функция сортировки операций по дате (вначале самые последние)
    :return: список со словарями
    """
    transaction = load_transactions('operations.json')
    transactions = [i for i in transaction if 'date' in i]

    sorted_transaction = sorted(transactions, key=itemgetter("date"), reverse=True)
    return sorted_transaction


def executed_transactions():
    """
    Функция удаления из списка отменненых операций (в списке остаются только успешные операции)
    :return: список со словарями
    """
    check_transaction = sorted_date_transactions()
    new_list_transaction = []
    for i in check_transaction:
        if i["state"] == "EXECUTED":
            new_list_transaction.append(i)
    return new_list_transaction


def information_transaction(i):
    """
    Функция отображения информации об операции
    :param i:
    :return: f-строки
    """
    five_transaction = executed_transactions()

    date = f"{five_transaction[i]["date"][8:10]}.{five_transaction[i]["date"][5:7]}.{five_transaction[i]["date"][0:4]}"

    account = five_transaction[i]["to"]
    split_account = account.split()
    if len(split_account) == 2 and split_account[0] == "Счет":
        encrypted_account = f"{split_account[0]} **{split_account[1][-4:]}"
    elif len(split_account) == 3:
        encrypted_account = f"{split_account[0]} {split_account[1]} {split_account[2][0:5]} {split_account[2][5:7]}** **** {split_account[2][-4:]}"
    elif split_account[0] == "Maestro" or split_account[0] == "MasterCard":
        encrypted_account = f"{split_account[0]} {split_account[1][0:5]} {split_account[1][5:7]}** **** {split_account[1][-4:]}"

    if five_transaction[i]["description"] == "Открытие вклада":
        information_five_transaction = f"""{date} {five_transaction[i]["description"]}
{encrypted_account}
{five_transaction[i]["operationAmount"]["amount"]} {five_transaction[i]["operationAmount"]["currency"]["name"]}
"""
        return information_five_transaction

    card_number = five_transaction[i]["from"]
    split_card_number = card_number.split()
    if len(split_card_number) == 2 and split_card_number[0] != "Счет":
        encrypted_card_number = f"{split_card_number[0]} {split_card_number[1][0:5]} {split_card_number[1][5:7]}** **** {split_card_number[1][-4:]}"
    elif len(split_card_number) == 3:
        encrypted_card_number = f"{split_card_number[0]} {split_card_number[1]} {split_card_number[2][0:5]} {split_card_number[2][5:7]}** **** {split_card_number[2][-4:]}"
    elif split_card_number[0] == "Счет":
        encrypted_card_number = f"{split_card_number[0]} **{split_card_number[1][-4:]}"

    information_five_transaction = f"""{date} {five_transaction[i]["description"]}
{encrypted_card_number} -> {encrypted_account}
{five_transaction[i]["operationAmount"]["amount"]} {five_transaction[i]["operationAmount"]["currency"]["name"]}
"""
    return information_five_transaction

