from django import forms
class question(forms.Form):
    category = forms.ChoiceField(choices=[('5','Professional'),('4','Excellent'),('3','Intermediate'),('2','Average'),('1','Beginner'),('0','Poor')])


