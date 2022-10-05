from rest_framework import serializers
from .models import Buyplan, Plan

class PlanSerializer(serializers.ModelSerializer):
   class Meta:
    model = Plan
    fields = ['id','amount','sms','roaming','data','subscription']


class BuyPlanSerializer(serializers.ModelSerializer):
   class Meta:
    model = Buyplan
    fields = ['id','amount','sms','roaming','data','subscription']