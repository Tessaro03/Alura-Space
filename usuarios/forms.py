from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length= 100,
        widget= forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.. Fulano Silva",
                "color":"#000000"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite a Senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nomeCadastro = forms.CharField(
        label="Nome do Usuario",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.. Fulano Silva"
            }
        )
    )
    email = forms.CharField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.. Cleiton@email.com ",
            }
        )
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite a Senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite a Senha Novamente"
            }
        )
    )

    def clean_nomeCadastro(self):
        nome = self.cleaned_data.get('nomeCadastro')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('Espaços não são permitidos neste campo')
        return nome
    
    def clean_senha_2(self):
         senha_1 = self.cleaned_data.get("senha_1")
         senha_2 = self.cleaned_data.get("senha_2")
         if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("As senhas não pode ser igual")
            else:
                return senha_2