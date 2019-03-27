from rest_framework import status
from rest_framework.response import Response
from UserProfile.models import User
from UserProfile.serializers import UserListSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from UserProfile.models import User
from UserProfile.serializers import UserSerializer, UserListSerializer
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserFriends(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


