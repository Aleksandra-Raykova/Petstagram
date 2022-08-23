from rest_framework import serializers

from petstagram.restapp.models import Profile, Pet, PetPhoto


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class PetPhotoSerializer(serializers.ModelSerializer):


    def validate(self, data):
        filesize = data.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise serializers.ValidationError("Max file size is %sMB" % str(megabyte_limit))

    class Meta:
        model = PetPhoto
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True)

    class Meta:
        model = Profile
        fields = "__all__"
