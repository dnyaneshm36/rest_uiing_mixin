
from django import forms
from .models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields=[
            'user',
            'content',
            'image',
        ]


        
    def clean_content(self ):
        content = self.cleaned_data.get('content')
        if len(content) >200:
            raise forms.ValidationError('content too loong.')
        return content
    def clean(self):
        print("fuck this is not working")
        data = self.cleaned_data
        print(data)

        content = data.get('content',None)
        if content  == "":
            content= None
            raise forms.ValidationError('content required.')
        image = data.get("image",None)
        if content is None and image is None:
            raise forms.ValidationError('content or image is required.')
        return super().clean()
