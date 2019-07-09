from django.contrib.auth import authenticate, login


def login_user(request, email, password):
    user = authenticate(username=email, password=password)
    if user:
        login(request, user)
        return user
    return None
