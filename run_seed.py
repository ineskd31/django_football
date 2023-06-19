import django 
django.setup()


from equipe.seed import run
from joueur.seed import run

if __name__ == '__main__':
    run()