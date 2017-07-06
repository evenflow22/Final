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
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin


def handle(request):
    topic = request.GET.get('texttopic', "")
    my_user = request.user
    my_topic = Topic(topic_title=topic, topic_poster=my_user)
    my_topic.save()
    context_dict = {"topic": my_topic}
    return render(request, 'forums/handle.html', context_dict)


def AddTopic(request):
    context_dict = {}
    return render(request, 'forums/AddTopic.html', context_dict)



class PostTopic(CreateView):
    model = Post
    fields =['topic', 'poster', 'content', 'parent']


def post(request, post_id):
    my_post = Post.objects.get(pk=post_id)
    replies = Post.objects.filter(parent=my_post)
    context_dict = {'post': Post.objects.get(pk=post_id), 'replies': replies}
    return render(request, 'forums/post.html', context_dict)

def handlereply(request):
    newcomment_content = request.POST.get('reply')
    my_user = request.user
    mytopic_id = request.POST.get('my_topic', "")
    my_topic = Topic.objects.get(pk=mytopic_id)
    my_parent = request.POST.get('my_parent', "")
    parentpost = Post.objects.get(pk=my_parent)
    mypost = Post(topic=my_topic, poster=my_user, content=newcomment_content, parent=parentpost)
    mypost.save()
    return HttpResponseRedirect(reverse('forums:topic', kwargs={'pk': mytopic_id}))



class AddProfile(CreateView):
    model = Profile
    fields = ['user']

    def form_valid(self, form):
        form.instnace.created_by = self.request.user
        return super(AddProfile, self).form_valid(form)


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/forums/login/'
    redirect_field_name = ""
    template_name = 'forums/index.html'

    def get_queryset(self):
        return Topic.objects.all()


class DetailView(generic.DetailView):
    model = Topic
    template_name = 'forums/topic_page.html'

def newpost(request):
    newcomment_content = request.POST.get('newcomment')
    my_user = request.user
    mytopic_id = request.POST.get('my_topic', "")
    my_topic = Topic.objects.get(pk=mytopic_id)
    mypost = Post(topic=my_topic, poster=my_user, content=newcomment_content)
    mypost.save()
    context_dict = {"topic": my_topic}
    #return render(request, 'forums/handlesnewpost.html', context_dict)
    return HttpResponseRedirect(reverse('forums:topic', kwargs={'pk': mytopic_id}))
    #return HttpResponseRedirect(reverse('forums:index'))




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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('forums:index'))


            else:
                return HttpResponse("Invalid login details supplied.")

        else:
            print("invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Your HockeyTalk account is disabled.")

    else:
        context_dict = {}
        return render(request, 'forums/login.html', context_dict)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('forums:index'))


def search(request):
    context_dict = {}
    return render(request, 'forums/search.html', context_dict)

def searchpostresults(request):
    search = request.GET.get('post',"")
    context_dict = {'results': Post.objects.filter(Topic=search)}
    return render(request, 'forums/searchpostresults.html', context_dict)
