from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from features.models import Feature, FeatureForm, Customer, AddCustomerForm
# from django.core.urlresolvers import reverse


# The render() function takes the request object as its first argument,
# a template name as its second argument and a dictionary as its optional third argument.

def index(request):
    latest_feature_list = Feature.objects.order_by('-created')
    context = {'latest_feature_list': latest_feature_list}
    return render(request, 'features/index.html', context)


def detail(request, feature_id):
    feature = get_object_or_404(Feature, pk=feature_id)
    if request.method == 'POST':  # If the form has been submitted...
        form = AddCustomerForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            customer, _ = Customer.objects.get_or_create(email=form.cleaned_data['customer_email'])
            feature.customers.add(customer)
            return render(request, 'features/detail.html', {'feature': feature})
    else:
        form = AddCustomerForm()  # An unbound form
    return render(request, 'features/detail.html', {'feature': feature})


def customers(request, feature_id):
    response = "These are the requesters for feature %s."
    return HttpResponse(response % feature_id)


def create_feature(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = FeatureForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            feature = form.save()
            customer, _ = Customer.objects.get_or_create(email=form.cleaned_data['customer_email'])
            feature.customers.add(customer)
            return HttpResponseRedirect('/features/')
    else:
        form = FeatureForm()  # An unbound form
    return render(request, 'features/new-feature.html', {'form': form})
