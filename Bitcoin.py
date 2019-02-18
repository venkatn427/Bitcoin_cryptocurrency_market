1. Bitcoin. Cryptocurrencies. So hot right now.
Since the launch of Bitcoin in 2008, hundreds of similar projects based on the blockchain technology have emerged. 
We call these cryptocurrencies (also coins or cryptos in the Internet slang). Some are extremely valuable nowadays, and others may have the potential to become extremely valuable in the future1. 
In fact, the 6th of December of 2017 Bitcoin has a market capitalization above $200 billion.

The astonishing increase of Bitcoin market capitalization in 2017.
1- WARNING: The cryptocurrency market is exceptionally volatile and any money you put in might disappear into thin air. 
Cryptocurrencies mentioned here might be scams similar to Ponzi Schemes or have many other issues (overvaluation, technical, etc.). 
Please do not mistake this for investment advice.

That said, let's get to business. As a first task, we will load the current data from the coinmarketcap API and display it in the output.

# Importing pandas
import pandas as pd
​
# Importing matplotlib and setting aesthetics for plotting later.
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'svg' 
plt.style.use('fivethirtyeight')
​
# Reading in current data from coinmarketcap.com
current = pd.read_json("https://api.coinmarketcap.com/v1/ticker/")
​
# Printing out the first few lines
current.head()
24h_volume_usd	available_supply	id	last_updated	market_cap_usd	max_supply	name	percent_change_1h	percent_change_24h	percent_change_7d	price_btc	price_usd	rank	symbol	total_supply
0	6.189495e+09	17538500	bitcoin	1550191046	63428107592	2.100000e+07	Bitcoin	-0.05	-0.49	6.33	1.000000	3616.506976	1	BTC	17538500
1	3.266116e+09	104862328	ethereum	1550191038	12744088393	NaN	Ethereum	-0.19	-1.28	15.98	0.033669	121.531618	2	ETH	104862328
2	4.151599e+08	41208093050	ripple	1550191023	12430819688	1.000000e+11	XRP	-0.28	-0.86	3.33	0.000084	0.301660	3	XRP	99991698361
3	9.760551e+08	60471000	litecoin	1550191025	2524284455	8.400000e+07	Litecoin	-0.06	-1.04	25.49	0.011564	41.743720	4	LTC	60471000
4	9.083497e+08	906245118	eos	1550191024	2499505958	NaN	EOS	0.03	-4.06	17.53	0.000764	2.758090	5	EOS	1006245120
