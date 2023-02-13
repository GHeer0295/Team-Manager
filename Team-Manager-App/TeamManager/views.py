from django.shortcuts import render, redirect
from .models import TeamMember
from .forms import TeamMemberForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class HomeView(ListView):
    model = TeamMember
    template_name =  'home.html'

class listDetailView(DetailView):
    model = TeamMember
    template_name = 'details.html'

class addMemberView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'add_new.html'

class UpdateTeamMemberView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'update.html'

def team_member_delete(request, pk):
    member = TeamMember.objects.get(pk=pk)
    member.delete()
    return redirect('home')