from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

# from ..models.User import User
from django.contrib.auth.models import User

from ..serializers_rest_django.UserDjangoSerializer import UserDjangoSerializer

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


# Authentication process
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

######################### api/books Views ########################

# @api_view(['GET'])
# def user_list(request, format=None):
#     '''
#         List all the books or add a new book
#     '''
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = UserSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def user_account(request, pk):

#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
    
    
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserDjangoSerializer(instance=user)
    output = {"token": token.key, "user": serializer.data}
    return Response(output, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def signup(request):
    serializer = UserDjangoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        # This store a hashed version of the plain password
        user.set_password(request.data['password'])
        user.save()
        #########################################
        token = Token.objects.create(user=user)
        output = {"token": token.key, "user": serializer.data}
        return Response(output, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("Estamos rulay ;) {}".format(request.user.email))