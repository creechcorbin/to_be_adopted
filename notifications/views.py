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
        count = 0
        notification_list = []
        for notification in owner_notifications:
            if notification.seen == False:
                count += 1
                notification_list.append(notification.favorited_pet)
                notification.seen == True
                notification.save()
        return render(request, 'notifications.html', {'owner_notifications': owner_notifications, 'notification_list': notification_list, 'count': count})


# Don't think we actually need this, but leaving it here for now.
class NotificationCountView(TemplateView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            notifications = Notification.objects.filter(owner_of_favorited=user)
            count = 0
            for notification in notifications:
                if notification.seen == False:
                    count += 1
        else:
            count = 0
        return count


