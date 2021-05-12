from django.shortcuts import render, redirect
from app import forms
from .models import Channel

def create_channel(request):
	user = request.user
	form = forms.ChannelForm()
	if request.method == 'POST':
		form = forms.ChannelForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			category = form.cleaned_data.get('category')
			Channel.objects.create(name=name, user=user, slug=user.username, category=category)
			return redirect('mychannel', slug=user.username)

		
	context = { 
		'form': form,
	}
	return render(request, 'channel/create.html', context)

def channel(request, slug):
	channel = Channel.objects.get(slug=slug)
	
	context = {
		'channel': channel
	}
	return render(request, 'channel/channel_home.html', context)

def edit_channel(request, slug):
	channel = Channel.objects.get(slug=slug)
	form = forms.EditChannelForm(instance=channel)

	if request.method == 'POST':
		form = forms.EditChannelForm(request.POST, request.FILES, instance=channel)
		if form.is_valid():
			form.save()
			return redirect('mychannel', slug=slug)

	context = {
		'edit_form': form
	}
	return render(request, 'channel/edit_channel.html', context)

