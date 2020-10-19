from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from tbauser.models import AdoptUser
from pets.models import Pet
from notifications.models import Notification



class NotificationView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        owner_notifications = Notification.objects.filter(owner_of_favorited=user)
        notif_count = 0
        fav_count = 0
        notification_list = []
        prev_favorited_list = []
        for notification in owner_notifications:
            if notification.seen == False:
                notif_count += 1
                notification_list.append(notification.favorited_pet)
                notification.seen = True
                notification.save()
            else:
                fav_count += 1
                prev_favorited_list.append(notification.favorited_pet)
  
        return render(request, 'notifications.html', {'notification_list': notification_list, 'notif_count': notif_count, 'prev_favorited_list': prev_favorited_list, 'fav_count': fav_count})





