# VideoEncoder - a telegram bot for compressing/encoding videos in h264 format.
# Copyright (c) 2021 WeebTime/VideoEncoder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from os import supports_dir_fd
from pyrogram import idle
from . import app, sudo_users
from .helper.ext_utils.fs_utils import restart

async def main():
    await app.start()
    print(f'[Started]: @{(await app.get_me()).username}')
    await idle()
    await app.stop()

app.loop.run_until_complete(main())


def restart(update, context):
    restart_message = sendMessage("Restarting...", context.bot, update.message)
    if Interval:
        Interval[0].cancel()
    alive.kill()
    clean_all()
    srun(["pkill", "-9", "-f", "gunicorn|aria2c|qbittorrent-nox|megasdkrest"])
    srun(["python3", "update.py"])
    with open(".restartmsg", "w") as f:
        f.truncate(0)
        f.write(f"{restart_message.chat.id}\n{restart_message.message_id}\n")
    osexecl(executable, executable, "-m", "bot")
    restart_handler = CommandHandler(BotCommands.RestartCommand, restart,
                                     filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)

dispatcher.add_handler(restart_handler)
