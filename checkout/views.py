from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51Jn5S2Evc0D4PDFxlRuxfhMqy2ESOZX5ZOfUgc2L0Alg3bxv9knkE9Ol995UNFkbuOPnsmCQ1R1IHuHh2Oik54iw00yzNef9wK',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
