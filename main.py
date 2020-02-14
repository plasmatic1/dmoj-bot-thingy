import yaml
import os.path
import discord.ext
from commands import register_commands
from log import Logger

# Config stuffs
if not os.path.exists('conf.yml'):
    print('Config file does not exist! Terminating bot...')
    exit(-1)
else:
    with open('conf.yml') as f:
        cfg = yaml.load(f, Loader=yaml.SafeLoader)


    def check_in_config(key):
        if key not in cfg:
            print(f'Config key {key} not in config! Terminating...')
            exit(-1)


    check_in_config('token')
    check_in_config('prefix')

# Initialize global stuff
logger = Logger()


def main():
    # Initialize bot
    bot = discord.ext.commands.Bot(cfg['prefix'])

    # Main event handlers
    @bot.event
    async def on_ready():
        logger.log(f'Bot is ready! Logged on as {bot.user.name}#{bot.user.discriminator} (id: {bot.user.id})')
        logger.log(f'Using prefix {cfg["prefix"]}')

    # Commands stuff
    bot = discord.ext.commands.Bot(cfg['prefix'])
    register_commands(bot)

    bot.run(cfg['token'])


if __name__ == '__main__':
    main()
