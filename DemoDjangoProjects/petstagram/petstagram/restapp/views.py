from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from petstagram.restapp.models import Profile, PetPhoto, Pet
from petstagram.restapp.serializers import PetSerializer, PetPhotoSerializer
from django.core.exceptions import ObjectDoesNotExist

class PetListCreate(APIView):
    def get(self, request):
        try:
            ...
        except Pet.DoesNotExist as exc:
            raise Pet.DoesNotExist(
                'some '
                'text'
            ) from exc
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    def post(self, request):
        pet_serializer = PetSerializer(data=request.data)
        if pet_serializer.is_valid():
            pet_serializer.save()
            return Response(pet_serializer.data, status=status.HTTP_201_CREATED)
        return Response(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PetGetUpdateDelete(APIView):
    def put(self, request, pet_id):
        try:
            pet = Pet.objects.get(id=pet_id)
            pet_serializer = PetSerializer(pet, data=request.data)
            if pet_serializer.is_valid():
                pet_serializer.save()
                return Response(pet_serializer.data)
            return Response(pet_serializer.errors)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pet_id):
        try:
            pet = Pet.objects.get(id=pet_id)
            pet_serializer = PetSerializer(pet)
            return Response(pet_serializer.data)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pet_id):
        try:
            pet = Pet.objects.get(id=pet_id)
            pet.delete()
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


class PetPhotoListCreate(APIView):
    def get(self, request):
        pets_photos = PetPhoto.objects.get()
        serializer = PetPhotoSerializer(pets_photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        pet_photo_serializer = PetPhotoSerializer(data=request.data)
        if pet_photo_serializer.is_valid():
            pet_photo_serializer.save()
            return Response(pet_photo_serializer.data, status=status.HTTP_201_CREATED)
        return Response(pet_photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PetPhotoGetUpdateDelete(APIView):
    def put(self, request, pet_photo_id):
        try:
            pet_photo = PetPhoto.objects.get(id=pet_photo_id)
            pet_photo_serializer = PetPhotoSerializer(pet_photo, data=request.data)
            if pet_photo_serializer.is_valid():
                return Response(pet_photo_serializer.data)
            return Response(pet_photo_serializer.errors)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pet_photo_id):
        try:
            pet_photo = PetPhoto.objects.get(id=pet_photo_id)
            pet_photo_serializer = PetPhotoSerializer(pet_photo)
            return Response(pet_photo_serializer.data)
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pet_photo_id):
        try:
            pet_photo = PetPhoto.objects.get(id=pet_photo_id)
            pet_photo.delete()
        except:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
