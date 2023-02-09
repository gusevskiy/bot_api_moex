# bot_api_moex
bot telegram for receiving prices stock in stock exchange moex

### 1) install libraries

```bash
pip install requests
pip install python-dotenv
pip install telegram-telegram-bot==13.7
```
### 2) create .env
##### put two variables there
##### TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


**Updater** - это средство обновления. Этот класс получает обновления для бота либо посредством длительного опроса, либо путем запуска сервера веб-перехватчиков. Полученные обновления ставятся в очередь в update_queue и могут быть извлечены оттуда для соответствующей обработки. Экземпляры этого класса можно использовать в качестве менеджеров асинхронного контекста.

**Update** - Этот объект представляет входящее обновление. Объекты этого класса сравнимы с точки зрения равенства. Два объекта этого класса считаются равными, если их update_id равен.

**add_handler** - регистрирует обработчик
**add_hendlers** - регистрирует сразу несколько обработчиков

```
app.add_handlers(handlers={
    -1: [MessageHandler(...)],
    1: [CallbackQueryHandler(...), CommandHandler(...)]
}
```