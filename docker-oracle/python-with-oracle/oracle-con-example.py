# WIP
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

URI = "oracle://system:password@oracle-db:1521"
engine = create_engine(URI, echo=True)

metadata_obj = MetaData()

user = Table('user', metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False),
    Column('email_address', String(60), key='email'),
    Column('nickname', String(50), nullable=False)
)

metadata_obj.create_all(engine)



print(f"INFO ==> {metadata_obj.info}")