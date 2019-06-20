from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class Hello(APIView):
    def get(self, args):
        return Response('hello django')

class HelloWithAuth(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, args):
        return Response('hello django with jwt')
