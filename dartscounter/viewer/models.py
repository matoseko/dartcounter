from django.contrib.auth.models import User

#create a user
def create_user(username, email, password):
    user = User.objects.create_user(username, email, password)
    return user
    