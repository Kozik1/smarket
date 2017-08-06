# This is the code to solve tasks a3, a4 and b.
import random, time, datetime
import numpy as np
import scipy.stats
import unittest
from randtime import  randomDate, strTimeProp
# task iii: Record transaction
class trade:
   'Common base class for all trades'
   tradeCount = 0

   def __init__(self, name,  timestamp, quantity, indicator):
      self.name = name
      self.timestamp = timestamp
      self.quantity=quantity
      self.indicator=indicator
      trade.tradeCount += 1
   def displayCount(self):
     print "Total Trades %d" % trade.tradeCount

   def displaytrade(self):
      print "Name : ", self.name,  ", timestamp: ", self.timestamp, ", quantity : ", self.quantity, ", indicator : ", self.indicator,  "\n"
# Random draws of trades
# I draw 1000 transactions within an hour time and record them.
# The type of a stock purchased is a uniform random draw from {TEA; POP; ALE; GIN; JOE}
# The price is drawn from normal distribution with par value of a drawn stock taken as a mean.
# The standard deviation is chosen so that 95% of observations fall within 10% price deviation from the mean.
# The quantity of stocks purchased is a uniform random draw between 1 and 100.
# The buy-or-sell indicator is a coin-toss draw from {buy; sell).
# First step is to initialize:
stocknames=["TEA", "POP", "ALE", "GIN", "JOE"]
indic=["buy","sell"]
d={}
sum_product=0
sum_quantity=0

# If for task 3 interested in time intervals other than 15 minutes, change checkTime
checkTime = datetime.timedelta(minutes=15)
TimeStart=datetime.datetime(2017, 1, 1, 14, 00, 00)-checkTime
pricebase=np.zeros((1000, 1))
# Start a loop and record 1000 trades (task 3)
for i in range(1,1001):
	timestamp=randomDate("1/1/2017 13:00:00", "1/1/2017 14:00:00", random.random())
	name=random.choice(stocknames)
	quantity=np.random.randint(1,100)
	indicator=random.choice(indic)
	if (name=="ALE"):
		mu, sigma = 60, 3 # mean and standard deviation
		price = np.random.normal(mu, sigma)
	elif (name=="JOE"):
		mu, sigma = 250, 12.5 
		price = np.random.normal(mu, sigma)	
	else:
		mu, sigma = 100, 5 
		price = np.random.normal(mu, sigma)
	# Update price base for the GBCE All Share Index
	pricebase[i-1,0]=price
	# Now record your transaction
	d["tr{0}".format(i)]=trade(name, timestamp, quantity, indicator)
	X = datetime.datetime.strptime(timestamp, '%m/%d/%Y %H:%M:%S')
	if (X>TimeStart):
	# Start calculating quantities during last 15 minutes of trading activity
		product=quantity*price
		sum_product+=product
		sum_quantity+=quantity	
	i+=1	
# Task 4: Calculate the volume weighted stock price:
task4answer=sum_product/sum_quantity
# An example of a recorded transaction:
print "An example of a recorded transaction:"
d["tr1"].displaytrade()
print "Total Stocks", trade.tradeCount
print "The Volume Weighted Stock Price based on trades in past 15 minutes is", task4answer
# Uncomment if you want an csv file containing all traded prices.
#np.savetxt("price_base.csv", pricebase, delimiter=",")

# Task b. Calculate the GBCE All Share Index using the geometric mean of prices for all stocks
# Our GBCE All Share Index is a geometric mean of all traded shares. Potential limitation
# is that some stocks could be traded more often than others. 
GBCE=scipy.stats.mstats.gmean(pricebase)
print "GBCE All Share Index is equal to: ", GBCE

## Unit testing
class TradingTestCase(unittest.TestCase):
    """Tests for meeting division by zero and non-negativity conditions."""

    def test_SQ_non_zero(self):
        """sum_quantity should be strictly greater than zero!"""
        self.assertGreater(sum_quantity,0)
        
    def test_VWSP_positive(self):
    	"""The volume weighted stock price cannot be negative!"""
    	self.assertGreaterEqual(task4answer,0)
    	
    def test_DY_positive(self):
    	"""GBCE All Share Index cannot be negative!"""
    	self.assertGreaterEqual(GBCE,0)

if __name__ == '__main__':
    unittest.main()
