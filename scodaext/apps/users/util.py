from scodaext.apps.users.models import Activity

def add_activity(request, description):
    a = Activity(user = request.user)
    a.activity = description
