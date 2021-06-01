import yfinance as yf
import pandas as pd


t=yf.Ticker("AAPL")

dati=t.history(period="10Y")

dati.to_csv("AzioniApple10Anni.csv")

print("Applicazione che si connette a YF per scaricare i dati di Microsoft")
print(dati.head())


t=yf.Ticker("MSFT")

dati_msft=t.history(period="10Y")

dati.to_csv("AzioniMSFT10Anni.csv")

print("Applicazione che si connette a YF per scaricare i dati di Microsoft")
print(dati.head())

print("progetto finito. Faccio l'ultimo push")