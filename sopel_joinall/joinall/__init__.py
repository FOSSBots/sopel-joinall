"""This plugin implements .joinall."""

from sopel.plugin import commands, thread, require_admin

import time


@require_admin
@commands('joinall')
@thread(True)
def handle_joins(bot, trigger):
    """Join some channels."""
    channels = bot.config.core.channels
    for channel in channels:
        bot.join(channel)
        time.sleep(1)
