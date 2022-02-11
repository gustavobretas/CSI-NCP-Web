from django import forms


BOOK_CHOICES = (('Non-Fiction',
                 (('1', 'Deep Learning with Keras'),
                  ('2', 'Web Development with Django'))),
                ('Fiction',
                 (('3', 'Brave New World'),
                  ('4', 'The Great Gatsby'))))

RADIO_CHOICES = (('Value One', 'Value One'),
                 ('Value Two', 'Value Two'),
                 ('Value Three', 'Value Three'))


class ExampleForm(forms.Form):
    text_input = forms.CharField()
    password_input = forms.CharField(widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICES)
    books_you_own = forms.MultipleChoiceField(choices=BOOK_CHOICES)
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField(required=False)
    float_input = forms.FloatField(required=False)
    decimal_input = forms.DecimalField(max_digits=3)
    email_input = forms.EmailField(required=False)
    date_input = forms.DateField(required=False)
    date_input1 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial='Hidden Value')
