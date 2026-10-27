from rest_framework import serializers
from review.models import Reviews
class ReviewSerializers(serializers.ModelSerializer):

    class Meta:

        model = Reviews

        fields="__all__"

        read_only_fields=["id","owner","movie"]