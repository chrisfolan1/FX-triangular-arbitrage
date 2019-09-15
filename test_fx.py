#
# test_fx.py
#
# triangular arbitrage example...
#
# The quotation EUR/USD 1.2500 means that one euro is exchanged for 1.2500 US dollars. 
# Here, EUR is the base currency and USD is the quote currency(counter currency). 
# This means that 1 Euro can be exchangeable to 1.25 US Dollars.
# 
#
'''
Example of Triangular Arbitrage
As an example, suppose you have $1 million and you are provided with the following exchange rates: 
EUR/USD = 0.8631, EUR/GBP = 1.4600 and USD/GBP = 1.6939.

With these exchange rates there is an arbitrage opportunity:

Sell dollars for euros: $1 million x 0.8631 = €863,100
Sell euros for pounds: €863,100/1.4600 = £591,164.40
Sell pounds for dollars: £591,164.40 x 1.6939 = $1,001,373
Subtract the initial investment from the final amount: $1,001,373 - $1,000,000 = $1,373
'''

class FX():
	def __init__(self,quote_ccy,rate,base_ccy='USD'):
		self.quote_ccy = quote_ccy
		self.base_ccy  = base_ccy
		self.rate      = rate

	def convert(self, amount, b2q=True):
		''' convert amount to base ccy ''' 
		res = amount / self.rate if b2q else amount * self.rate    # base to quote or quote to base
		print ("{} {} => {} {} ".format(amount, self.quote_ccy, res, self.base_ccy))
		return res

def main():

	EUR_USD_RATE = 0.8631
	eur_usd = FX(base_ccy='EUR', quote_ccy='USD', rate=EUR_USD_RATE)

	EUR_GBP_RATE = 1.4600
	eur_gbp = FX(base_ccy='EUR', quote_ccy='GBP', rate=EUR_GBP_RATE)

	USD_GBP_RATE = 1.6939
	usd_gbp = FX(base_ccy='USD', quote_ccy='GBP', rate=USD_GBP_RATE)

	usd1 = 1000000
	eur  = eur_usd.convert(amount=usd1, b2q=False)		# USD -> EUR
	gbp  = eur_gbp.convert(amount=eur, b2q=True)
	usd2 = usd_gbp.convert(amount=gbp, b2q=False)
	print ("arbitrage: {}".format(round(usd2-usd1,2)))

main()