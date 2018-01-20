from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='Write your question here', max_length=500, required=True, strip=True)


class AnswerForm(forms.Form):
    question3 = forms.CharField(widget=forms.HiddenInput(attrs={
                'class': 'yuy'}), required=False)
    answer = forms.CharField(label='Write your answer here', max_length=1000, required=False, strip=True)
