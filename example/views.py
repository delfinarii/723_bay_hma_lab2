# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from models import Device, Shop, Buy

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        devices = Device.objects.all()
        shops = Shop.objects.all()
        buys = Buy.objects.all()
        context.update(
            {
                'devices': devices,
                'shops': shops,
                'buys': buys
            }
        )
        return context
