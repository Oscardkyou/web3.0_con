# Взаимодействие с блокчейном Ethereum

![Ethereum](https://img.shields.io/badge/-Ethereum-3C3C3D?style=flat-square&logo=ethereum&logoColor=white)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Web3.py](https://img.shields.io/badge/web3.py-5.17.0-blue.svg)](https://github.com/ethereum/web3.py)


# Ethereum Blockchain Interaction с использованием Python и Web3.py

Этот репозиторий представляет собой мощный инструмент, который предоставляет базовые функции для взаимодействия с локальным блокчейном Ethereum. Включая проверку баланса аккаунтов и выполнение транзакций между ними, наш проект ставит целью предложить простой и эффективный способ для работы с Ethereum.

## Требования к окружению

- Python (версия 3.8 и выше)
- Web3.py (версия 5.17.0)

## Быстрый старт

1. Клонировать этот репозиторий:
```bash
git clone https://github.com/your-username/ethereum-blockchain-interaction.git

    Перейти в директорию проекта:

bash

cd ethereum-blockchain-interaction

    Установить зависимости:

bash

pip install -r requirements.txt

Инструкции по использованию

    Запустите свой локальный Ethereum blockchain. Вы можете использовать инструменты вроде Ganache, он должен быть доступен по адресу http://localhost:8545.

    В файле main.py вам нужно обновить следующие параметры:
        address: Ethereum адрес, баланс которого вы хотите проверить.
        sender_private_key: Приватный ключ аккаунта отправителя.
        receiver_address: Ethereum адрес аккаунта получателя.
        amount: Количество Ether (ETH), которое вы хотите отправить.

    Запустите скрипт:

bash

python main.py

Описание функций

    get_balance(address): Получает баланс указанного Ethereum адреса и возвращает его в виде количества Ether (ETH).

    send_eth(sender_private_key, receiver_address, amount): Позволяет выполнять транзакции Ether (ETH) между аккаунтами и возвращает хеш транзакции для подтверждения и отслеживания.
