import threading
import time

from discord.ext import commands

from request_manager import RequestManager, request_submissions

DUEL_UPDATE_TIMEOUT = 10.0


class Duel:
    def __init__(self, user1, user2, problem_id, start_time):
        self.user1 = user1
        self.user2 = user2
        self.problem_id = problem_id
        self.start_time = start_time

    def init_message(self):
        raise NotImplementedError  # TODO

    def update_time(self, cur_time):
        raise NotImplementedError  # TODO

    """
    Returns 1 if p1 (player 1) wins, 2 if p2 (player 2) wins, and -1 if nobody has won yet
    """

    def check_win(self, p1_subs, p2_subs):
        raise NotImplementedError  # TODO

    def update_win(self, who_won):
        raise NotImplementedError  # TODO


class DuelManager:
    def __init__(self, duel_update_timeout=DUEL_UPDATE_TIMEOUT):
        self.duel_update_timeout = duel_update_timeout

        self.users = set()
        self.duels = []

        self.duel_update_thread = threading.Thread(target=self.update_duels)
        self.dmoj_request_manager = RequestManager(request_submissions)

    def is_dueling(self, user):
        return user in self.users

    def add_duel(self, user1, user2, problem_id):
        self.duels.append(Duel(user1, user2, problem_id, time.time()))

    def update_duels(self):
        while True:
            # Keeping track of completed duels
            to_remove = []
            index = 0

            # Update duels
            for duel in self.duels:
                p1_subs = self.dmoj_request_manager.ask(duel.user1)
                p2_subs = self.dmoj_request_manager.ask(duel.user2)
                win = duel.check_win(p1_subs, p2_subs)
                if win == 1:
                    duel.update_win(1)
                    to_remove.append(index)
                elif win == 2:
                    duel.update_win(2)
                    to_remove.append(index)
                else:
                    duel.update_time(time.time())

                index += 1

            # Remove completed duels
            for index in reversed(to_remove):  # Reversed so that earlier indices removed do not affect later ones
                del self.duels[index]

            # Only update every once in a while
            time.sleep(self.duel_update_timeout)

    def register_commands(self, bot: commands.Bot):
        @bot.group(
            name='duel',
            description='Command for managing duels',
        )
        @commands.check(commands.guild_only())
        async def duel(ctx: commands.Context):
            if not ctx.invoked_subcommand:
                ctx.channel.send('Invalid Subcommand!')

        @duel.command(
            name='challenge',
            description='Challenges another user',

        )
        async def challenge(ctx: commands.Context):
            raise NotImplementedError  # TODO

        @duel.command()
        async def list_duels(ctx: commands.Context):
            raise NotImplementedError  # TODO

        @duel.command()
        async def duel_params(ctx: commands.context):
            raise NotImplementedError  # TODO
