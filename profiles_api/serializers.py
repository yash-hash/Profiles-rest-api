from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes our name field for testing our APIVIew"""
    name = serializers.CharField(max_length=10)
