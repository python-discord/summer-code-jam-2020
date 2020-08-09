from django.shortcuts import render


# Create your views here.
def index(request):
    """Views to render the homepage index."""

    context = {
        "login": request.user.is_authenticated,
    }

    if request.user.is_authenticated:
        context["username"] = request.user.username

    return render(request, "home/index.html", context)


def about_us(request):
    """Views to render the About Us page."""

    context = {
        "login": request.user.is_authenticated,
        "page": "about_us",
        "devs": [
            Developer(
                "SleepeerSocks♡",
                "duaanmol2@gmail.com",
                """
                Anything new, Tell me about it. Like to see new projects,
                their progress and how you manage the project. New stuff?
                I'm in.
                """,
                "Team Leader",
                "dev-1.png"
            ),
            Developer(
                "iqrar99",
                "moonkiller1999@gmail.com",
                """
                A student who wants to be a Data Scientist and Software
                Engineer. Really love Python as a main programming
                language.
                """,
                "Developer",
                "dev-2.png"
            ),
            Developer(
                "Nabob",
                "https://git.io/JJMff",
                "A cool guy who loves programming and Container technologies",
                "Developer",
                "dev-4.png"
            ),
            Developer(
                "Music",
                "",
                "Contrary to name, zero involvement in music.",
                "Developer",
                "dev-3.png"
            ),
            Developer(
                "Soyybeans",
                "",
                "A passionate guy who interested with Python",
                "Developer",
                "dev-5.png"
            )
        ]
    }

    return render(request, "home/about.html", context)


def error_404_view(request, exception):
    """Views to render the 404 error page."""

    render(request, '404.html')


class Developer(object):
    """Class that contains all developer information
    for about-us page.
    """

    name: str
    email: str
    description: str
    role: str
    picture: str

    def __init__(self, name, email, description, role, picture):
        self.name = name
        self.email = email
        self.description = description
        self.role = role
        self.picture = picture
