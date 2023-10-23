from django.db import models

class Author(models.Model):
    __listAuthors = []
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
    def get_author_list(self):
        #If the local memory is empty load from the database
        if len(self.__listAuthors) == 0:
            self.__listAuthors = Author.objects.all()
            return self.__listAuthors
        
        #If the local memory already has been loaded do not access to the database
        else:
            len(self.__listAuthors) > 0
            return self.__listAuthors
        

    def get_author_by_name(self):
        #Returns the full record looking for the name
        pass
