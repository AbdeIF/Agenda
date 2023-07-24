from django.shortcuts import render, redirect

from portal.models import Contato
from portal.forms import ContatoForm

def home(request):
    contatos = Contato.objects.all()
    context = {
        'contatos': contatos
    }
    return render(request, 'portal/home.html', context=context)

def contato_add(request):
    form = ContatoForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'portal/contato_add.html', context=context)

def contato_edit(request, pk):
    #informando a chave primária do usuário a ser editado
    u = Contato.objects.get(pk=pk)
    if request.method == "POST":
        u.nome = request.POST.get('nome', None)
        u.sobrenome = request.POST.get('sobrenome', None)
        u.email = request.POST.get('email', None)
        u.data_nascimento = request.POST.get('data_nascimento', None)
        u.save()
        return redirect('home')
    context = {
    'contato': u
    }
    return render(request, 'portal/contato_edit.html', context)

def contato_delete(request,pk):
    contato = Contato.objects.get(pk=pk)
    contato.delete()
    return redirect('home')
