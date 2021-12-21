from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import gallery, favorite
from django.http import JsonResponse
from django.contrib.auth.models import User
from .gallery_management import image_management, infinite_scroll
# Create your views here.

def tg2a(request):
    # Main page
    context = {
        "form": ImageForm(), # Form load for the add image element.
    }

    return render(request, "TG2A/tg2a.html", context)


def add_image(request):
    # Add image
    if request.method == 'POST':
        # Image add class/method. Check gallery_management.py for more info.
        image_management(user=request.user, form=ImageForm(request.POST, request.FILES)).add_image()

    return redirect("TG2A")

def image_page(request, img_id):
    # Image page (specific image page)
    img = gallery.objects.get(id=img_id) # Query for image.
    # Check if the image is mark as favorite for the person on the page. Check gallery_management.py for more info.
    response = image_management(user=request.user,form=img).check() # return the the response

    if request.method == "POST":
        print(request.POST)
        # Management of the favorite function. Check gallery_management.py for more info.
        image_management(user=request.user, form= img).fav(fav_form=request.POST['fav'])

    context = {
        "image": img,
        "fav": response,
    }

    return render(request, "TG2A/image_page.html", context)

def gallery_items(request, page_num):
    # Management of the pagination/infinite scroll. Check gallery_management.py for more info.
    response = infinite_scroll(gallery_content = gallery.objects.only("id", "thumbnail_url").order_by('-date'), page = request.GET.get('page', page_num))

    return JsonResponse({"items": list(response["items"].object_list.values()), "page": response["page_num"]})


def profile(request, user):
    # Query's for the profile page.
    user_1 = User.objects.get(username=user)
    fav = favorite.objects.filter(user=user_1, favorite = True)
    all_uploads = gallery.objects.filter(user=user_1)

    context = {
        "fav": fav,
        "user_profile": user,
        "all_uploads": all_uploads,
    }
    return render(request, "TG2A/profile.html", context)
