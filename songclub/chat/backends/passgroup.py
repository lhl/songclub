from django.contrib.auth.models import User, Group
from django_chat.chat.models import UserData
from django.conf import settings


class GroupBackend:
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username__exact=username)
            # authentication db
            try:
                group = Group.objects.get(name=password)
                if user.groups.filter(name=password).count() == 0:
                    user.groups=(group,)
                return user
            except:
                return None
        except:
            from random import choice
            import string
            temp_pass = ""
            for i in range(8):
                temp_pass = temp_pass + choice(string.letters)
            user = User.objects.create_user(username, "", temp_pass)
            UserData.objects.get_or_create(user=user)
            user.is_staff = False
            user.save()
            try:
                group = Group.objects.get(name=password)
                if user.groups.filter(name=password).count() == 0:
                    user.groups.add(group)
            except:
                return None
        return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
