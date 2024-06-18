from rest_framework import serializers
from .models import Register
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
        extra_kwargs = {
            'fname': {'required': True},
        }
        
    username = serializers.CharField( required=True, validators = [UniqueValidator(queryset= Register.objects.all())])
    email = serializers.EmailField( required=True, validators = [UniqueValidator(queryset= Register.objects.all())])
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    c_password = serializers.CharField(write_only=True, required=True)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['c_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
    def create(self, validated_data):
        user = Register.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            fname=validated_data['fname'],
            phone_no=validated_data['phone_no'],
            password= validated_data['password'],
            c_password= validated_data['c_password'],
        )

        # user.set_password(validated_data['password'])
        user.save()

        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = Register(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Both fields are required")
        data['user'] = user
        return data