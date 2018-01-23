from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea, label='Write your question here', max_length=500, required=True, strip=True)


class AnswerForm(forms.Form):
    answer_from = forms.CharField(widget=forms.HiddenInput(), required=True)
    answer_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    answer = forms.CharField(widget=forms.Textarea,label='Write your answer here', max_length=1000, required=True, strip=True)
