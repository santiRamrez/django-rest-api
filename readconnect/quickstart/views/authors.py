from django.views.decorators.csrf import csrf_exempt

from ..models.Author import Author
from ..serializers_rest_django.AuthorSerializer import AuthorSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser


######################### api/authors Views ########################

@api_view(['GET', 'POST'])
def author_list(request, format=None):
    '''
        List all the authors or add a several authors
    '''
    if request.method == 'GET':
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        uploaded_json = request.data
        serializer = AuthorSerializer(data = uploaded_json, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)