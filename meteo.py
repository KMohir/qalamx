import os

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

# Now you can import Django modules
import django
django.setup()

# Your Django-related code here
from basic_app.models import DataHashorot
from basic_app.models import data

def get_statistica_values():
    # Retrieve all instances
    data = DataHashorot.objects.all()

    # Extract the 'statistica' field from each instance
    statistica_values = [entry.statistica for entry in data]

    return statistica_values
temp=0

statistica_values = get_statistica_values()
for x in statistica_values:
    a = x.split(' ', 1)[0]
    temp+=float(a)

summa = (temp/550)*100
if summa>100:
    summa=100


eggs = (temp/50)*100
if eggs>100:
    eggs=100


lichinka = (temp/200)*100
if lichinka>100:
    lichinka=100


zrelix=(temp/300)*100
if zrelix>100:
    zrelix=100
data_entry = {
    'summa': f'{summa} %',
    'eggs': f'{eggs} %',
    'lichinka': f"{lichinka} %",
    'dlyazrelix': f"{zrelix} %",

}
data_instance = data.objects.create(**data_entry)
