FROM gorialis/discord.py

WORKDIR /code

COPY . .

CMD ["python", "./bot.py"]
