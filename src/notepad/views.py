# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .forms import NoteModelForm
from .models import Note

def create_view(request):

	form = NoteModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect('/home/')

	context = {
		'form': form
	}

	return render(request, "notepad/create.html", context)

def list_view(request):
	notes = Note.objects.all()
	context = {
		'object_list': notes
	}
	return render(request, "notepad/list.html", context)

def delete_view(request, id):
	item_to_delete = Note.objects.filter(pk=id)
	if item_to_delete.exists():
		if request.user == item_to_delete[0].users:
			item_to_delete[0].delete()
	return redirect('/notes/list')

def update_view(request, id):
	