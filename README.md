Fastapi_-practise


## framework

fastapi

### schemas

主要是用於api的輸入輸出的格式，用於檢查輸入、輸出的格式是否正確

### models

主要是用於操作資料庫，對資料庫進行增刪改查

## Database - sqlalchemy

利用sqlalchemy的套件，可用於 ORM（物件關聯映射），將 Python 類與資料庫表格進行映射，提供一個抽象層來操作資料庫，也有其他SQL查、插、刪的功能

### alembic

用於資料庫遷移，修改資料庫結構，並記錄版本資訊

# sqlalchemy - alembic

Alembic 來檢測 SQLAlchemy Model 的變更，生成對應的遷移文件。遷移文件描述如何在資料庫進行這些變更。

最後:執行 Alembic 的遷移命令可變更ˋ在實際的資料庫結構中。這樣，資料庫才會同步到最新的 Model 結構。
