coinbase-tracker
======
A minimal console ticker for Coinbase exchange rates, written in Python 3.3.


Screenshot
------------
![Screenshot](http://i.imgur.com/ooXJ5nD.png)


### Usage

        $ ./tracker.py [-r seconds] [-q btc amount] [-h]
        
- -r (--refresh) allows you to set the refresh rate (in seconds) for Coinbase prices.  Default is 8.
- -q (--quantity) controls the amount of Bitcoin to query the price on.  Default is 1.

Todo
------------
1. Add ability to see price in other currancies
2. Daemon mode (to enable fun things like displaying the price in your command prompt)