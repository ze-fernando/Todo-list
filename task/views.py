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
        try:
            data = JSONParser().parse(req)
            task_serializer = TaskSerializer(data=data)
            if task_serializer.is_valid():
                task_serializer.save(user=req.user)
                return JsonResponse(task_serializer.data, status=201)
            else:
                return JsonResponse(task_serializer.errors, status=400)
        except KeyError as e:
            return JsonResponse({'error': str(e)}, status=400)


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
            task = Task.objects.filter(user=user, id=id).first()
            data = JSONParser().parse(req)
            if task:
                task.name=data['name']
                task.done=data['done']
                task.save()
                
                serializer = TaskSerializer(task)
                
                return JsonResponse(serializer.data, safe=False, status=200)
            
            else:
                return JsonResponse({"message": "task does not exists"},e safe=False, status=404)
                
        except Task.DoesNotExist:
            return JsonResponse({'message': 'task id not found'}, status=404)
        
        except KeyError as e:
            return JsonResponse({'message': str(e)}, status=400)


    def delete(self, req, id):
        user = req.user
        try:
            task = Task.objects.filter(user=user).get(id=id)
            task.delete()
            return JsonResponse({'message': 'task deleted'}, status=204)
        except Task.DoesNotExist:
            return JsonResponse({'message': 'task id not found'}, status=404)
