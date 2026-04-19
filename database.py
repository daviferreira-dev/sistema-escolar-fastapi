import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from pymongo import MongoClient

# Carrega as variáveis do arquivo .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# String de conexão MySQL
URL_BANCO = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Engine com pool_pre_ping para maior estabilidade
engine = create_engine(URL_BANCO, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependência para o FastAPI obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Configuração do MongoDB (NoSQL)
URL_MONGO = os.getenv("URL_MONGO", "mongodb://localhost:27017/") # Tenta pegar do env, senão usa local
mongo_client = MongoClient(URL_MONGO)
db_nosql = mongo_client["bd_escola_nosql"]
colecao_recados = db_nosql["mural_recados"]