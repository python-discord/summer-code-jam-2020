from django.forms import ModelForm, modelformset_factory

from trivia_builder.models import TriviaQuestion, TriviaQuiz


class TriviaQuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TriviaQuestion
        fields = ['question_text', 'question_answer']


class TriviaQuizForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TriviaQuiz
        fields = ['name']


TriviaQuestionFormSet = modelformset_factory(TriviaQuestion, form=TriviaQuestionForm, extra=3)
