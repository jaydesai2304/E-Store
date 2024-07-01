from rest_framework import serializers
from .models import Register
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"
        extra_kwargs = {
            "fname": {"required": True},
        }

    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=Register.objects.all())]
    )
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=Register.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    c_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs["password"] != attrs["c_password"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = Register.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            fname=validated_data["fname"],
            phone_no=validated_data["phone_no"],
            password=validated_data["password"],
            c_password=validated_data["c_password"],
        )

        # user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ("username", "password")

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = Register.objects.filter(username=username, password=password).first()
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        return data


class ForgotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ("email",)

    def validate(self, data):
        email = data.get("email")
        person_details = Register.objects.filter(email=email)
        if not person_details:
            raise serializers.ValidationError("email address not valid")
        return data


class OtpSerializer(serializers.Serializer):
    enter_otp = serializers.CharField()

    def validate(self, data):
        otp = self.context.get("otp")
        enter_otp = data.get("enter_otp")
        if otp != enter_otp:
            raise serializers.ValidationError("Invalid OTP")
        return data


class ResetpasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ("password", "c_password")

    def validate(self, data):
        email = self.context.get("email_id")
        password = data.get("password")
        c_password = data.get("c_password")

        if password != c_password:
            raise serializers.ValidationError("password not match")

        person_details = Register.objects.get(email=email)
        person_details.password = password
        person_details.c_password = c_password
        person_details.save()
        return person_details


class EditprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ("fullname", "phone_number")

    def validate(self, data):
        username = self.context.get("user_id")
        fullname = data.get("fullname")
        phone_number = data.get("phone_number")

        if not phone_number.isdigit():
            raise ValidationError("Please enter only numbers for the phone number.")

        if len(phone_number) != 10:
            raise ValidationError("Enter a 10 digit phone number.")

        person_details = Register.objects.filter(username=username).first()
        if person_details:
            person_details.fullname = fullname
            person_details.phone_number = phone_number
            person_details.save()
        return data
