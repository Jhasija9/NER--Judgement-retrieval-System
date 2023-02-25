from rest_framework import serializers
from .models import File

# serialize the api by doing serialization

class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'