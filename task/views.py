from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from task.models import Task
from .serializers import TaskSerializer


class TaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        user = req.user
        tasks = Task.objects.filter(user=user)
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, req):
        data = JSONParser().parse(req)
        task = Task(
            name=data['name'],
            done=data['done'],
            user=req.user
        )
        serializer = TaskSerializer(task)
        task.save()
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False, status=201)


class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req, id):
        user = req.user
        try:
            task = Task.objects.filter(user=user).get(id=id)
            serializer = TaskSerializer(task)
            return JsonResponse(serializer.data)
        except Task.DoesNotExist:
            return JsonResponse({'message': 'task id not found'}, status=404)

    def put(self, req, id):
        user = req.user
        try:
            task = Task.objects.filter(user=user).get(id=id)
            data = JSONParser().parse(req)
            serializer = TaskSerializer(task, data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False)

            return JsonResponse(serializer.errors, status=400)

        except Task.DoesNotExist:
            return JsonResponse({'message': 'task id not found'}, status=404)

    def delete(self, req, id):
        user = req.user
        try:
            task = Task.objects.filter(user=user).get(id=id)
            task.delete()
            return JsonResponse({'message': 'task deleted'}, status=204)
        except Task.DoesNotExist:
            return JsonResponse({'message': 'task id not found'}, status=404)
