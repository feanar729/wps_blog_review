from django.shortcuts import redirect

from wpsblog.models import Post


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    image = request.POST.get("image")

    post = Post.objects.create(
        title=title,
        content=content,
        image=image,
    )

    return redirect(post)
