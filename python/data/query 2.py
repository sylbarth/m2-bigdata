import pandas as pd
import sqlalchemy
from sqlalchemy.sql import text

DB = "mysql+pymysql://root:master2@localhost/projet"

engine = sqlalchemy.create_engine(DB)

# exécuter du SQL directement
with engine.connect() as con:
    con.execute(text(f"DELETE FROM articles WHERE id=1"))
    con.commit()

# exécuter via pandas
data = pd.read_csv("auteurs.csv")
data.to_sql(name="auteurs", con=engine, if_exists='append', index=False)
