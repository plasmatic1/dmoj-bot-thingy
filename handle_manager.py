from discord.ext import commands
import discord
import tinydb

from util import verify_folder_exists

DB_FOLDER = 'data'
DB_FILE = f'{DB_FOLDER}/handles.json'


class HandleManager:
    def __init__(self):
        verify_folder_exists(DB_FOLDER)
        self.db = tinydb.TinyDB(DB_FILE)

    def get_handle(self, id):
        """
        Gets the handle of a user
        :param id: The user ID to get
        :return: The DM::OJ handle of the user, or None of non exists
        """
        return self.db.get(id, None)

    def set_handle(self, id, handle):
        """
        Set the handle of a user
        :param id: The user ID to set
        :param handle: The DM::OJ handle to use
        :return:
        """
        self.db[id] = handle

    def register_commands(self, bot: commands.Bot):
        """
        Registers all the handle-related commands
        :param bot: The bot to register these commands to
        :return:
        """

        @bot.group(
            name='handle',
            description='Manages DM::OJ handles of users in the server'
        )
        async def handle(ctx: commands.Context):
            if not ctx.invoked_subcommand:
                await ctx.channel.send('Invalid subcommand!')

        @handle.command(
            name='set',
            description='Set the handle of a user (or yourself)'
        )
        async def set_handle(ctx: commands.Context):
            raise NotImplementedError

        @handle.command(
            name='get',
            description='Get the handle of a user (or yourself)'
        )
        async def get_handle(ctx: commands.Context, user=None):
            await ctx.channel.send(user or 'None')

        @handle.command(
            name='list',
            description='List handles of all users in the server'
        )
        async def list_handles(ctx: commands.Context):
            raise NotImplementedError
