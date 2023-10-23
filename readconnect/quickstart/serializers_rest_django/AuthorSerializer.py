from rest_framework import serializers

from ..models.Author import Author

class AuthorListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        authors = [Author(**item) for item in validated_data]
        return Author.objects.bulk_create(authors)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        list_serializer_class = AuthorListSerializer
        fields = '__all__'