from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class TaskListView(APIView):
    
    def get(self):
        ...


    def post(self):
        ...



class TaskDetailView(APIView):
    
    def get(self, id):
        ...

    def put(self, id):
        ...

    def delete(self, id):
        ...
