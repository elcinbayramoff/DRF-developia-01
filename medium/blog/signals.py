# singal növləri
#receiver
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from .models import Comment
from rest_framework.validators import ValidationError
#Comment yaradılarkən Article'n comment_count field'i artsin

@receiver(post_save, sender=Comment)
def increase_comment_count(sender, instance, created, **kwargs):
    """
    Eger yaradilmaq ucundurse, created = True
    Eks halda created = False
    """
    if created:
        print('Geldi bura')
        instance.article.comment_count += 1
        instance.article.save()


@receiver(post_delete, sender=Comment)
def decrease_comment_count(sender, instance, **kwargs):
    
    if instance.article.comment_count > 0:
        instance.article.comment_count -= 1
        instance.article.save()


# @receiver(pre_save, sender=Comment)
# def pre_save_for_testing(sender, instance, **kwargs):
    
#     raise ValidationError("Qoymuram save edesen")

# @receiver(post_save, sender=Comment)
# def post_save_for_testing(sender, instance, created, **kwargs):
    
#     raise ValidationError("Qoymuram save edesen")

#1. pre_save
#2. post_save
#3. pre_delete
#4. post_delete
#5. m2m_changed
#6. pre_migrate
#7. post_migrate

"""
Süd - > Qida, Ağartı, Tez Köhnələn
"""

