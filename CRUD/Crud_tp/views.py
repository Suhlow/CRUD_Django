from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.views.generic import ListView, DetailView

#READ
class IndexView(ListView):
 template_name='Crud_tp/index.html'
 context_object_name = 'post_list'
 def get_queryset(self):
  return Post.objects.all()

#READ(DETAIL)
class PostDetailView(DetailView):
 model=Post
 template_name = 'Crud_tp/post-detail.html'

#CREATE
def postview(request):
 if request.method == 'POST':
  form = PostForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = PostForm()
 return render(request,'Crud_tp/post.html',{'form': form})

#EDIT
def edit(request, pk, template_name='Crud_tp/edit.html'):
    post= get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#DELETE
def delete(request, pk, template_name='Crud_tp/confirm_delete.html'):
    post= get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':post})