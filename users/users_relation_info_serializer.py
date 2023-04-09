from rest_framework import serializers


class BaseUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ...
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'user_role']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class GetStudentInfo:
    def get_balance(self, obj):
        bank_account = obj.bank_account_id
        return bank_account.balance if bank_account else None

    def get_direction(self, obj):
        direction = obj.direction
        from users.serializers import DirectionSerializer
        return DirectionSerializer(direction, many=True).data


class GetEmployeeInfo:
    def get_direction(self, obj):
        direction = obj.direction
        from users.serializers import DirectionSerializer
        return DirectionSerializer(direction).data