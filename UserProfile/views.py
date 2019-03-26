from rest_framework import status
from rest_framework.response import Response
from UserProfile.models import User, Friend
from UserProfile.serializers import UserListSerializer, FriendSerializer
from django.http import Http404
from rest_framework.views import APIView

# class FriendList(APIView):
#
#     def get(self, request, format=None):
#         friend = Friend.objects.all()
#         serializer = FriendSerializer(friend, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = FriendSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserListSerializer(user, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = UserListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

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
