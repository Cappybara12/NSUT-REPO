from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserViewSerializer
from .models import AsUser
import random
import requests
from .colors import COLORS
from .animals import ANIMALS
from .adjectives import ADJECTIVES
from .star_wars import STAR_WARS

def get_random_name(combo=[COLORS, ANIMALS, STAR_WARS,ADJECTIVES], separator: str = " ", style: str = "capital"):
    if not combo:
        raise Exception("combo cannot be empty")

    random_name = []
    for word_list in combo:
        part_name = random.choice(word_list)
        if style == "capital":
            part_name = part_name.capitalize()
        if style == "lowercase":
            part_name = part_name.lower()
        if style == "uppercase":
            part_name = part_name.upper()
        random_name.append(part_name)
    return separator.join(random_name)



# Create your views here.
def create_otp():
    return random.randint(1000, 9999)

def create_random_name():
    name = get_random_name(combo=[ADJECTIVES,ANIMALS])
    return name

def sms_send(a, msg):
    url = "https://2factor.in/API/V1/1793bfe6-a9f3-11ed-813b-0200cd936042/SMS/+91"+str(a[0])+'''/'''+str(msg)+'''/LFTESTUSER'''
    print(url)
    response = requests.request("GET", url)
    print(response.text)

@api_view(['POST'])
def user_signin(request):
    if request.method == 'POST':
        name = create_random_name()
        data = request.data
        otp = create_otp()
        data["otp"] = otp
        data["name"] = name
        print(data['phone'])
        serializer = UserViewSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            sms_send([int(data["phone"])], str(otp))
            obj = AsUser.objects.get_by_natural_key(data["phone"])
            res = getattr(obj, "id")
            return Response({'msg': 'data created', 'userid': res})
        else:
            print(serializer.errors)
            obj = AsUser.objects.get_by_natural_key(data['phone'])
            obj.otp = otp
            obj.save()
            sms_send([int(data["phone"])], str(otp))
            res = getattr(obj, "id")
            return Response({'msg': 'data created', 'userid': res})
