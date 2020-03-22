from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Destinations

# Create your views here.
""" solve the caroulsel issue """
def main_view(request):
    #Here need to make a destination var and get all objects
    #loop tem on the main page with nice cards
    show_destinations = Destinations.objects.all()

    # show_destinations is to loop destinations in the main page.
    return render(request, 'main.html', {'show_destinations': show_destinations})

    #make multiples carousels with different slides <<<<

def destinations(request):
    """
    This function will display the pagination
    if the number of elements are not > than
    the number of the 'paginator'==3 the Pagination
    will desappear.
    """
    destination = Destinations.objects.all()
    page = request.GET.get('page', 1)

    # Will display the number of elements per page, in this case 3.
    paginator = Paginator(destination, 3)

    try:
        destinations = paginator.page(page)
        print(destinations)

    except PageNotAnInteger:
        destinations = paginator.page(1)

    except EmptyPage:
        destinations = paginator.page(paginator.num_pages)

    return render(request, 'destinations.html', {'destinations': destinations})

def destination_details(request, id):
    # Get a singular destination, or return a 404
    details= get_object_or_404(Destinations, pk=id)
    template_name = 'details.html'
    post = get_object_or_404(Destinations, pk=id)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'details':details,
                                           'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
