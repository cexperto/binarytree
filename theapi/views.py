from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .Tree import Node
# Create your views here.


def create_tree(request):    
    try:
        root = Node(70)
        root.left = Node(49)
        root.right = Node(84)
        root.right.left = Node(37)
        root.left.right = Node(54)
        root.right.left.left = Node(22)
        root.right.left.right = Node(40)
        root.right.left = Node(78)
        root.right.right = Node(85)

        root.right.left.left = Node(76)
        root.right.left.right = Node(80)
        return JsonResponse({'messague': 'tree created'})    
    except Exception:
        return Response({"error": "some problem to create tree"})


@api_view(["POST"])
def binary_tree(request):
    if request.method == "POST":
        if request.data["input"]:
            return Response({
                'message': request.data
            })
        return Response({"error": "invalid keys"})
