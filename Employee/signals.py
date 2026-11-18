 

from django.dispatch import receiver
from django.db.models.signals import pre_save
from Employee.models import Employee

@receiver(pre_save,sender=Employee)
def to_upper(sender, instance, **kwargs):
                     instance.name  = instance.name.upper()
