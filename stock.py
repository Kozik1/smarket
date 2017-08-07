# This is the code to solve tasks a1 and a2
from __future__ import division
import random, time
import numpy as np
from randtime import  randomDate, strTimeProp
import unittest
class stock:
   'Common base class for all STOCKS'
   stockCount = 0

   def __init__(self, name, type, lastdiv, fixdiv, parvalue):
      self.name = name
      self.type = type
      self.lastdiv=lastdiv
      self.fixdiv=fixdiv
      self.parvalue=parvalue
      stock.stockCount += 1
   
   def displayCount(self):
     print "Total Stocks %d" % stock.stockCount

   def displaystock(self):
      print "Name : ", self.name,  ", Type: ", self.type, ", Last Dividend : ", self.lastdiv, ", Fixed Dividend : ", self.fixdiv,  ", Par Value : ", self.parvalue,  "\n"

"This would create first object of stock class"
TEA = stock("TEA", "common", 0, 0, 100)
"This would create second object of stock class"
POP = stock("POP", "common", 8, 0, 100)
ALE=stock("ALE", "common", 23, 0, 60)
GIN=stock("GIN", "preferred", 8, 0.02, 100)
JOE=stock("JOE", "common", 13, 0, 250)
# Display all the stocks:
print "These are the declared stocks of our simple stock market:"
TEA.displaystock()
POP.displaystock()
ALE.displaystock()
GIN.displaystock()
JOE.displaystock()
print "Total Number of Declared Stocks:", stock.stockCount
stockobj = input('Enter the stock symbol out of {TEA; POP; ALE; GIN; JOE}:')
price = input('Enter the prevailing stock market price:')
# task i: Calculate Dividend yield depending on the type of a stock
if (stockobj.type=="common"):
	DY=stockobj.lastdiv/price
	print  "Dividend yield is:", DY
else:
	DY=stockobj.fixdiv*stockobj.parvalue/price
	print "Dividend yield is:", DY



# task ii: Calculate PE ratio
PE=0
if 	(stockobj.lastdiv!=0):
	PE=price/stockobj.lastdiv
	print "PE ratio of", stockobj.name, "stock is", PE
else:
	print "Last divident of the stock is 0. Cannot calculate PE ratio."
## Unit testing. Try entering a negative price for example!
class DividendTestCase(unittest.TestCase):
    """Tests for meeting division by zero and non-negativity conditions."""
    def test_price_non_zero(self):
        """Price should be strictly greater than zero!"""
        self.assertGreater(price,0)      
        
    def test_DY_positive(self):
        """Dividend yield cannot be negative!"""
        self.assertGreaterEqual(DY,0)      	
    def test_PE_positive(self):
        """PE ratio cannot be negative!"""
        self.assertGreaterEqual(PE,0)     
         		
    def test_lastdiv_non_zero(self):
        """lastdiv strictly greater than zero!"""
        self.assertGreater(stockobj.lastdiv,0)		

if __name__ == '__main__':
    unittest.main()
