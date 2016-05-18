from django.contrib import messages
from django.core import validators
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from math import pi

from . import forms
from . import models

# Create your views here.
def hello_nuzz(request):
    return render(request, 'converter/hello_nuzz.html')


def times_two_view(request):
    form = forms.TimesTwoForm()
    if request.method == 'POST':
        form = forms.TimesTwoForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            messages.add_message(
                request,
                messages.SUCCESS,
                '{} * 2 = {}'.format(number, number * 2)
            )
            return HttpResponseRedirect(reverse('converter:times_two'))
    # answer = form['number'] * 2
    return render(request, 'converter/times_two.html', {'form': form})


def ctof_view(request):
    form = forms.CtoFForm()
    if request.method == 'POST':
        form = forms.CtoFForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            if form.cleaned_data['tempurature'].lower() == 'c':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "{} Celsius is {} Fahrenheit!".format(
                        number, round(number * (9 / 5) + 32, 2)
                    ))
            else:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "{} Fahrenheit is {} Celsius!".format(
                        number, round((number - 32) * (5 / 9), 2)
                    ))
            return HttpResponseRedirect(reverse('converter:tempurature'))
    return render(request, 'converter/tempurature.html', {'form': form})


def distance_view(request):
    form = forms.DistanceForm()
    if request.method == 'POST':
        form = forms.DistanceForm(request.POST)
        if form.is_valid():
            xyz = 1
            if form.cleaned_data['start'] == 'feet' and form.cleaned_data['end'] == 'meter':
                xyz = .3048
            elif form.cleaned_data['start'] == 'meter' and form.cleaned_data['end'] == 'feet':
                xyz = 3.28084
            elif form.cleaned_data['start'] == 'inches' and form.cleaned_data['end'] == 'centimeters':
                xyz = 2.54
            elif form.cleaned_data['start'] == 'centimeters' and form.cleaned_data['end'] == 'inches':
                xyz = .393701
            elif form.cleaned_data['start'] == 'miles' and form.cleaned_data['end'] == 'kilometers':
                xyz = 1.60934
            elif form.cleaned_data['start'] == 'kilometers' and form.cleaned_data['end'] == 'miles':
                xyz = 0.621371

            elif form.cleaned_data['start'] == 'feet' and form.cleaned_data['end'] == 'inches':
                xyz = 12
            elif form.cleaned_data['start'] == 'inches' and form.cleaned_data['end'] == 'feet':
                xyz = 1/12
            elif form.cleaned_data['start'] == 'feet' and form.cleaned_data['end'] == 'centimeters':
                xyz = 30.48
            elif form.cleaned_data['start'] == 'centimeters' and form.cleaned_data['end'] == 'feet':
                xyz = 1 / 30.48
            
            elif form.cleaned_data['start'] == 'meters' and form.cleaned_data['end'] == 'inches':
                xyz = 39.3701
            elif form.cleaned_data['start'] == 'inches' and form.cleaned_data['end'] == 'meters':
                xyz = 1 / 39.3701
            elif form.cleaned_data['start'] == 'meters' and form.cleaned_data['end'] == 'centimeters':
                xyz = 100
            elif form.cleaned_data['start'] == 'centimeters' and form.cleaned_data['end'] == 'meters':
                xyz = 1 / 100
            
            elif form.cleaned_data['start'] == 'miles' and form.cleaned_data['end'] == 'feet':
                xyz = 5280
            elif form.cleaned_data['start'] == 'feet' and form.cleaned_data['end'] == 'miles':
                xyz = 1 / 5280
            elif form.cleaned_data['start'] == 'miles' and form.cleaned_data['end'] == 'meters':
                xyz = 1609.34
            elif form.cleaned_data['start'] == 'meters' and form.cleaned_data['end'] == 'miles':
                xyz = 1 / 1609.34

            elif form.cleaned_data['start'] == 'miles' and form.cleaned_data['end'] == 'inches':
                xyz = 63360
            elif form.cleaned_data['start'] == 'inches' and form.cleaned_data['end'] == 'miles':
                xyz = 1 / 63360
            elif form.cleaned_data['start'] == 'miles' and form.cleaned_data['end'] == 'centimeters':
                xyz = 160934
            elif form.cleaned_data['start'] == 'centimeters' and form.cleaned_data['end'] == 'miles':
                xyz = 1 / 160934

            elif form.cleaned_data['start'] == 'kilometers' and form.cleaned_data['end'] == 'meters':
                xyz = 1000
            elif form.cleaned_data['start'] == 'meters' and form.cleaned_data['end'] == 'kilometers':
                xyz = 1 / 1000
            elif form.cleaned_data['start'] == 'kilometers' and form.cleaned_data['end'] == 'feet':
                xyz = 3280.84
            elif form.cleaned_data['start'] == 'feet' and form.cleaned_data['end'] == 'kilometers':
                xyz = 1 / 3280.84

            elif form.cleaned_data['start'] == 'kilometers' and form.cleaned_data['end'] == 'inches':
                xyz = 39370.1
            elif form.cleaned_data['start'] == 'inches' and form.cleaned_data['end'] == 'kilometers':
                xyz = 1 / 39370.1
            elif form.cleaned_data['start'] == 'kilometers' and form.cleaned_data['end'] == 'centimeters':
                xyz = 100000
            elif form.cleaned_data['start'] == 'centimeters' and form.cleaned_data['end'] == 'kilometers':
                xyz = 1 / 100000
            
            else:
                xyz = 1
            
            messages.add_message(
                request,
                messages.SUCCESS,
                "{} {} = {} {}!".format(
                    form.cleaned_data['number'],
                    form.cleaned_data['start'],
                    round(form.cleaned_data['number'] * xyz, 4),
                    form.cleaned_data['end']
                ))
            return HttpResponseRedirect(reverse('converter:distance'))
    return render(request, 'converter/distance.html', {'form': form})


