from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Buyplan, Plan
from .serializers import PlanSerializer, BuyPlanSerializer

# Create your views here.
def plan(request):
    postpaid_plan = Plan.objects.all()
    return render(request,'plan.html',{'postpaid_plan':postpaid_plan})

def buy_plan(request):
    if request.method=='POST':
        amount = request.POST.get('amount')
        data = request.POST.get('data')
        sms = request.POST.get('sms')
        roaming = request.POST.get('roaming')
        subscription = request.POST.get('subscription')
        plan = Buyplan(amount = amount, data = data, sms = sms, roaming = roaming, subscription = subscription)
        plan.save()

    return render(request,'plan_buy.html')


class PlanlistAPI(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class BuyPlanlistAPI(ListCreateAPIView):
    queryset = Buyplan.objects.all()
    serializer_class = BuyPlanSerializer