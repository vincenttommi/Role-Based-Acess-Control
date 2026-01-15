from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'myapp.User'
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        #using lazy import to avoid circular 
        from myapp.models import User
        user = User.objects.create_user(**validated_data)
        return user    
    


class StudentSerializer(serializers.ModelSerializer):
     
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = 'myapp.Student'
        fields = '__all__'



    def create(self, validated_data):
        #using lazy import to avoid circular import
        from myapp.models import User,Student
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student
    





    

