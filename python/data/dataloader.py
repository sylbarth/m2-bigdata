import pandas as pd
import yfinance
import sqlalchemy
from sqlalchemy.sql import text

# connection à la base de données
DB = "mysql+pymysql://root:master2@localhost/projet"
engine = sqlalchemy.create_engine(DB)

# on efface les données précédentes de la table ohlcdata
try:
    with engine.connect() as con:
        con.execute(text(f"DELETE FROM ohlcdata"))
        con.commit()
except:
    print("Cannot delete table")

# lecture de la donnée pour une liste de tickers et stockage dans ohlcdata
tickers = ["BTC-USD", "AAPL", "MSFT", "TSLA"]

for ticker in tickers:
    data = yfinance.download(ticker).reset_index()
    data["ticker"] = ticker
    data.to_sql(name="ohlcdata", con=engine, if_exists='append', index=False)
