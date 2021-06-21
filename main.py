# Importing Package to get Stock Prices
import stockquotes as sq

# Importing Time To Have Intervals Between The Checking of Stocks
import time

# Defining Class For Stock
class Stock():
    stock_old_price = None
    stock_owned = False
    def __init__(self, symbol):
        self.symbol = symbol
    def stock_current_price(self):
        stock = sq.Stock(self.symbol)
        stock_price = stock.current_price
        print(self.symbol, "-", stock_price)
        return stock_price

# Array To Store All Stocks
Stocks = []

# Calling Global Classes and Variables
MSFT = Stock('MSFT')
Stocks.append(MSFT)

AAPL = Stock('AAPL')
Stocks.append(AAPL)

AMZN = Stock('AMZN')
Stocks.append(AMZN)

GOOG = Stock('GOOG')
Stocks.append(GOOG)

GOOGL = Stock('GOOGL')
Stocks.append(GOOGL)

FB = Stock('FB')
Stocks.append(FB)

TSLA = Stock('TSLA')
Stocks.append(TSLA)

NVDA = Stock('NVDA')
Stocks.append(NVDA)

JPM = Stock('JPM')
Stocks.append(JPM)

JNJ = Stock('JNJ')
Stocks.append(JNJ)

# V = Stock('V')
# Stocks.append(V)

# UNH = Stock('UNH')
# Stocks.append(UNH)

# PYPL = Stock('PYPL')
# Stocks.append(PYPL)

# PG = Stock('PG')
# Stocks.append(PG)

# HD = Stock('HD')
# Stocks.append(HD)

# MA = Stock('MA')
# Stocks.append(MA)

#DIS = Stock('DIS')
#Stocks.append(DIS)

#BAC = Stock('BAC')
#Stocks.append(BAC)

#ADBE = Stock('ADBE')
#Stocks.append(ADBE)

#CMCSA = Stock('CMCSA')
#Stocks.append(CMCSA)

#XOM = Stock('XOM')
#Stocks.append(XOM)

#VZ = Stock('VZ')
#Stocks.append(VZ)

#CRM = Stock('CRM')
#Stocks.append(CRM)

#INTC = Stock('INTC')
#Stocks.append(INTC)

#NFLX = Stock('NFLX')
#Stocks.append(NFLX)

# CSCO = Stock('CSCO')
# Stocks.append(CSCO)

# PFE = Stock('PFE')
# Stocks.append(PFE)

# KO = Stock('KO')
# Stocks.append(KO)

# T = Stock('T')
# Stocks.append(T)

# PEP = Stock('PEP')
# Stocks.append(PEP)

# ABBV = Stock('ABBV')
# Stocks.append(ABBV)

# CVX = Stock('CVX')
# Stocks.append(CVX)

# ABT = Stock('ABT')
# Stocks.append(ABT)

# MRK = Stock('MRK')
# Stocks.append(MRK)

# TMO = Stock('TMO')
# Stocks.append(TMO)

# AVGO = Stock('AVGO')
# Stocks.append(AVGO)

# WMT = Stock('WMT')
# Stocks.append(WMT)

# ACN = Stock('ACN')
# Stocks.append(ACN)

# LLY = Stock('LLY')
# Stocks.append(LLY)

# WFC = Stock('WFC')
# Stocks.append(WFC)

# MCD = Stock('MCD')
# Stocks.append(MCD)

# TXN = Stock('TXN')
# Stocks.append(TXN)

# COST = Stock('COST')
# Stocks.append(COST)

# MDT = Stock('MDT')
# Stocks.append(MDT)

# NKE = Stock('NKE')
# Stocks.append(NKE)

# DHR = Stock('DHR')
# Stocks.append(DHR)

# PM = Stock('PM')
# Stocks.append(PM)

# QCOM = Stock('QCOM')
# Stocks.append(QCOM)

# BMY = Stock('BMY')
# Stocks.append(BMY)

# HON = Stock('HON')
# Stocks.append(HON)

money = 100000

# Function to Buy A Stock
def buy(stock):
    # Calling All Global Variables
    global money

    money = money - stock.stock_current_price()
    stock.stock_owned = True

# Function to Sell A Stock
def sell(stock):
    # Calling All Global Variables
    global money

    money = money + stock.stock_current_price()
    stock.stock_owned = False

# Function to Format Into A String What Stocks are Owned
def stocks_owned():
    # Calling All Global Variables
    global Stocks

    # Array To Store All Stocks
    stocks_owned = []

    # Formatting
    for i in Stocks:
        if i.stock_owned:
            stocks_owned.append(i.symbol)

    return stocks_owned

def checkStocks():
    # Calling All Global Variables
    global Stocks
    global money

    # Set All Prices to Old Prices
    for a in Stocks:
        stock_curr_price = a.stock_current_price()
        if a.stock_old_price != None:
            if stock_curr_price - a.stock_old_price >= a.stock_old_price * 0.0003:
                if money >= stock_curr_price:
                    if a.stock_owned == False:
                        buy(a)
            elif stock_curr_price - a.stock_old_price <= a.stock_old_price * -0.0003:
                if a.stock_owned:
                    sell(a)
        a.stock_old_price = stock_curr_price

wait_message = "Waiting For Next Price Check"

for a in range(1, 11):
    for b in range(12):
        print(wait_message)
        time.sleep(5)
    if money <= 0:
        print("Simulation Ended")
        print(money)
        break
    else:
        print(money)
        print("Stocks Owned:", stocks_owned())
        checkStocks()

for z in Stocks:
    if z.stock_owned:
        sell(z)

print("Final Total:", money)