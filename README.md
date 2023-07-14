# Взаимодействие с блокчейном Ethereum

![Ethereum](https://img.shields.io/badge/-Ethereum-3C3C3D?style=flat-square&logo=ethereum&logoColor=white)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Web3.py](https://img.shields.io/badge/web3.py-5.17.0-blue.svg)](https://github.com/ethereum/web3.py)


Этот репозиторий содержит скрипт на языке Python, который позволяет взаимодействовать с локальным блокчейном Ethereum. Он предоставляет функции для проверки баланса счета и отправки Ether (ETH) между аккаунтами.

## Предварительные требования

- Python 3.8 или выше
- Библиотека Web3.py (версия 5.17.0)

## Установка

1. Клонируйте этот репозиторий:

```bash
git clone https://github.com/your-username/ethereum-blockchain-interaction.git

    Перейдите в папку проекта:

bash

cd ethereum-blockchain-interaction

    Установите необходимые зависимости:

bash

pip install -r requirements.txt

Использование

    Запустите локальный блокчейн Ethereum (например, с помощью Ganache) на http://localhost:8545.

    Откройте файл main.py и измените следующие переменные:
        address: Адрес Ethereum, для которого вы хотите проверить баланс.
        sender_private_key: Приватный ключ отправителя Ethereum-аккаунта.
        receiver_address: Адрес Ethereum-аккаунта получателя.
        amount: Количество Ether (ETH) для отправки.

    Запустите скрипт:

bash

python main.py

Документация по функциям
get_balance(address)

Получает баланс указанного Ethereum-адреса.

    address: Адрес Ethereum для проверки баланса.
    Возвращает баланс счета в Ether (ETH).

send_eth(sender_private_key, receiver_address, amount)

Отправляет указанное количество Ether (ETH) с одного счета на другой.

    sender_private_key: Приватный ключ отправителя Ethereum-аккаунта.
    receiver_address: Адрес Ethereum-аккаунта получателя.
    amount: Количество Ether (ETH) для отправки.
    Возвращает хэш транзакции.

Лицензия


Вы можете настроить этот шаблон в соответствии со своими конкретными потребностями проекта.
