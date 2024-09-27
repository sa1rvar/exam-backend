from rest_framework import serializers
from app.models import Food, Category

class FoodSerializers(serializers.Serializer):
    class Meta:
        model = Food
        fields = 'all'


class FoodSerializersRetr(serializers.Serializer):
    name = serializers.CharField()
    info = serializers.CharField()
    manufacture = serializers.TimeField()
    cat_id = serializers.IntegerField()


    def create(self, validated_data):
        return Food.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.info = validated_data.get("info", instance.content)
        instance.manufacture = validated_data.get("manufacture", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance



class CategorySerializers(serializers.Serializer):
    class Meta:
        model = Category
        fields = 'all'


class CategorySerializersRetr(serializers.Serializer):
    name = serializers.CharField()



    def create(self, validated_data):
        return Food.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance