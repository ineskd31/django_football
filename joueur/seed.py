from django_seed import Seed
from .models import Roles


def run():
    seeder = Seed.seeder()
    
    
    
    roles = [
        {"name":"Avant"},3
        {"name":"Arriere"},3
        {"name":"Central"},3
        {"name":"Remplacant"},3
    ]
    for el in roles:
        seeder.add_entity(Roles, 1, el)
        
    seeder.execute()
    print("ROLES OK")