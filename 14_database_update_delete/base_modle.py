from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

# 這個是用來定義資料庫的命名規則
# 這裡定義了五種命名規則，分別是：
# ix: index
# uq: unique
# ck: check
# fk: foreign key
# pk: primary key
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)
