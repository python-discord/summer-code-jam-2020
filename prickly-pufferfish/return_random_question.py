import os
import random


class RandomQuestion():
    def question(self):

        path = "python_questions"

        names = os.listdir(path)
        # removes hidden files, just in case.
        names = [f for f in names if not f.startswith('.')]
        list_of_paths = []
        for root, dirs, files in os.walk(path):
            for f in files:
                x = os.path.join(root, f)
                list_of_paths.append(x)

        question = random.choice(list_of_paths)
        open_question = open(question, 'r')
        return open_question.read()

    def name(self):
        path = "python_questions"
        names = os.listdir(path)
        # removes hidden files, just in case.
        names = [f for f in names if not f.startswith('.')]
        name = random.choice(names)
        return name
