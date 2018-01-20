from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='Write your question here', max_length=500, required=True, strip=True)


class AnswerForm(forms.Form):
    answer = forms.CharField(label='Write your answer here', max_length=1000, required=True, strip=True)
