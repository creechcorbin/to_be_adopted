from django.shortcuts import render, reverse, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

from tbauser.models import AdoptUser
from tbauser.forms import Edit
# Create your views here.


@login_required
def user_detail_view(request, user_id):
    try:
        selected_user = AdoptUser.objects.get(id=user_id)
    except AdoptUser.DoesNotExist:
        return render(request, "404.html", status=404)
    return render(request, 'user_detail.html',
                  {'selected_user': selected_user})


def edit_user_view(request, user_id):
    form = None
    html = 'edit_profile.html'
    instance = AdoptUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = Edit(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('user_detail', args=[instance.id]))
    else:
        form = Edit(instance=instance)
        return render(request, html, {'form': form})
