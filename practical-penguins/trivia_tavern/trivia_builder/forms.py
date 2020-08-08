from django.forms import ModelForm

from trivia_builder.models import TriviaQuestion, TriviaQuiz


class TriviaQuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question_text'].required = True
        self.fields['question_answer'].required = True

    class Meta:
        model = TriviaQuestion
        fields = ['question_text', 'question_answer']


class TriviaQuizForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True

    class Meta:
        model = TriviaQuiz
        fields = ['name', 'description']



