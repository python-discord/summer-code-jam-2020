from django.forms import ModelForm
from django.utils.translation import ugettext_lazy

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
        self.fields['description'].required = True

    class Meta:
        model = TriviaQuiz
        fields = ['name', 'description']
        labels = {
            'name': ugettext_lazy('Trivia Pack Name'),
        }
