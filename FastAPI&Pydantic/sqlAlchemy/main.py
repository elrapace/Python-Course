from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# DEFINIZIONE DELLA BASE
Base = declarative_base()

# DEFINIZIONE TABELLA (MODELLO) 'USER'
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# CONFIGURAZIONE DEL MOTORO DI DATABASE
engine = create_engine('sqlite:///users.db')

# CREAZIONE DELLA SESSIONE
Session = sessionmaker(bind=engine)
session = Session()

# CREAZIONE DELLE TABELLE (NEL DB, SE NON ESISTONO GIÀ)
Base.metadata.create_all(engine)

# AGGIUNTA DI UN RECORD
new_user = User(name='Alice', age=30)
session.add(new_user)

# FARE UNA QUERY
users = session.query(User).all()  # RECUPERO GLI UTENTI
for user in users:
    print(user)

# FILTRARE DATI
user = session.query(User).filter_by(name='Alice').first()  # PRENDI L'UTENTE CON NOME 'ALICE'
print(user)