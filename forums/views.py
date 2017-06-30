from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, User, Topic, Profile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm


class AddTopic(CreateView):
    model = Topic
    fields = ['topic_title']


class IndexView(generic.ListView):
    template_name = 'forums/index.html'

    def get_queryset(self):
        return Topic.objects.all()


class DetailView(generic.DetailView):
    model = Topic
    template_name = 'forums/topic_page.html'


class UserFormView(View):
    form_class = UserForm
    template_name = 'forums/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # add to db

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('forums:index')

        return render(request, self.template_name, {'form': form})


def login_user(request):
    #return HttpResponse(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                #return HttpResponseRedirect(reverse('index'))
                return render(request, 'forums/index.html', {})

            else:
                return HttpResponse("Invalid login details supplied.")

        else:
            print("invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Your HockeyTalk account is disabled.")

    else:
        #return HttpResponseRedirect('../user_login.html')
        #return render(request, 'forums/login.html', {})
        context_dict = {}
        return render(request, 'forums/login.html', context_dict)










