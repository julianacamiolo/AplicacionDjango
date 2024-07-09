from django import forms

class FormArticle(forms.Form):
    
    title = forms.CharField(
        label = "Titulo",
        max_length= 40,
        required=False,
        widget= forms.TextInput(
            attrs= {
                'placeholder': 'Mete el titulo',
                'class': 'titulo_forms_article'
            }
        )
    )

    title = forms.CharField(
        label = "Contenido", 
        widget = forms.Textarea
    )
    
    public_options = [
        (1,'Si'),
        (0, 'No')
    ]
    
    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )