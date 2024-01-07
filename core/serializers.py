from djoser.serializers import UserSerializer as BasedUserSerializer

class UserSerializer(BasedUserSerializer):
    class Meta(BasedUserSerializer.Meta):
        fields = ['id', 'username', 'email']