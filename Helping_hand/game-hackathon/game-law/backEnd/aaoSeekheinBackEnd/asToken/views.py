from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MultiToken as Token
from .serializers import TokenSerializer
from signin.models import AsUser

# Create your views here.
@api_view(['POST'])
def get_token(request):
    if request.method == 'POST':
        data = request.data
        user_id = request.data.get("user")
        otp = request.data.get("otp")
        check_serializer = TokenSerializer(data=data)
        if len(str(otp)) < 4:
            return Response(check_serializer.errors)
        if AsUser.objects.filter(id=user_id, otp=otp).exists():
            tmp = AsUser.objects.filter(id=user_id, otp=otp)

            if check_serializer.is_valid():
                tmp.update(otp=0)
                token = Token()
                key = token.generate_key()
                check_serializer.save(key=key)
                return Response({"token": str(key)})
            else:
                return Response(check_serializer.errors)
        else:
            return Response({"message":"row does not exist"})