from django.shortcuts import render
from .models import *

from rest_framework import viewsets
from monitor.serializers import *

# Create your views here.
def index(request):
    if request.method == 'GET':
        # chainsplit bool
        is_forked = ForkState.objects.all()[0].is_currently_forked
        has_forked = ForkState.objects.all()[0].has_forked

        # node info
        nodes = Node.objects.all()

        # soft fork stats
        forks = BIP9Fork.objects.all()

        # mtp forks
        mtpforks = MTFork.objects.all()

        context = {'is_forked':is_forked, 'has_forked':has_forked, 'nodes':nodes, 'forks':forks, 'mtpforks':mtpforks}
        return render(request, 'index.html', context)


class NodeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows nodes to be viewed.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class BIP9ForkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows bip9 fork to be viewed.
    """
    queryset = BIP9Fork.objects.all()
    serializer_class = BIP9ForkSerializer


class MTForkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows mt fork to be viewed.
    """
    queryset = MTFork.objects.all()
    serializer_class = MTForkSerializer


class ForkStateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows fork state to be viewed.
    """
    queryset = ForkState.objects.all()
    serializer_class = ForkStateSerializer


