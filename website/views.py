from django.shortcuts import render
from  website.models import Pessoa

# Create your views here.
def index(request):
    args = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        # tb é válido: pessoa.nome = request.POST['nome']
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.genero = request.POST.get('genero')
        pessoa.email = request.POST.get('email')
        pessoa.save()
        args = {'msf':'parabens'}
    return render(request,'index.html', args)

def sobre(request):
    args = {

    }
    return render(request,'sobre.html', args)