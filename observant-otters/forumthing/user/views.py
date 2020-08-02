from django.shortcuts import render


def message(request, id):
    if request.method == "DELETE":
        pass  # @TODO: Handle message deletion

    elif request.method == "PATCH":
        pass  # @TODO: Handle message edit
