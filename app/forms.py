from django import forms
from .models import Channel

class ChannelForm(forms.ModelForm):
	class Meta:
		model = Channel
		fields = ('name', 'category',)
		widgets = {
			'name':forms.TextInput(attrs={'placeholder':'enter your channel name','class':'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'}),
            'category':forms.Select(attrs={'class':'border rounded w-full py-2 px-4 outline-none focus:shadow-outline'})
		}