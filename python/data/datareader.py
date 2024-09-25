import pandas as pd
import sqlalchemy
from sqlalchemy.sql import text
import plotly.graph_objects as go

# connection à la base de données
DB = "mysql+pymysql://root:master2@localhost/projet"
engine = sqlalchemy.create_engine(DB)

# lecture des données
data = pd.read_sql(sql="SELECT * FROM ohlcdata WHERE ticker='BTC-USD' ORDER BY Date", con=engine)
print(data)

# plot
fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])
fig.update_layout(xaxis_rangeslider_visible=True)
fig.show()
