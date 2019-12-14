from adopcje.models import Message, AdoptionForm
from datetime import datetime
import os

def message_adf_delete():
    messages_to_del = Message.objects.all() #Message.objects.filter(expiry_date=datetime.today)
    adoption_forms_to_del = AdoptionForm.objects.filter(expiry_date=datetime.today)
    for message in messages_to_del:
        for adf in adoption_forms_to_del:
            message.delete()
            adf.delete()

os.environ['DJANGO_SETTINGS_MODULE'] = 'serwis_adopcyjny.settings'
message_adf_delete()