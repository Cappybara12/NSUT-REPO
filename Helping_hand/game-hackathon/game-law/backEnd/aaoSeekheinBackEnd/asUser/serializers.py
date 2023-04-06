from signin.models import AsUser
# from rest_flex_fields.serializers import FlexFieldsModelSerializer
from rest_framework.serializers import ModelSerializer

class UserViewSerializer(ModelSerializer):
    class Meta:
        model = AsUser
        fields = ['id', 'name','phone','level','otp','createdAt']

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
