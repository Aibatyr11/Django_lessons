from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=30)


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare, through='Kit',
                                    through_fields=('machine', 'spare'))

    notes = GenericRelation('Note', related_query_name='spare')

    notes = GenericRelation('Note')


class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, )


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


# Прямое наследование
class Message(models.Model):
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-published', ]


class PrivateMessage(Message):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.OneToOneField(Message, on_delete=models.CASCADE, parent_link=True)


# # Абстракные наследование
# class Message(models.Model):
#     content = models.TextField()
#     name = models.CharField(max_length=20)
#     email = models.EmailField()
#     # published = models.DateTimeField(auto_now_add=True, db_index=True)
#
#     class Meta:
#         abstract = True
#         ordering = ['name']
#
#
#
# class PrivateMessage(Message):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#     email = None

    # class Meta:
    #     abstract = True
    #     ordering = ['order', 'name']


# from django.contrib.postgres.fields import ArrayField,HStoreField
#
#
# class PGSRubric(models.Model):
#     name = models.CharField(max_length=30, verbose_name='Name')
#     description = models.TextField(verbose_name='Description')
#
#     tags = ArrayField(models.CharField(max_length=20),
#                                        verbose_name='Tags')
#
#
# class PGSProject(models.Model):
#     name = models.CharField(max_length=40, verbose_name='Название')
#     platforms = HStoreField(verbose_name='platforms')
#     description = models.TextField(verbose_name='Description')
#
#     tags = ArrayField(models.CharField(max_length=20),
#                       verbose_name='Tags')


#variant 1
# class Profile(models.Model):
#     phone = models.CharField(max_length=20)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#variant 2
# class AdvUser(AbstractUser):
#     phone = models.CharField(max_length=20)

#variant 3
# class AdvUser(User):
#     phone = models.CharField(max_length=20)
#     class Meta:
#         proxy = True

# class Comment(models.Model):
#     ...
#     class Meta:
#         permissions = (
#             ('hide_comments', 'Can hide comments'),
#         )
#         default_permissions = ('change', 'delete')
#
#
# def hide_comment(request):
#     if request.user.has_perm('bboard.hide_comments'):
#         #Пользователь может скрывать коменты
#         pass