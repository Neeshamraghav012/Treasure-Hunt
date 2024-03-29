from csv import DictReader
from django.core.management import BaseCommand


from game.models import Team, Questions


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from children.csv"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Team.objects.exists() or Questions.objects.exists():
            print('child data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading childrens data")


        #Code to load the data into database
        for row in DictReader(open('./teams.csv')):
            team = Team(temail = row['temail'], tcode = row['tcode'], tname = row['tname'], tbno = row['tbno'], tdone = row['tdone'])  
            team.save()


        for row in DictReader(open('./questions.csv')):
            question = Questions(qtoken = row['qtoken'], qsno = row['qsno'], qbno = row['qbno'], nextlink = row['nextlink'])
            question.save()