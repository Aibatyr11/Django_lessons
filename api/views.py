from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from bboard.models import Rubric
from api.serializers import RubricSerializer
from rest_framework import status, generics

#var1
# def api_rubrics(request):
#     if request.method == 'GET': # дай мне какие-то данные
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
#         return JsonResponse(serializer.data, safe=False)

#var2
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def api_rubrics(request):
    if request.method == 'GET':
        rubrics = Rubric.objects.all()
        serializer = RubricSerializer(rubrics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RubricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_rubric_details(request, pk):
    rubric = Rubric.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = RubricSerializer(rubric)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = RubricSerializer(rubric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rubric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#НИЗКОУРОВНЕВЫЙ
# class APIRubrics(APIView):
#     def get(self, request):
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = RubricSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#

#Комбинтрованные
class APIRubrics(generics.ListCreateAPIView):
    queryset = Rubric.objects.all()
    serializer_class = (IsAuthenticated,)


class APIRubricDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rubric.objects.all()
    serializer_class = (IsAuthenticated,)


class APIRubricList(generics.ListAPIView):
    queryset = Rubric.objects.all()
    serializer_class = (IsAuthenticated,)


