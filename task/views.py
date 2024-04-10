from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse

from task.models import Task
from .serializers import TaskSerializer


class TaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, req):
        data = JSONParser().parse(req)
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse(serializer.errors, status=400)


class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req, id):
        try:
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task)
            return JsonResponse(serializer.data)
        except Task.DoesNotExist:
            return HttpResponse({'message': 'user id not found'}, status=404)

    def put(self, req, id):
        try:
            task = Task.objects.get(id=id)
            data = JSONParser().parse(req)
            serializer = TaskSerializer(task, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)

            return JsonResponse(serializer.errors, status=400)

        except Task.DoesNotExist:
            return HttpResponse({'message': 'user id not found'}, status=404)

    def delete(self, req, id):
        try:
            task = Task.objects.get(id=id)
            task.delete()
            return JsonResponse({'message': 'task deleted'}, status=204)
        except Task.DoesNotExist:
            return HttpResponse({'message': 'user id not found'}, status=404)
