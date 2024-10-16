from django.shortcuts import render, redirect
from .models import Equipment, Booking

def equipment_list(request):
    equipments = Equipment.objects.all()  # This line fetches all equipment
    if request.method == 'POST':
        equipment_id = request.POST.get('equipment_id')
        days = int(request.POST.get('days'))
        equipment = Equipment.objects.get(id=equipment_id)
        booking = Booking(equipment=equipment, days=days)
        booking.save()
        return render(request, 'rentals/success.html', {'booking': booking})
    return render(request, 'rentals/equipment_list.html', {'equipments': equipments})
