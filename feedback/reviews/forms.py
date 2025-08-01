from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label='Your name',max_length=10,required=True,error_messages={
#         'required':'Your name must not be empty',
#         'max_lenght':'Please enter a shorter name',
#     })

#     review_text=forms.CharField(label='Your Feedback',widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(label='Your rating',min_value=1,max_value=5,)

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        # fiels=['user_name',]
        # exclude=['owner_comment']
        labels={
            'user_name':"Enter your name",
            'review_text':"Enter your feedback",
            'rating':"Enter your ratings",
        }
        error_messages={
            'user_name':{
                'required':"Your name must not be empty!",
                'max_lenght':"Please enter a shorter name!"
            }
        }