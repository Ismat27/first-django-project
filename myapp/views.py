from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Superb'
    feature1.details = 'Our services are superb'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'We never disappoint'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Vast'
    feature3.details = 'We have varieties of services '

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.details = 'Are prices are affordable and higly competitive'
    features = [feature1, feature2, feature3, feature4]
    return render(request, 'index.html', {'features': features}) 

def counter(request):
    comment = request.POST['comment']
    count = len(comment.split())
    return render(request, 'counter.html', {'count': count}) 