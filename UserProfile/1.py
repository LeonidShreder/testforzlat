from UserProfile.serializers import UserProfileSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

UserProfile = UserProfile(code='foo = "bar"\n')
UserProfile.save()

UserProfile = UserProfile(code='print("hello, world")\n')
UserProfile.save()