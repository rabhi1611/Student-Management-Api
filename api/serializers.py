from rest_framework import serializers
from api import models


class InstituteSerializer(serializers.ModelSerializer):
    class meta:
        model = models.Institute
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):

    institute = InstituteSerializer(read_only =True)
    class meta:
        model = models.Student
        fields = "__all__"