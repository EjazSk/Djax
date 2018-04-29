# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView,CreateView,DetailView
from django.shortcuts import render
from .models import TweetModel
from .forms import TweetForm
from django.urls import reverse_lazy
# Create your views here.
# def Home(request):
# 	return render(request,'index.html',{})


class TweetList(ListView):
	model=TweetModel
	template_name = 'index.html'

	def get_context_data(self,*args,**kwargs):
		context = super(TweetList,self).get_context_data(*args,**kwargs)
		context['create_form']=TweetForm()
		context['create_url'] = reverse_lazy('create')
		return context



class CreateTweet(CreateView):
	model  = TweetModel
	template_name = 'create.html'
	form_class = TweetForm
	success_url = '/'

	def form_valid(self,form):
		form.instance.user= self.request.user
		form.save()
		return super(CreateTweet,self).form_valid(form)


class TweetDetail(DetailView):
	model = TweetModel
	template_name = 'detail.html'