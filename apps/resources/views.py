from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import Resources
from apps.user.models import User
from .utils import generate_cat_count_list
from .forms import PostResourceForm


# Create your views here.
def home_page(request):
    res_cnt = Resources.objects.all().count()
    user_cnt = User.objects.count()
    cnt_per_cat = Resources.objects.values("cat_id__cat").annotate(cnt=Count("cat_id"))

    # we could call it whatever, but to follow the convention, we will call it like this.
    context = {
        "res_cnt": res_cnt,
        "user_cnt": user_cnt,
        "cnt_per_cat": cnt_per_cat,
    }
    return render(request, "resources/home.html", context)


def home_page_old(request):
    res_cnt = Resources.objects.all().count()
    user_cnt = User.objects.count()
    cnt_per_cat = Resources.objects.values("cat_id__cat").annotate(cnt=Count("cat_id"))
    response = f"""
      <html>
         <h1>Welcome to ResourceShare</h1>
         
         <p>{res_cnt} resources and counting!</p>

         <h2>All Users</h2>
         <p>{user_cnt} Users and counting!</p>
         <h2>All Categories</h2>
         <ol>
            {generate_cat_count_list(cnt_per_cat)}
         </ol>
      </html>
      
    """
    return HttpResponse(response)


@login_required
def resource_detail(request, id):
    # set max viewed resources to store
    max_viewed_resources = 5
    # Get current value of the stored viewed resources if any, else return []
    viewed_resources = request.session.get("viewed_resources", [])

    res = (
        Resources.objects.select_related("user_id").prefetch_related("tags").get(pk=id)
    )

    # create the list to be stored in the session
    viewed_resource = [res.id, res.title]

    # remove it if it already exist. This is because we want it to be append at the start of the list
    if viewed_resource in viewed_resources:
        viewed_resources.remove(viewed_resource)

    # insert at index 0
    viewed_resources.insert(0, viewed_resource)

    # Get the limit
    viewed_resources = viewed_resources[:max_viewed_resources]

    # add it back to our session
    request.session["viewed_resources"] = viewed_resources

    context = {"res": res}
    return render(request, "resources/resource_detail.html", context)


def resource_detail_old(request, id):
    # res = Resources.objects.get(pk=id)
    res = (
        Resources.objects.select_related("user_id").prefetch_related("tags").get(pk=id)
    )

    response = f"""
      <html>
         <h1>{res.title}</h1>
         <p><b>User</b>: {res.user_id.username.capitalize()}</p>
         <p><b>Link</b>: {res.link}</p>
         <p><b>Description</b>: {res.description}</p>
         <p><b>Category</b>: {res.cat_id.cat}</p>
         <p><b>Tags</b>: {res.get_all_tags()}</p>
      </html>
   """
    return HttpResponse(response)


def post_resource_old(request):
    # Process the form here
    breakpoint()

    return render(
        request,
        "resources/post.html",
    )


@login_required
def post_resource(request):
    if request.method == "POST":
        # Bound state
        form = PostResourceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            breakpoint()

            # TODO: process and save in database. Manually add a user id for now.
            # TODO: redirect to a page that shows all list of resources
        else:
            # TODO: set an error message and render the bound form
            # TODO: display that error message in your browser as a non-field error
            pass
    else:
        # Unbound state
        form = PostResourceForm()
        context = {"form": form}
        return render(
            request,
            "resources/posts.html",
            context,
        )


class HomePage(TemplateView):
    template_name = "home_page.html"
