from django.shortcuts import render, redirect


def home(request):
    return redirect("threads-all")


def threads(request, id=None):
    if request.method == "GET":
        if id is None:
            return render(request, 'forum/home.html', {})
        else:
            p = request.GET.get("p", default=1)
            data = {
                "id": id,
                "page": p,

                # @TODO: Remove debug values
                "next_page": int(p)+1,
                "next_id": int(id)+1
            }

        if int(p) > 1:
            data.update({"prev_page": int(p) - 1})
        if int(id) > 1:
            data.update({"prev_id": int(id) - 1})

        return render(request, 'forum/thread.html', data)

    elif request.method == "POST":
        if id is None:
            pass  # @TODO: Handle new thread creation
        else:
            pass  # @TODO: Handle new thread reply creation

    elif request.method == "DELETE":
        assert id is not None, "Thread deletion without id"
        # @TODO: Handle thread deletion

    elif request.method == "PATCH":
        assert id is not None, "Thread edit without id"
        # @TODO: Handle thread edit
