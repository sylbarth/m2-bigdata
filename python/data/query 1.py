import pandas as pd
import sqlalchemy
from sqlalchemy.sql import text

DB = "mysql+pymysql://root:master2@localhost/projet"

engine = sqlalchemy.create_engine(DB)

data = pd.read_csv("auteurs.csv")
data.to_sql(name="auteurs", con=engine, if_exists='append', index=False)

newdata = pd.read_sql("select * from auteurs", con=engine)
