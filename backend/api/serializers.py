from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=["id","username","password"] #will check for these filds in the input before creating the user;
    extra_kwargs={"password": {"write_only": True}}

  def create(self, validated_data):#will create a user and return user;
    user=User.objects.create_user(**validated_data)
    return user
  
class NoteSerializers(serializers.ModelSerializer):
  class Meta:
    model=Note
    fields=["id","title","content","created_at","author"]
    extra_Kwargs={"author":{"read_only":True}}