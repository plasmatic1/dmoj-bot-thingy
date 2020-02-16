import yaml
import os.path
import discord.ext
from duel.duel_manager import DuelManager
from handle_manager import HandleManager
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
duel_manager = DuelManager()
handle_manager = HandleManager()


def main():
    # Initialize bot
    bot = discord.ext.commands.Bot(cfg['prefix'], description='test')

    # Main event handlers
    @bot.event
    async def on_ready():
        logger.log(f'Bot is ready! Logged on as {bot.user.name}#{bot.user.discriminator} (id: {bot.user.id})')
        logger.log(f'Using prefix {cfg["prefix"]}')
        await bot.change_presence(activity=discord.Game(name='Juggling a hot cup of Coffee'))

    # Commands stuff
    duel_manager.register_commands(bot)
    handle_manager.register_commands(bot)

    logger.log('Logging in...')
    bot.run(cfg['token'])


if __name__ == '__main__':
    main()
