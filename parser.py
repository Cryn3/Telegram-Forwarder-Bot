import configparser
import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message


class parser:
    def __init__(self):
        self.config_file = 'data.ini'
        self._create_config_if_not_exists()
        self.config = self._load_config()
        self.app = Client(
            "my_account",
            api_id=self.config['Telegram']['api_id'],
            api_hash=self.config['Telegram']['api_hash'],
            phone_number=self.config['Telegram']['phone']
        )
        self.source_channel = self.config['Channels']['source_channel']
        self.target_channel = self.config['Channels']['target_channel']

    def _create_config_if_not_exists(self):
        if not os.path.exists(self.config_file):
            config = configparser.ConfigParser()

            config['Telegram'] = {
                'api_id': 'YOUR_API_ID',
                'api_hash': 'YOUR_API_HASH',
                'phone': 'YOUR_PHONE_NUMBER'
            }

            config['Channels'] = {
                'source_channel': '@source_channel_username',
                'target_channel': '@target_channel_username'
            }

            with open(self.config_file, 'w') as configfile:
                config.write(configfile)
            exit()

    def _load_config(self) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(self.config_file)

        if config['Telegram']['api_id'] == 'YOUR_API_ID':
            print("\nПожалуйста, заполните данные в файле data.ini перед запуском бота!")
            exit()

        return config

    async def forward_message(self, message: Message):
        try:
            await message.forward(self.target_channel)
            print(f"Сообщение {message.id} успешно переслано")
        except Exception as e:
            print(f"Ошибка при пересылке сообщения {message.id}: {str(e)}")

    async def start_forwarding(self):
        @self.app.on_message(filters.chat(self.source_channel))
        async def handle_new_message(client, message):
            await self.forward_message(message)

        print("Бот запущен.")
        await self.app.start()
        await self.app.idle()

    def run(self):
        asyncio.run(self.start_forwarding())


if __name__ == "__main__":
    userbot = parser()
    userbot.run()