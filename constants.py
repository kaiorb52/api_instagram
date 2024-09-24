# constants.py

from datetime import datetime
from datetime import timedelta, datetime

dia_atual = datetime.today()
x = dia_atual.weekday()

ontem = dia_atual - timedelta(days = 1)
run = True
