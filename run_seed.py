import django 
django.setup()


from joueur.seed import run

if __name__ == '__main__':
    run()