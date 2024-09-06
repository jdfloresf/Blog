from apps.home.models import Home

# Proceso para recuperar y telefono y correo del registro home

def home_contact(request):
    home = Home.objects.latest('created')

    return {
        'phone': home.phone,
        'correo': home.conatct_email
    }