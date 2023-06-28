from web3 import Web3

# Подключение к локальному блокчейну Ethereum (порт 8545)
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Проверка успешного подключения к блокчейну
if w3.is_connected():
    print("Успешное подключение к блокчейну Ethereum")
else:
    print("Не удалось подключиться к блокчейну Ethereum")


def get_balance(address):
    balance = w3.eth.get_balance(address)
    return w3.fromWei(balance, 'ether')


def send_eth(sender_private_key, receiver_address, amount):
    # Получение аккаунта отправителя на основе приватного ключа
    sender_account = w3.eth.account.from_key(sender_private_key)

    # Получение текущего номера блока
    current_block = w3.eth.block_number

    # Создание транзакции
    transaction = {
        'to': receiver_address,
        'value': w3.toWei(amount, 'ether'),
        'gas': 21000,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(sender_account.address),
        'chainId': w3.eth.chain_id,
    }

    # Подписание транзакции
    signed_transaction = sender_account.sign_transaction(transaction)

    # Отправка транзакции в сеть
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

    return transaction_hash


# Пример использования функций
if w3.is_connected():
    # Адрес аккаунта для проверки баланса
    address = "0x..."
    balance = get_balance(address)
    print(f"Баланс аккаунта {address}: {balance} ETH")

    # Приватный ключ аккаунта отправителя
    sender_private_key = "..."
    # Адрес аккаунта получателя
    receiver_address = "0x..."
    # Количество Ether для отправки
    amount = 0.1
    transaction_hash = send_eth(sender_private_key, receiver_address, amount)
    print(f"Транзакция успешно отправлена. Хэш транзакции: {transaction_hash.hex()}")
