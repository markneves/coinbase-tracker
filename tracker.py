#!/usr/bin/python
# [very simple] Coinbase Tracker v0.2
# by Mark Neves - mneves@gmail.com
import json
import requests
import threading
import sys
cb = "https://coinbase.com/api/v1/prices/"


class loadStat(object):
    last = {'buy': 0, 'sell': 0}

    def __init__(self, disp_type="sell"):
        self.disp_type = disp_type

    def val(self):
        arrow = "  "
        r = json.loads(requests.get(cb + self.disp_type).text)
        if(loadStat.last[self.disp_type] and loadStat.last[self.disp_type]
                != r['subtotal']['amount']):
            arrow = "\033[92m ▴\033[0m" if loadStat.last[self.disp_type] < r[
                'subtotal']['amount'] else "\033[91m ▾\033[0m"
        else:
            loadStat.last[self.disp_type] = r['subtotal']['amount']

        return("\033[1m" + self.disp_type.title() + ": $"
               + r['subtotal']['amount'] + arrow +
               "\033[0m ($" + r['total']['amount']
               + " with fees)")


def displayTicker():
    threading.Timer(10.0, displayTicker).start()
    sys.stdout.write("\r" + loadStat('buy').val()
                     + "  ¦  " + loadStat('sell').val())
    sys.stdout.flush()

print("\nCoinbase prices (per 1 Bitcoin):")
print("-" * 74)
displayTicker()
