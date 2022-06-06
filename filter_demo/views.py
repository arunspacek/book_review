from django.shortcuts import render


def index(request):
	names = "Oliver,Queen,Is,Batman"
	return render(request, "index.html", {"names": names})

def greeting_view(request):
	books = {"The night rider": "Ben Author", "The Justice": "Don Abeman"}
	return render(request, 'simple_tag_template.html', {'username': 'Superman', "books": books})
