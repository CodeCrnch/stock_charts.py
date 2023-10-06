import yfinance as yf
import matplotlib.pyplot as plt
import certifi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ticker = input("Enter Stock Name: ")
data = yf.download(ticker, start="2023-01-01", end="2023-10-01")

plt.figure(figsize=(10, 5))
plt.plot(data["Close"])
plt.title(F"{ticker} Stock Chart")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()