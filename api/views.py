from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bboard.models import Rubric
from api.serializers import RubricSerializer


#var1
# def api_rubrics(request):
#     if request.method == 'GET': # дай мне какие-то данные
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
#         return JsonResponse(serializer.data, safe=False)

#var2
@api_view(['GET'])
def api_rubrics(request):
    rubrics = Rubric.objects.all()
    serializer = RubricSerializer(rubrics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_rubric_details(request, pk):
    rubric = Rubric.objects.get(pk=pk)
    serializer = RubricSerializer(rubric)
    return Response(serializer.data)