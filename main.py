import asyncio
from sqlalchemy import Integer, String, create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__  = "items"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)

engine = create_engine('sqlite:///items.db')
Sesion = sessionmaker(bind=engine)
sesion = Sesion()

Base.metadata.create_all(engine)

lista = [
    {'nombre': 'casa1', 'descripcion': 'esta bonita'}, 
    {'nombre': 'casa2', 'descripcion': 'esta elegante'}, 
    {'nombre': 'casa3', 'descripcion': 'esta preciosa'}, 
    {'nombre': 'casa4', 'descripcion': 'esta moderna'}, 
    {'nombre': 'casa5', 'descripcion': 'esta espaciosa'}, 
    {'nombre': 'casa6', 'descripcion': 'esta acogedora'}, 
    {'nombre': 'casa7', 'descripcion': 'esta melancólica'}, 
    {'nombre': 'casa8', 'descripcion': 'esta nostálgica'}, 
    {'nombre': 'casa9', 'descripcion': 'esta fantástica'}, 
    {'nombre': 'casa10', 'descripcion': 'esta mágica'}, 
    {'nombre': 'casa11', 'descripcion': 'esta bella'}, 
    {'nombre': 'casa12', 'descripcion': 'esta hermosa'}, 
    {'nombre': 'casa13', 'descripcion': 'esta victoriana'}, 
    {'nombre': 'casa14', 'descripcion': 'esta adorable'}
]

for esto in lista: 
    item = Item(nombre=esto['nombre'], descripcion=esto['descripcion'])
    sesion.add(item)

sesion.commit()

async def listar_todos(): 
    print('Bienvenido a tus casas :3')
    await asyncio.sleep(2)
    print('Aquí puedes ver todos todas tus casas')
    todos = sesion.query(Item).all()
    for esto in todos: 
        print(f'nombre de tu casa: {esto.nombre}\ndescripción de tu casa: {esto.descripcion}')

async def main(): 
    await listar_todos()

asyncio.run(main())