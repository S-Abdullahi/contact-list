from msilib.schema import ServiceInstall
from reg.api.serializer import RegisterSerializer, UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from reg import models

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(user)[1]
        })
    
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if (serializer.is_valid()):
    #         user = serializer.save()
    #         return Response(user)
             
    #     else:
    #         return Response(serializer.errors)
        
        # return Response(user)

# @api_view(['POST'],)
# def register(request):
#     if request.method == 'POST':
#         serializer = RegisterSerializer(data=request.data)
        
#         data = {}
#         if serializer.is_valid():
#             account = serializer.save()
            
#             data['response'] = 'Registration is successful'
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#         # return Response(data, status=status.HTTP_201_CREATED)
        