import django_tables2 as tables
from .models import UserProfileInfo

class UserInfoTable(tables.Table):
    # username = tables.Column(linkify=("member:details", {"pk": tables.A("pk")}))

    class Meta:
        model = UserProfileInfo
        template_name = 'django_tables2/bootstrap.html'
        fields = ('user_profile.username', 'sponsor','phone_number')

class SingleLegUserTable(tables.Table):
    class Meta:
        model = UserProfileInfo
        template_name = 'django_tables2/bootstrap.html'
        fields = ('user_profile.username','country.country','country.flag')