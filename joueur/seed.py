from django_seed import Seed
from .models import Roles


def run():
    seeder = Seed.seeder()
    
    
    
    roles = [
        {"name":"Avant"},
        {"name":"Arriere"},
        {"name":"Central"},
        {"name":"Remplacant"},
    ]
    for el in roles:
        seeder.add_entity(Roles, 1, el)
        
    seeder.execute()
    print("ROLES OK")