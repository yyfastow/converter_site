from django import forms
from django.core import validators

from . import models


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')

class TimesTwoForm(forms.Form):
    number = forms.FloatField()
    
    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get('number')


class CtoFForm(forms.Form):
    number = forms.FloatField()
    tempurature = forms.CharField(max_length=1)
    
    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get('number')
        tempurature = cleaned_data.get('tempurature')
        
        if tempurature not in ['C', 'c', 'F', 'f']:
            raise forms.ValidationError(
                "Type C for celsius and F for farenfeit only, not '{}'".format(cleaned_data['tempurature'])
            )


class DistanceForm(forms.Form):
    start = forms.CharField(max_length=50, label="start from")
    number = forms.FloatField()
    end = forms.CharField(max_length=50, label="to")

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get('number')
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')

        if start not in ['miles', 'kilometers', 'feet', 'meters', 'inches', 'centimeters']:
            raise forms.ValidationError("Only use listed value")
        elif end not in ['miles', 'kilometers', 'feet', 'meters', 'inches', 'centimeters']:
            raise forms.ValidationError("Only use listed value")

            

class CalculatorForm(forms.Form):
    formula = forms.CharField(max_length=355)
    
    def clean(self):
        cleaned_data = super().clean()
        formula = cleaned_data.get('formula')


class TipCalcForm(forms.Form):
    total_bills = forms.DecimalField(decimal_places=2, min_value=0.01)
    tip = forms.IntegerField(max_value=100, min_value=0, label="tip (by '%')")
    split = forms.IntegerField(max_value=100, min_value=0, required=False)

    def clean(self):
        cleaned_data = super().clean()


class CircleForm(forms.ModelForm):
    radius = forms.FloatField(min_value=0)
    class Meta:
        model = models.Shape
        fields = ['measurement']
        


    def clean(self):
        cleaned_data = super().clean()
        radius = cleaned_data.get('radius')


class RectangleForm(forms.ModelForm):
    height = forms.FloatField(min_value=0)
    length = forms.FloatField(min_value=0)

    class Meta:
        model = models.Shape
        fields = ['measurement']


    def clean(self):
        cleaned_data = super().clean()
        height = cleaned_data.get('height')


class TriangleForm(forms.ModelForm):
    side1 = forms.FloatField(min_value=0, label="height(area) / side1(parameter)")
    side2 = forms.FloatField(min_value=0, label="base(area) / side2(parameter)")
    side3 = forms.FloatField(min_value=0, required=False, label="side3(only needed for parameter)")
    
    class Meta:
        model = models.Shape
        fields = ['measurement']
    

    def clean(self):
        cleaned_data = super().clean()
        side1 = cleaned_data.get('side1')
        side2 = cleaned_data.get('side2')
        side3 = cleaned_data.get('side3')


class CubeForm(forms.ModelForm):
    side1 = forms.FloatField(min_value=0, label="length")
    side2 = forms.FloatField(min_value=0, label="width")
    side3 = forms.FloatField(min_value=0, label="height")
    
    class Meta:
        model = models.Shape
        fields = ['measurement']
    

    def clean(self):
        cleaned_data = super().clean()
        side1 = cleaned_data.get('side1')
        side2 = cleaned_data.get('side2')
        side3 = cleaned_data.get('side3')


class SphereForm(forms.ModelForm):
    radius = forms.FloatField(min_value=0)
    class Meta:
        model = models.Shape
        fields = ['measurement']
        


    def clean(self):
        cleaned_data = super().clean()
        radius = cleaned_data.get('radius')


class CylinderForm(forms.ModelForm):
    radius = forms.FloatField(min_value=0)
    height = forms.FloatField(min_value=0, label="height of sphere")
    class Meta:
        model = models.Shape
        fields = ['measurement']
        


    def clean(self):
        cleaned_data = super().clean()
        radius = cleaned_data.get('radius')
        height = cleaned_data.get('height')


class PyramidForm(forms.ModelForm):
    length= forms.FloatField(min_value=0, label="base length")
    width = forms.FloatField(min_value=0, label="base width")
    height = forms.FloatField(min_value=0, label="pyramid height")
    
    class Meta:
        model = models.Shape
        fields = ['measurement']
    

    def clean(self):
        cleaned_data = super().clean()
        length = cleaned_data.get('length')
        width = cleaned_data.get('width')
        height = cleaned_data.get('height')


class TrapezoidForm(forms.ModelForm):
    base1 = forms.FloatField(min_value=0)
    base2 = forms.FloatField(min_value=0)
    side1 = forms.FloatField(min_value=0, label="height(area) / side1(surface area)")
    side2 = forms.FloatField(min_value=0, required=False, label="side2(only needed for surface area)")
    
    class Meta:
        model = models.Shape
        fields = ['measurement']
    

    def clean(self):
        cleaned_data = super().clean()
        base1 = cleaned_data.get('base1')
        base2 = cleaned_data.get('base2')
        side1 = cleaned_data.get('side1')
        side2 = cleaned_data.get('side2')
