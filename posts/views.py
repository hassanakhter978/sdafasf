from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .models import PostModel
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your views here.


# ucntion based Views
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])  # Add authentication classes
@permission_classes([IsAuthenticated])  # Apply IsAuthenticated permission
def listAll_and_create_view(request):    #This fucntion will show all the posts on GET Mehthod and will create a new post on POST method
    if request.method == 'GET':
        posts = PostModel.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_view(request, pk):  #this fuction will show a specific post on GET Method, Update a specific post on PUT method.
    try:
        post = PostModel.objects.get(pk=pk)
    except PostModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterUser(APIView):
    def new_user(self,request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wring'})

        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user= user)
        return Response({'status' : 200, 'payload' : serializer.data, 'token': str(token_obj), 'messsage': 'your data is shown'})