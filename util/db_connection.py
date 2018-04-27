import sqlalchemy
import os


class PostgresClient:
	"""
		Classe para encapsular conexão com Postgres
	"""
	conn_engine = None
	
	@classmethod
	def get_conn_engine(cls) -> sqlalchemy.engine.Engine:
		
		if cls.conn_engine is None:
			connection_string = "postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}".format(
				user=os.getenv("USER"),
				pwd=os.getenv("PWD"),
				host=os.getenv("HOST"),
				port=os.getenv("PORT"),
				db=os.getenv("DB")
			)
			
			cls.conn_engine = sqlalchemy.create_engine(
				connection_string,
				pool_size=5,
				max_overflow=0
			)
		
		return cls.conn_engine
