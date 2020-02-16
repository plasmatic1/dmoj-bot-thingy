import discord
import os.path


def retrieve_channel_by_name(name: str, guild: discord.Guild):
    raise NotImplementedError  # TODO


def format_channel(channel: discord.TextChannel):
    raise NotImplementedError  # TODO


def verify_folder_exists(path: str):
    """
    Checks whether the path exists as a directory.  If not, a directory will be created at that path
    :param path: The path
    """
    if not os.path.isdir(path):
        os.mkdir(path)

