from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics #give generic class for our convience , read the documentation for more
from .serializers import UserSerializer,NoteSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
   serializer_class=NoteSerializers
   permission_classes=[IsAuthenticated]

   def get_queryset(self):
      user=self.request.user # a way to get user name 
      return Note.objects.filter(author=user) # will give all the notes with the current user as author
   
   def perform_create(self, serializer):
      if serializer.is_valid():
         serializer.save(author=self.request.name)   
      else:
         print(serializer.errors)

      
class NoteDelete(generics.DestroyAPIView):
   serializer_class=NoteSerializers
   permission_classes=[IsAuthenticated]

   def get_queryset(self):
      user=self.request.user
      return Note.objects.filter(author=user) #we just need to specifiy the note , it will delete the note itself. Who is it? who cares.


class CreateUserView(generics.CreateAPIView):
   queryset=User.objects.all()
   serializer_class=UserSerializer
   permission_classes=[AllowAny]