def calculator_view(request):
    form = forms.CalculatorForm()
    if request.method == 'POST':
        form = forms.CalculatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['formula'].split()
            num = 0
            total = 0
            sign = ''
            for value in data:
                try:
                    value = float(value)
                    if sign == '+':
                        total += value
                    elif sign =='-':
                        total = total - value
                    elif sign =='*':
                        total = total * value
                    elif sign =='/':
                        total = total / value
                    else:
                        total = total + value
                except ValueError:
                    if value in '*/+-':
                        sign = value
            messages.add_message(
                request,
                messages.SUCCESS,
                "{}".format(round(total, 2)))              
            return HttpResponseRedirect(reverse('converter:calculator'))
    return render(request, 'converter/calculator.html', {'form': form})


def tip_calc_view(request):
    form = forms.TipCalcForm()
    if request.method == 'POST':
        form = forms.TipCalcForm(request.POST)
        if form.is_valid():
            total_bills = form.cleaned_data['total_bills']
            tip = form.cleaned_data['tip']
            split = form.cleaned_data['split']
            messages.add_message(
                request,
                messages.SUCCESS,
                "Tip: {}".format(round( total_bills * tip / 100, 2)))
            try:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Total: {}".format(round(
                            (total_bills + total_bills *  tip / 100) / split, 2)))
            except TypeError:
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Total: {}".format(round(
                            total_bills + total_bills *  tip / 100, 2)))
            return HttpResponseRedirect(reverse('converter:tipcalc'))
    return render(request, "converter/tip_calc.html", {'form': form})
                


def circle_view(request):
    shape = get_object_or_404(models.Shape, pk=3)
    form = forms.CircleForm()
    if request.method == 'POST':
        form = forms.CircleForm(request.POST)
        if form.is_valid():
            radius = form.cleaned_data['radius']
            if form.cleaned_data['measurement'].lower() == 'area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Area of circle is {}".format(
                        round(pi * radius ** 2, 2)
                    ))
            elif form.cleaned_data['measurement'].lower() == 'surface area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Surface area of circle is {}".format(
                        round(2 * pi * radius, 2)
                        ))
            return HttpResponseRedirect(reverse('converter:circle'))
    return render(request, 'converter/shape.html', {'form': form, 'shape': shape})


def rectangle_view(request):
    shape = get_object_or_404(models.Shape, pk=2)
    form = forms.RectangleForm()
    if request.method == 'POST':
        form = forms.RectangleForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            length = form.cleaned_data['length']
            if form.cleaned_data['measurement'].lower() == 'area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Area of rectangle is {}".format(
                        round(height * length, 2)
                    ))
            elif form.cleaned_data['measurement'].lower() == 'surface area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Surface area of rectangle is {}".format(
                        round(2 * (height + length), 2)
                    ))
            return HttpResponseRedirect(reverse('converter:rectangle'))
    return render(request, 'converter/shape.html', {'form': form, 'shape': shape})


