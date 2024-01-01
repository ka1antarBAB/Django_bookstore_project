from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from .models import Book
from .forms import CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


def book_detail_view(request, pk):
    #book
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.book = book #book
            comment.user = request.user
            comment.save()
            comment_form = CommentForm()
            redirect_url = reverse_lazy('books:book_detail')
    if request.method == 'GET':
        comment_form = CommentForm()
    return render(request, 'books/book_detail.html', context={
        'book': book,
        'comments': comments,
        'comment_form': comment_form,
    })


class BookCreateView(generic.CreateView):
    model = Book
    fields = ["title", "author", "description", "price", "cover", ]
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = "books/book_update.html"
    fields = ["title", "author", "description", "price", "cover", ]
    context_object_name = "books"


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy('books/book_list.html')
