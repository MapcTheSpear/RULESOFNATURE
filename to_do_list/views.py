from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status


@api_view(['GET'])
def task_list_api_view(request):
    tasks = Task.objects.all()
    data = TaskSerializer(tasks, many=True).data
    return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail_api_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={'Yo, man, no error, no such task!': 'fr no'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = TaskSerializer(task).data
        return Response(data=data)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        task.title = request.data.get('title')
        task.description = request.data.get('description')
        task.completed = request.data.get('completed')
        task.created = request.data.get('created')
        task.save()
        return Response(data={'task_id': task.id}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def task_create_api_view(request):
    title = request.data.get('title')
    description = request.data.get('description')
    completed = request.data.get('completed')
    created = request.data.get('created')
    task = Task.objects.create(title=title, description=description, completed=completed,
                               created=created)
    task.save()
    return Response(data={'task_id': task.id})



