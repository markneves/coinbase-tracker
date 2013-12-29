#!/usr/bin/python
# [very simple] Coinbase Tracker v0.1
# by Mark Neves - mneves@gmail.com
import json
import requests
import threading
import sys
cb = "https://coinbase.com/api/v1/prices/"


class loadStat(object):

    def __init__(self, disp_type="sell"):
        self.disp_type = disp_type

    def val(self):
        r = json.loads(requests.get(cb + self.disp_type).text)
        return("\033[1m" + self.disp_type.title() + ": $" + r['subtotal']['amount'] + "\033[0m ($" + r['total']['amount'] + " after fees)")


def displayTicker():
    threading.Timer(5.0, displayTicker).start()
    sys.stdout.write("\r" + loadStat('buy').val()
                     + "  ¦  " + loadStat('sell').val())
    sys.stdout.flush()

print("\nCoinbase prices (per 1 Bitcoin):")
print("-" * 72)
displayTicker()