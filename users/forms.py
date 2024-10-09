from django import forms
from django.contrib.auth import get_user_model


#Получения тякущей модели пользователя
User = get_user_model()

#Создание формы регистрации пользователя
class UserRegistrationFrom(forms.ModelForm):
    #Создание дополнительного поля пороля для повторного ввода при регистрации
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput)

    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('Пароли не совподают!')
        return cleaned_data['password2']

    class Meta:
        model = User
        fields = ('username', 'password',
                  'first_name', 'last_name', 'email',
                  'phone', 'citi')


class CustomPasswordChangeForm(forms.Form):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput)
    new_password_1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput)
    new_password_2 = forms.CharField(label="Повторить новый пароль", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password_1 = cleaned_data['new_password_1']
        new_password_2 = cleaned_data['new_password_2']
        old_password = cleaned_data['old_password']

        if new_password_1 and new_password_2 and new_password_1 != new_password_2:
            raise forms.ValidationError('Пароли не совподают!')

        if new_password_1 and new_password_2 and new_password_1 == new_password_2 and new_password_1 == old_password:
            raise forms.ValidationError('Пароль совподает с текущим!')

        return cleaned_data

