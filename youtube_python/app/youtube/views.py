from django.shortcuts import render
from django.views import View
from .models import Channel, Video

# Create your views here.


def homepage(request):
    return render(request, 'base.html')


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        most_recent_video = Video.objects.order_by('-datetime')[:8]
        most_recent_channel = Channel.objects.filter()

        channel = False
        print(request.user.username)
        if request.user.username != "":
            try:
                channel = Channel.objects.filter(user__username=request.user)
                print(channel)
                channel = channel.get()
            except Channel.DoesNotExist:
                channel = False
        return render(request, self.template_name, {'menu_active_item': 'home', 'most_recent_video': most_recent_video, 'most_recent_channel': most_recent_channel, 'channel': channel})
