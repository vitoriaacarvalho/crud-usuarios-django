from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256




def cadastro(request):
    status=request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def login(request):
    status=request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def valida_cadastro(request):
    nome= request.POST.get('nome')
    matricula=request.POST.get('matricula')
    senha=request.POST.get('senha')

    usuario = Usuario.objects.filter(matricula=matricula)

    if len(nome.strip()) == 0 or (matricula==0) :
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome,
                          senha = senha,
                          matricula=matricula)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')


def valida_login(request):
    matricula=request.POST.get('matricula')
    senha=request.POST.get('senha')
    
    
    senha=sha256(senha.encode()).hexdigest()

    usuario=Usuario.objects.filter(matricula=matricula).filter(senha=senha)

    if len(usuario)==0:
        return redirect('/auth/login/?status=1')

    elif len(usuario)>0:
        request.session['usuario']=usuario[0].id
        return redirect(f'#')

    return HttpResponse(f"{matricula} {senha}")


def sair(request):
    request.session.flush()
    return redirect('/auth/login/')

   #email ou senha invalidos
   #faça login antes de tentar acessar o sistema
   



# Create your views here.

