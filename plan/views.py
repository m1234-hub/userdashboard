from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from .forms import CustomUserCreationForm
from . import serializers
from . import models
from .models import Journaal,TradingPlan
#from.forms import StudentRegistration
from django.contrib import messages



# Create your views here.

@login_required(login_url='plan:login')   
def trading_business_plan(request):
    students = models.TradingPlan.objects.filter(user=request.user)
    if request.method == "POST":
        if "create" in request.POST:
            goals = request.POST.get("goals")
            milestone_timeline = request.POST.get("milestone_timeline")
            strengths = request.POST.get("strengths")
            weaknesses = request.POST.get("weaknesses")
            opportunities = request.POST.get("opportunities")
            threats = request.POST.get("threats")
            TradingPlan.objects.create(
                
                goals=goals,
                milestone_timeline=milestone_timeline,
                strengths=strengths,
                weaknesses=weaknesses,
                opportunities=opportunities,
                threats=threats,
                user=request.user                          
            )
            
            
            
            messages.success(request, "Data added successfully")
        elif "update" in request.POST:
            id = request.POST.get("id")
            goals= request.POST.get("goals")
            milestone_timeline= request.POST.get("milestone_timeline")
            strengths = request.POST.get("strengths")
            weaknesses= request.POST.get("weaknesses")
            opportunities= request.POST.get("opportunities")
            threats= request.POST.get("threats")
            student = TradingPlan.objects.get(id=id)
            student.goals = goals
            student.milestone_timeline = milestone_timeline
            student.strengths = strengths
            student.weaknesses = weaknesses
            student.opportunities = opportunities
            student.threats = threats
            student.save()
            messages.success(request, "Data updated successfully")
    
        elif "delete" in request.POST:
            id = request.POST.get("id")
            TradingPlan.objects.get(id=id).delete()
            messages.success(request, "Data deleted successfully")
    # print(f"The length of students is: {len(students)}")
    context = {"students": students}
    return render(request, 'trading-business-plan.html' , context=context)

@login_required(login_url='plan:login')
def homepag(request):
      return render(request, 'homepag.html')
  
@login_required(login_url='plan:login')
def pricing (request):
      return render(request, 'pricing.html')

@login_required(login_url='plan:login')
def stockMarkets(request):
      return render(request, 'stock-markets.html')

@login_required(login_url='plan:login')
def tradindViwe(request):
      return render(request, 'trading-view.html')
 

 
 
 
 
@login_required(login_url='plan:login') 
def journals(request):
    stu = models.Journaal.objects.filter(user=request.user)
    if request.method == "POST":
        if "create" in request.POST:
            pair =request.POST.get('pair')
            session =request.POST.get('session')
            pips =request.POST.get('pips')
            date =request.POST.get('date')
            entry_time=request.POST.get('entry_time')
            comment =request.POST.get('comment')
            chart_before =request.POST.get('chart_before')
            chart_after =request.POST.get('chart_after')
            profit = request.POST.get('profit')
            Journaal.objects.create(
                
                       pair=pair,
                       session=session,
                       pips=pips,
                       date=date,
                       entry_time=entry_time,
                       comment=comment,
                       chart_after=chart_after,
                       chart_before=chart_before,
                       profit=profit,
                       user=request.user 
                       
                       )
            messages.success(request, "Data added successfully")
        elif "update" in request.POST:
            id = request.POST.get("id")
            pair =request.POST.get('pair')
            session =request.POST.get('session')
            pips =request.POST.get('pips')
            date =request.POST.get('date')
            entry_time=request.POST.get('entry_time')
            comment =request.POST.get('comment')
            chart_before =request.POST.get('chart_before')
            chart_after =request.POST.get('chart_after')
            profit=request.POST.get('profit')
            student = Journaal.objects.get(id=id)
            student.pair = pair
            student.session = session
            student.pips = pips
            student.date = date
            student.entry_time = entry_time
            student.comment = comment
            student.chart_before = chart_before
            student.chart_after = chart_after
            student.profit = profit
            student.save()
            messages.success(request, "Data updated successfully")
            
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Journaal.objects.get(id=id).delete()
            messages.success(request, "Data deleted successfully")

    context = {"stu": stu}
    # print(f"The length STU is: {len(stu)}")
    # print(stu)
    return render(request, 'journal-trades.html', context)

@login_required(login_url='plan:login')
def index(request):
    return_list = []
    info = models.Info.objects.filter(user=request.user)
    returns = models.ActualReturns.objects.filter(user=request.user)
    for i in returns:
        return_list.append({
            'id': i.id,
            'user': i.user.id,
            'value': i.value,
            'day': i.day
        })
    trade_data = []
    if len(info) != 0:
        user_info = info[0]
        over_under_total = 0
        for i in range(1, 32):
            data = {'day': i}
            if i == 1:
                data['starting_balance'] = round(user_info.starting_balance, 3)
            else:
                data['starting_balance'] = round(trade_data[i - 2]['starting_balance'] + trade_data[i - 2]['target'], 3)

            data['target'] = round(data['starting_balance'] * user_info.growth / 100, 3)
            for j in returns:
                if i == j.day:
                    data['actual'] = round(j.value, 3)
                    data['id'] = j.id
                    break
            else:
                data['actual'] = 0
                data['id'] = -1
            if data['actual'] == 0:
                data['over_under'] = 0
            else:
                data['over_under'] = round(data['actual'] - data['target'], 3)
            over_under_total += data['over_under']
            data['over_under_total'] = round(over_under_total, 3)

            trade_data.append(data)
    return render(request, 'index.html',
                  context={'user': {'id': request.user.id, 'username': request.user.username},
                           'data': trade_data})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('plan:homepag')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'auth_form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('plan:login')


def registerUser(request):
      page = 'register'
      form = CustomUserCreationForm()

      if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                  
                  user = form.save(commit=False)
                 
                  user.save()
                
                 # messages.success(request,"Account created Successfully")
                  user = authenticate(request, username=user.username, password=request.POST['password1'])

                  if user is not None:
                        login(request,user)
                        messages.success(request,"Account created Successfully")                     
                        return redirect('plan:login')


      context = {'form': form, 'page': page} 
      return render(request, 'register.html', context=context)

# Create your views here.
class InfoFormViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = models.Info.objects.all()
    serializer_class = serializers.InfoFormSerializer


class ActualReturnsViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = models.ActualReturns.objects.all()
    serializer_class = serializers.ActualReturnsFormSerializer
