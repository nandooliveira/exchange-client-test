# -*- coding: utf-8 -*-
u"""job to run on heroku."""

from api import 

cron = BackgroundScheduler(daemon=True)
