from django import forms
from profanity import profanity


class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea, label='Write your question here', max_length=500, required=True, strip=True)

    def clean_question(self):
        text = self.cleaned_data['question']
        if profanity.contains_profanity(text):
            raise forms.ValidationError("The question is offensive.")
        return text


class AnswerForm(forms.Form):
    answer_from = forms.CharField(widget=forms.HiddenInput(), required=True)
    answer_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    answer = forms.CharField(widget=forms.Textarea,label='Write your answer here', max_length=1000, required=True, strip=True)

    def clean_answer(self):
        text = self.cleaned_data['answer']
        if profanity.contains_profanity(text):
            raise forms.ValidationError("The answer is offensive.")
        return text

