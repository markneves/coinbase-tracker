#!/usr/bin/python
# [very simple] Coinbase Tracker v0.3 - powered by Python3
# by Mark Neves - mneves@gmail.com
#
# Notes: Conformed to PEP8, which is why there are odd line-breaks now
#
# Usage: ./tracker.py [btc amount]
#
import json
import requests
import threading
import sys
cb = "https://coinbase.com/api/v1/prices/"
qty = 1 if len(sys.argv) != 2 else int(sys.argv[1])
q = {'qty': qty}


class loadStat(object):
    last = {'buy': 0, 'sell': 0}

    def __init__(self, disp_type="sell"):
        self.disp_type = disp_type

    def val(self):
        arrow = "  "
        headers = {'content-type': 'application/json'}
        r = json.loads(requests.get(cb + self.disp_type, data=json.dumps(q),
                                    headers=headers).text)
        if(loadStat.last[self.disp_type] and loadStat.last[self.disp_type]
                != r['subtotal']['amount']):
            arrow = "\033[92m ▴\033[0m" if loadStat.last[self.disp_type] < r[
                'subtotal']['amount'] else "\033[91m ▾\033[0m"
        else:
            loadStat.last[self.disp_type] = r['subtotal']['amount']

        return("\033[1m" + self.disp_type.title() + ": ${:,.2f}".format(float(
            r['subtotal']['amount'])) + arrow + "\033[0m (${:,.2f}"
            .format(float(r['total']['amount'])) + " with fees)")


def displayTicker():
    threading.Timer(10.0, displayTicker).start()
    sys.stdout.write("\r" + loadStat('buy').val()
                     + "  ¦  " + loadStat('sell').val())
    sys.stdout.flush()

btc = int(q['qty'])
print("\nCoinbase prices (amount: %d Bitcoin%s)" % (btc, "s"[btc == 1:]))
print("-" * 74)
displayTicker()
