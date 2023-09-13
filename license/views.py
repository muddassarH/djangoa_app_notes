from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required



# @login_required
# def all_data(request):
#     data = License.objects.all()
#     return render(request, 'all_data.html', {'data': data})



# @login_required
# def save_data(request):
#     if request.method == 'POST':
#         p_id = request.POST.get('p_id')
#         system_id = request.POST.get('system_id')
#         date_input = request.POST.get('date_input')
#         business_name = request.POST.get('business_name')
#         owner_name = request.POST.get('owner_name')
#         opening_date = request.POST.get('opening_date')
#         mid_date = request.POST.get('mid_date')
#         final_date = request.POST.get('final_date')
#         user_id = request.POST.get('user_id')

#         lisc = License(
#             p_id=p_id,
#             system_id=system_id,
#             date_input=date_input,
#             business_name=business_name,
#             owner_name=owner_name,
#             opening_date=opening_date,
#             mid_date=mid_date,
#             final_date=final_date,
#             user_id=user_id
#         )

#         lisc.save()

#     return render(request,'home.html')
@login_required
def home(request):
    return render(request, 'home.html')
