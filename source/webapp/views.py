from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import GuestForm
from webapp.models import Guest, STATUS_CHOICES


def main_view(request):
    guests = Guest.objects.filter(status='active').order_by("created_at").reverse()
    return render(request, 'index.html', {'guests':guests})

def create_guest_view(request):
    if request.method == 'GET':
        form = GuestForm()
        return render(request, 'guest_create.html', {"status_choices":STATUS_CHOICES, "form":form})
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            new_guest = Guest.objects.create(name=name,
                                             email=email,
                                             text=text)
            return redirect("main_page")
        return render(request, "guest_create.html", {"form":form})

def update_guest_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        form = GuestForm(initial={
                        'name': guest.name,
                        'email': guest.email,
                        'text': guest.text})
        return render(request, 'guest_update.html', {"guest":guest, "form":form})
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.name = request.POST.get('name')
            guest.email = request.POST.get('email')
            guest.text = request.POST.get('text')
            guest.save()
            return redirect("main_page")
        return render(request, 'guest_update.html', {"guest": guest, "form": form})


def delete_guest_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        return render(request, "guest_delete.html", {"guest":guest})
    else:
        guest.delete()
        return redirect("main_page")
