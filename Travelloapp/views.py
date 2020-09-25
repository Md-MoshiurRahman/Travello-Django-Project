from django.shortcuts import render
from .models import Destination

# Create your views here.
def aboutus(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):  

    dests = Destination.objects.all()

    #########for static######
    #dest1 = Destination()
    #dest1.name = 'Dhaka'
    #dest1.desc = 'City of dreams'
    #dest1.img = 'destination_1.jpg'
    #dest1.price = 500
    #dest1.offer = False

    #dest2 = Destination()
    #dest2.name = "Cox's Bazar "
    #dest2.desc = 'Longest sea beach in the world'
    #dest2.img = 'destination_2.jpg'
    #dest2.price = 600
    #dest2.offer = True

    #dest3 = Destination()
    #dest3.name = 'Bandarban'
    #dest3.desc = 'Famous tourist spot'
    #dest3.img = 'destination_3.jpg'
    #dest3.price = 550
    #dest3.offer = False

    #dest4 = Destination()
    #dest4.name = 'Sajek'
    #dest4.desc = 'Land of clouds'
    #dest4.img = 'destination_4.jpg'
    #dest4.price = 400
    #dest4.offer = False

    #dest5 = Destination()
    #dest5.name = 'Kuakata'
    #dest5.desc = 'Land of sunrise'
    #dest5.img = 'destination_5.jpg'
    #dest5.price = 500
    #dest5.offer = False

    #dest6 = Destination()
    #dest6.name = 'Dinajpur'
    #dest6.desc = 'Lovely small town'
    #dest6.img = 'destination_6.jpg'
    #dest6.price = 250
    #dest6.offer = True

    #dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    #########################

    

    return render(request, 'index.html', {'dests' : dests})
    #return render(request, 'index1.html')