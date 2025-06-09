# Telegram Forwarder Bot 🤖

[English](#english) | [Русский](#russian)

<a name="english"></a>
# English Version

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pyrofork](https://img.shields.io/badge/Pyrofork-Latest-green)

## 📝 Description

Telegram Forwarder Bot is a simple and efficient tool for automatically forwarding messages between Telegram channels. Built with Pyrofork library, it provides an easy way to manage content forwarding.

## ✨ Features

- 🚀 Automatic message forwarding between channels
- 📱 Support for all message types (text, media, documents)
- 🛠️ Simple configuration through config file
- 🔄 Asynchronous operation

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Cryn3/Telegram-Forwarder-Bot.git
cd parser
```

2. Install dependencies:
```bash
pip install pyrofork
```

## ⚙️ Configuration

1. Get API credentials from [my.telegram.org](https://my.telegram.org)
2. On first run, the bot will create a `data.ini` file
3. Fill in the following data in `data.ini`:
   - `api_id`: Your API ID
   - `api_hash`: Your API Hash
   - `phone`: Your phone number (with country code)
   - `source_channel`: @username of source channel
   - `target_channel`: @username of target channel

## 🚀 Usage

Run the bot:
```bash
python parser.py
```

The bot will automatically start forwarding messages from the source channel to the target channel.

## 📋 Requirements

- Python 3.8 or higher
- Pyrofork

## ⚠️ Disclaimer

This bot is intended for legal use only. Users are fully responsible for compliance with Telegram's terms of service.

## 📞 Support

If you have questions or issues, create an Issue in the project repository.

---

<a name="russian"></a>
# Русская версия

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pyrofork](https://img.shields.io/badge/Pyrofork-Latest-green)

## 📝 Описание

Telegram Forwarder Bot - это простой и эффективный инструмент для автоматической пересылки сообщений между каналами Telegram. Разработан с использованием библиотеки Pyrofork, он предоставляет удобный способ управления пересылкой контента.

## ✨ Особенности

- 🚀 Автоматическая пересылка сообщений между каналами
- 📱 Поддержка всех типов сообщений (текст, медиа, документы)
- 🛠️ Простая настройка через конфигурационный файл
- 🔄 Асинхронная работа

## 🛠️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Cryn3/Telegram-Forwarder-Bot.git
cd parser
```

2. Установите зависимости:
```bash
pip install pyrofork
```

## ⚙️ Настройка

1. Получите API credentials на [my.telegram.org](https://my.telegram.org)
2. При первом запуске бот создаст файл `data.ini`
3. Заполните следующие данные в `data.ini`:
   - `api_id`: Ваш API ID
   - `api_hash`: Ваш API Hash
   - `phone`: Ваш номер телефона (с кодом страны)
   - `source_channel`: @username канала-источника
   - `target_channel`: @username канала-получателя

## 🚀 Использование

Запустите бота:
```bash
python parser.py
```

Бот автоматически начнет пересылать сообщения из указанного канала-источника в канал-получатель.

## 📋 Требования

- Python 3.8 или выше
- Pyrofork

## ⚠️ Отказ от ответственности

Этот бот предназначен только для легального использования. Пользователи несут полную ответственность за соблюдение правил и условий использования Telegram.

## 📞 Поддержка

Если у вас возникли вопросы или проблемы, создайте Issue в репозитории проекта.
