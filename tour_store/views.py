from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import CommentForm, ContactForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Destinations
from django.urls import reverse


# Create your views here.
def main_view(request):
    """
    This function loads the main page with destinations,
    and contact form.
    """
    show_destinations = Destinations.objects.all()
    # contacts = details.contact.filter(active=True)
    new_contact = None
    # Comment posted
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            # Create contact object but don't save to database yet
            new_contact = contact_form.save(commit=False)
            # Assign the current post to the comment
            # new_contact.post = details
            # Save the comment to the database
            new_contact.save()
            messages.success(request, "Our team will contact you as soon as possible.")
            return redirect(reverse("index"))
    elif request.user.is_authenticated:
        # Added username and email as default for contact form if user is authenticated
        contact_form = ContactForm(
            initial={"name": request.user.username, "email": request.user.email}
        )
    else:
        # Leave empty contact form for Anonymous User
        contact_form = ContactForm()

    # show_destinations is to loop destinations in the main page.
    return render(
        request,
        "main.html",
        {
            "show_destinations": show_destinations,
            "new_contact": new_contact,
            "contact_form": contact_form,
        },
    )


def destinations(request):
    """
    This function will display the pagination
    if the number of elements are not > than
    the number of destinations in destinations.
     if the 'paginator'==3 the Pagination
    will desappear.
    """
    destination = Destinations.objects.all()
    page = request.GET.get("page", 1)

    # Will display the number of elements per page, in this case 3.
    paginator = Paginator(destination, 3)

    try:
        destinations = paginator.page(page)

    except PageNotAnInteger:
        destinations = paginator.page(1)

    except EmptyPage:
        destinations = paginator.page(paginator.num_pages)

    return render(request, "destinations.html", {"destinations": destinations})


def destination_details(request, id):
    """
    This function will display the details page,
    with the coment form and comments.
    """
    # Get a singular destination, or return a 404
    details = get_object_or_404(Destinations, pk=id)
    comments = details.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = details
            # Save the comment to the database
            new_comment.save()
            messages.success(request, "Your comment is awaiting moderation.")
            # redirect user to the same page after submit a comment
            return redirect(reverse("destinationDetails", args=[details.id]))
    elif request.user.is_authenticated:
        # Added username and email as default for comment form if user is authenticated
        comment_form = CommentForm(
            initial={"name": request.user.username, "email": request.user.email}
        )
    else:
        # Leave empty comment form for Anonymous User
        comment_form = CommentForm()

    return render(
        request,
        "details.html",
        {
            "details": details,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
