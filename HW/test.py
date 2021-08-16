# ------------------------------------------------------------------
# Name ----------------- Python camp HW #1
# Developer ------------ Cecilia Y. Sui
# Project Description -- software for financial institution to model 
# ---------------------- client's portfolio 
# Limitations ---------- Assume that the person using your library will 
# specify the correct buy price so you can trust it and just need to 
# maintain a proper internal state given the specified buy price. 
# --> This program assumes the correct amount and format of user inputs.
# ------------------------------------------------------------------

import numpy as np

class Portfolio():

    def __init__(self):
        self.hist_log = [] # a list of strings of transactions
        self.cash = 0
        self.stocks = {}  # {symbol: [shares, price bought]} 
        self.mfs = {} # {symbol: shares}

    def __str__(self):
        c = "cash: ${}".format(self.cash)
        s = ["%-5s %s" % (j[0], i) for i, j in self.stocks.items()]
        mf = ["%-5s %s" % (round(j,2), i) for i, j in self.mfs.items()]
        return c + "\nstock: \n" + "\n".join(s) + "\nmutual funds: \n" + "\n".join(mf)
    
    def addCash(self, amount):
        self.cash += amount
        self.hist_log.append("Added ${} to portforlio.".format(amount))

    def buyStock(self, shares, stock):
        total = shares * stock.price
        self.cash -= total
        self.stocks[stock.symbol] = [shares, stock.price]
        self.hist_log.append("Purchased {} share(s) of {} stock for ${} per share with a total of ${}".format(shares,stock.symbol, stock.price, total)) 

    def buyMutualFund(self, shares, mutualfund):
        total = shares * mutualfund.price
        self.cash -= total
        self.mfs[mutualfund.symbol] = shares
        self.hist_log.append("Purchased {} share(s) of {} mutual fund for $1 per share with a total of ${}".format(shares,mutualfund.symbol,total)) 
    
    def sellMutualFund(self, symbol, shares):
        mf_price = round(np.random.uniform(0.9,1.2),2) 
        # round to 2 decimal places for simplicity
        total = mf_price * shares
        self.cash += total
        if self.mfs[symbol] == shares: 
            self.mfs.pop(symbol)
        else: 
            self.mfs[symbol] -= shares
        self.hist_log.append("Sold {} share(s) of {} mutual fund for ${} per share with a total of ${}".format(shares,symbol,mf_price,total)) 

    def sellStock(self, symbol, shares):
        x = self.stocks[symbol][1]
        stock_price = round(np.random.uniform(0.5*x,1.5*x),2) 
        # round to 2 decimal places for simplicity
        total = stock_price * shares
        self.cash += total
        if self.stocks[symbol][0] == shares:
            self.stocks.pop(symbol)
        else:
            self.stocks[symbol][0] -= shares
        self.hist_log.append("Sold {} share(s) of {} stock for ${} per share with a total of ${}".format(shares,symbol,stock_price,total)) 

    def withdrawCash(self, amount):
        if amount > self.cash:
            print("Withdrawing more cash than available.")
        self.cash -= amount 
        self.hist_log.append("Withdrew ${} from portforlio.".format(amount))

    def history(self):
        [print(i) for i in self.hist_log]

class Stock():
    def __init__(self, price, symbol):
        self.price = int(price) # int
        self.symbol = symbol # str
        
class MutualFund():
    def __init__(self, symbol):
        self.symbol = symbol # str
        self.price = 1 # always purchased for $1 / share


if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.addCash(300.50)
    s = Stock(20,"HFH")
    portfolio.buyStock(5, s)
    mf1 = MutualFund("BRT")
    mf2 = MutualFund("GHT")
    portfolio.buyMutualFund(10.3,mf1)
    portfolio.buyMutualFund(2, mf2)
    print(portfolio)
    portfolio.sellMutualFund("BRT", 3)
    portfolio.sellStock("HFH", 1)
    portfolio.withdrawCash(50)
    portfolio.history()
    # print(portfolio)