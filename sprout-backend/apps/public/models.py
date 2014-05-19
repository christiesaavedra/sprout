from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

###
### The below @receiever is a Python decorator. Decorators can alter the way
### that methods work. This one in particular listens for anytime a User object is
### saved, and if it is just being created, it creates a new security token associated
### with that user. These tokens are used for the REST Framework, and allow us to 
### track who is logged in and allow different permissions per user
###
###

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)


###
### Below is an example of a model. Uncomment to see it in action.
### When you create a new model, you must create a new schema migration
### [ python manage.py schemamigration __YOUR-APP-NAME__ --auto ]
### Once the migration is created, you then have to apply it with:
### [ python manage.py migrate ]
###

# class Address(models.Model):
#     ''' Model features for an address '''
#     street = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     state = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)

#     def __unicode__(self):
#         return u'%s, %s, %s' % (self.street, self.city, self.state)

#     class Meta:
#         verbose_name_plural = 'Addresses'

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    glycemic_index = models.DecimalField(max_digits=5, decimal_places=1)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.TextField(unique=True)

    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    photo = models.ImageField(upload_to='photos', blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    cook_time = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    detailed_directions = models.CharField(max_length=10000)
    note = models.CharField(max_length=5000,)
    favorited_by = models.ManyToManyField(User, blank=True, null=True)



    def __unicode__(self):
        return self.name



# class Measurement(models.Model):
#     measurement_type = models.ForeignKey(MeasurementType)
#     amount = models.CharField(max_length=50)
#     recipe = models.ForeignKey(Recipe)
#     ingredient = models.ForeignKey(Ingredient)
#
#
#     def __unicode__(self):
#         return self.name