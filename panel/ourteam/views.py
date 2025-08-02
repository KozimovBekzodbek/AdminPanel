from django.shortcuts import render,redirect,get_object_or_404
from restoran import models
from panel.ourteam.forms import OurTeamForm

def OurTeamList(request):
    team = models.Ourteam.objects.all()
    return render(request, "panel/ourteam/list.html", {"team":team})


def OurTeamCreate(request):
    form = OurTeamForm()
    if request.POST:
        form = OurTeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ourteamlist') 
    return render(request, 'panel\ourteam\create.html', {"form":form})

        
def OurTeamUpdate(request, pk):
    old =  get_object_or_404(models.Ourteam, pk=pk)
    if request.POST:
        form = OurTeamForm(request.POST, request.FILES, instance=old)
        if form.is_valid():
            form.save()
            return redirect('ourteamlist') 
    form = OurTeamForm(instance=old)
    return render(request, 'panel/ourteam/update.html', {"form":form})



def OurTeamDelete(request, pk):
    object = get_object_or_404(models.Ourteam, pk=pk)
    object.delete()
    return redirect('ourteamlist')


    
