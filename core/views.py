from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms import ContatoForm, ProdutoModelForm
from core.models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        #print('Post: ',request.POST)
        if form.is_valid():
            '''
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            print('Mensagem Enviada')
            print('Nome: ',nome)
            print('Email: ', email)
            print('Assunto: ', assunto)
            print('Mensagem: ', mensagem)
            '''
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }  
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                #prod = form.save(commit=False)
                #print("Nome: ",prod.nome," Preço: ",prod.preco," Estoque: ",prod.estoque," Imagem: ",prod.imagem)
                form.save()
                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')