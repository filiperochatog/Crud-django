from django.shortcuts import render, redirect
from .models import Contato
from .forms import ContatoForm

def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/lista_contatos.html', {'contatos': contatos})

def adicionar_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contatos')
    else:
        form = ContatoForm()
    return render(request, 'contatos/form_contato.html', {'form': form})

def editar_contato(request, pk):
    contato = Contato.objects.get(id=pk)
    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('lista_contatos')
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'contatos/form_contato.html', {'form': form})

def deletar_contato(request, pk):
    Contato.objects.get(id=pk).delete()
    return redirect('lista_contatos')