def triangle_view(request):
    shape = get_object_or_404(models.Shape, pk=1)
    form = forms.TriangleForm()
    if request.method == 'POST':
        form = forms.TriangleForm(request.POST)
        if form.is_valid():
            side1 = form.cleaned_data['side1']
            side2 = form.cleaned_data['side2']
            side3 = form.cleaned_data['side3']
            if form.cleaned_data['measurement'].lower() == 'area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Area of triangle is {}".format(
                        round(side1 * side2 / 2, 2)
                    ))
            elif form.cleaned_data['measurement'].lower() == 'surface area':
                try:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "Surface area of triangle is {}".format(
                            round(side1 + side2 + side3, 2)))
                except TypeError:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "side3 needs to be filled if you want to measure the surface area")
            return HttpResponseRedirect(reverse('converter:triangle'))
    return render(request, 'converter/shape.html', {'form': form, 'shape': shape})


def cube_view(request):
    shape = get_object_or_404(models.Shape, pk=4)
    form = forms.CubeForm()
    if request.method == 'POST':
        form = forms.CubeForm(request.POST)
        if form.is_valid():
            side1 = form.cleaned_data['side1']
            side2 = form.cleaned_data['side2']
            side3 = form.cleaned_data['side3']
            if form.cleaned_data['measurement'].lower() == 'area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Area of cube is {}".format(
                        round(side1 * side2 * side3, 2)
                    ))
            elif form.cleaned_data['measurement'].lower() == 'surface area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Surface area of cube is {}".format(
                        round((2 * side1 * side2) + (2 * side2 * side3) +
                              (2 * side1 * side3), 2)
                    ))
            return HttpResponseRedirect(reverse('converter:cube'))
    return render(request, 'converter/shape.html', {'form': form, 'shape': shape})


def sphere_view(request):
    shape = get_object_or_404(models.Shape, pk=5)
    form = forms.SphereForm()
    if request.method == 'POST':
        form = forms.SphereForm(request.POST)
        if form.is_valid():
            radius = form.cleaned_data['radius']
            if form.cleaned_data['measurement'].lower() == 'area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Area of sphere is {}".format(
                        round((4 / 3) * pi * radius ** 3, 2)
                    ))
            elif form.cleaned_data['measurement'].lower() == 'surface area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Surface area of sphere is {}".format(
                        round(4 * pi * radius ** 2, 2)
                    ))
            return HttpResponseRedirect(reverse('converter:sphere'))
    return render(request, 'converter/shape.html', {'form': form, 'shape': shape})


def cylinder_view(request):
    shape = get_object_or_404(models.Shape, pk=6)
    form = forms.CylinderForm()
    if request.method == 'POST':
        form = forms.CylinderForm(request.POST)
        if form.is_valid():
            radius = form.cleaned_data['radius']
            height = form.cleaned_data['height']
            if form.cleaned_data['measurement'].lower() == 'area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Area of cylinder is {}".format(
                        round((pi * radius ** 2) * height, 2)
                    ))
            elif form.cleaned_data['measurement'].lower() == 'surface area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Surface area of cylinder is {}".format(
                        round((2 * pi * radius * height) + (2 * pi * radius**2), 2)
                    ))
            return HttpResponseRedirect(reverse('converter:cylinder'))
    return render(request, 'converter/shape.html', {'form': form, 'shape': shape})


def pyramid_view(request):
    shape = get_object_or_404(models.Shape, pk=7)
    form = forms.PyramidForm()
    if request.method == 'POST':
        form = forms.PyramidForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['measurement'].lower() == 'area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Area of pyramid is {}".format(
                        round((form.cleaned_data['length'] *
                               form.cleaned_data['width'] *
                               form.cleaned_data['height']) / 3, 2)
                    ))
            return HttpResponseRedirect(reverse('converter:pyramid'))
    return render(request, 'converter/shape.html', {'form': form, 'shape': shape})


def trapezoid_view(request):
    shape = get_object_or_404(models.Shape, pk=8)
    form = forms.TrapezoidForm()
    if request.method == 'POST':
        form = forms.TrapezoidForm(request.POST)
        if form.is_valid():
            base1 = form.cleaned_data['base1']
            base2 = form.cleaned_data['base2']
            side1 = form.cleaned_data['side1']
            side2 = form.cleaned_data['side2']
            if form.cleaned_data['measurement'].lower() == 'area':
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Area of trapezoid is {}".format(
                        round((base1 + base2) / 2 * side1, 2)
                    ))
            elif form.cleaned_data['measurement'].lower() == 'surface area':
                try:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "Surface area of trapezoid is {}".format(
                            round(base1 + base2 + side1 + side2, 2)
                        ))
                except TypeError:
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        "side2 needs to be filled if you want to measure the surface area")
            return HttpResponseRedirect(reverse('converter:trapezoid'))
    return render(request, 'converter/shape.html', {'form': form, 'shape': shape})
