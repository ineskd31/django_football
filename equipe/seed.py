from django_seed import Seed
from .models import Continent

def run():
    seeder = Seed.seeder()
    
    continent = [
        {"name":"Asia"},
        {"name":"Europe"},
        {"name":"America"},
        {"name":"Africa"},
    ]
    
    for el in continent:
        seeder.add_entity(Continent, 1, el)
        
    seeder.execute()
    print('OK')
