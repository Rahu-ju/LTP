from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from users.models import CustomUser


#If user created any topic, then it redirect the recent topic Page
# otherwise redirect the home page
@login_required(login_url='/users/login/')
def latest(request):
	try:
		topic = Topic.objects.filter(owner=request.user).latest('date_added')
		entries = topic.entry_set.order_by('date_added')
		if entries:
			context = {'topic': topic, 'entries': entries,}
		#return HttpResponseRedirect(reverse('learning_path_tracker:topic', args=(str(topic_id))))
			return render(request, 'learning_path_tracker/topic.html', context)
		else:
			topic_id = topic.id
			messages.info(request, 'you are not yet take anysteps on this goal.')
			return HttpResponseRedirect(reverse('learning_path_tracker:new_entry', args=[topic_id]))
	except ObjectDoesNotExist:
		topic = Topic.objects.filter(owner=request.user).latest('date_added')
		topic_id = topic.id
		messages.info(request, 'you are not yet take anysteps on this goal.')
		return HttpResponseRedirect(reverse('learning_path_tracker:new_entry', args=[topic_id]))


def index(request):
	'''The home page for learning log.'''

	if request.user.is_authenticated:
		# If user have any goal then redirect the user to the recent page
		# otherwise to home Page
		try:
			topic = Topic.objects.filter(owner=request.user).latest('date_added')
			return HttpResponseRedirect(reverse('learning_path_tracker:recent'))
		except Topic.DoesNotExist:
			messages.warning(request, 'You are not yet take any goal.Take one first.')
			return render(request, 'learning_path_tracker/index.html')
		# try:
		# 	topic = Topic.objects.filter(owner=user).latest('date_added')
		# 	topic_id = topic.id
		# 	return HttpResponseRedirect(reverse('learning_path_tracker:topic', args=(str(topic_id))))
		# except Topic.DoesNotExist:
		# 	pass
	return render(request, 'learning_path_tracker/index.html')

@login_required(login_url='/users/login/')
def topics(request):
	'''Show all topics.'''
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_path_tracker/topics.html', context)

@login_required(login_url='/users/login/')
def topic(request, topic_id):
	'''Show a single topic and its entries'''
	#it can help to get the specific topic
	#topic = Topic.objects.get(id=topic_id)

	#It can help to get the topic and fi topic not in the database it call 404.html in the main template
	topic = get_object_or_404(Topic, id=topic_id)

	# Make sure the topic belongs to the current user.
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('date_added')
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_path_tracker/topic.html', context)

@login_required(login_url='/users/login/')
def new_topic(request):
	'''Add a new topic.'''
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form = TopicForm()
	else:
		#POST data submitted; process data.
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			data = request.POST.get('text')
			new_topic.owner = request.user
			new_topic.save()
			topic = Topic.objects.get(text=data, owner=request.user)
			topic_id = topic.id
			return HttpResponseRedirect(reverse('learning_path_tracker:new_entry', args=[topic_id]))

	context = {'form':form}
	return render(request, 'learning_path_tracker/new_topic.html', context)

@login_required(login_url='/users/login/')
def new_entry(request, topic_id):
	'''Add a new entry for a particular topic'''
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		#No data submitted; create a blank form
		form = EntryForm()
	else:
		#POST data submitted; process data.
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_path_tracker:topic', args=[topic_id]))
	context = {'topic': topic, 'form':form}
	return render(request, 'learning_path_tracker/new_entry.html', context)

@login_required(login_url='/users/login/')
def edit_entry(request, entry_id):
	''' Edit an existing entry'''
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		#Initial request; prefill form with the current entry.
		form = EntryForm(instance=entry)
	else:
		#POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_path_tracker:topic', args=[topic.id]))

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_path_tracker/edit_entry.html', context)
