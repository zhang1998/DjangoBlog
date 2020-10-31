from django.shortcuts import render

# Create your views here.
def update(request):
    print "==>", request.POST.get('value'),request.POST.get('pk')
    if request.method == 'POST':
        pk = request.POST.get('pk')
        v = request.POST.get('value')
        try:
            a = IP.objects.get(id=pk)
            a.hostname = v
            a.save()
        except:
            a = IP(hostname=v, id=pk)
            a.save()
    return HttpResponse('yes')
