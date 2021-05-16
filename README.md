# Bitcoin
This is a small command line tool that gives you the price of the Bitcoin cryptocurrency. You can use it for every currency as long as coinbase supports it
## Installation
```sh
# For your user
pip install bitcoin-cli
# Globally
sudo pip install bitcoin-cli
```
## Usage
The default currency is GBP, so by just running `bitcoin` you will see the price in GBP
If you wish to use another currency, use:
```sh
bitcoin USD # US Dollars
bitcoin EUR # Euros
bitcoin AUD # Australian Dollars
# etc.
```
It will return an output like this:
```                                                                                           
--------------------------------------------------
Current Bitcoin Price in GBP:
£34,557.00
--------------------------------------------------
Price Change over 24 Hours:
Down 11.71%
--------------------------------------------------
Date & Time (BST):
18:55:31, Thursday 13 May 2021
--------------------------------------------------
Source:
Coin Gecko API (coingecko.com)
--------------------------------------------------
```