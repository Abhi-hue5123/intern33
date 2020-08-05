from django.shortcuts import render
from .models import Destination
from .models import UserList
from .resources import UserListResource
from django.contrib import messages
from tablib import Dataset 
from django.http import HttpResponse


# Create your views here.
def index(response):
    
    '''dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Vizag'
    dest2.desc = 'The City of Destiny'
    dest2.img = 'destination_2.jpg'
    dest2.price = 1000
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.desc = 'The Silicon City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    dest3.offer = True

    dests = [dest1, dest2, dest3]'''

    dests = Destination.objects.all()

    return render(response, "socius/index.html", {'dests': dests})


def simple_upload(request):
    if request.method == 'POST':
        user_list = UserListResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'Wrong Format')
            return render(request, 'socius/upload.html')

        imported_data = dataset.load(new_person.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	#print(data[1])
        	value = UserList(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3]
        		)
        	value.save() 
    return render(request, 'socius/upload.html')

