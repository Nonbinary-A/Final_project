from rest_framework import viewsets,permissions
from django.shortcuts import render, HttpResponse
from .models import Workers
from .serializers import WorkersSerializer

# Create your views here.


def workers_list(request):
    obj = Workers.objects.all
    context = {"object":obj}
    return render(request,'workers/workers_list.html', context)


def worker_detail(request, slug):
    # return HttpResponse(slug)
    worker = Workers.objects.get(slug=slug)
    return render(request, "workers/worker_detail.html", {'worker':worker})


class WorkersView(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
