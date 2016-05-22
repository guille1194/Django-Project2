from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Promovido, Promotor
from django.views.generic import FormView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .forms import Registro, PromotorForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Permission
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ValidationError
import csv


# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def error(request):
    return render(request, 'home/error.html')

class RegistrarPromovido(FormView):
    template_name = 'home/RegistrarPromovido.html'
    form_class = Registro
    success_url = reverse_lazy('home')

    def form_valid(self, form):
            p = Promovido()
            promovidos  = Promotor.objects.get(nombre = form.cleaned_data['promotor'] )
            p.promovido_id = form.cleaned_data['promovido_id']
            p.promovido_nombre = form.cleaned_data['promovido_nombre']
            p.promotor = form.cleaned_data['promotor']
            p.voto = form.cleaned_data['voto']
            if promovidos.no_promovidos >= 10:
                return redirect('/error')
            else:
                p.save()
                promovidos.no_promovidos = promovidos.no_promovidos + 1
                promovidos.save()
            return super(RegistrarPromovido, self).form_valid(form)


    def get_context_data(self, **kwargs):
        ctx = super(RegistrarPromovido, self).get_context_data(**kwargs)
        ctx['Promotor'] = Promotor.objects.all()
        ctx['Promovido'] = Promovido.objects.all()
        return ctx

def login_app(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('No acct')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'home/home.html', {})

class RegistroPromotor(FormView):
    template_name = 'home/registro.html'
    form_class = PromotorForm
    success_url = reverse_lazy('home')

    def form_valid(self,form):
		user = form.save()
		p = Promotor()
		p.user = user
		p.nombre = user.first_name
		p.apellido = user.last_name
		p.no_promovidos = 0
		p.save()
		permiso = Permission.objects.get(codename='puede_ser_promotor')
		p.user.user_permissions.add(permiso)
		p.save()
		return super (RegistroPromotor, self).form_valid(form)

def ReportesUsuarios(request):
    return render(request ,'home/ru.html')

def ReportesEstadisticos(request):
    return render(request ,'home/re.html')

class Reporte_VotoSi(ListView):
    template_name = 'home/votosi.html'
    model = Promovido

class Reporte_VotoNo(ListView):
    template_name = 'home/votono.html'
    model = Promovido

class Reporte_Promotores(ListView):
    template_name = 'home/promotores.html'
    model = Promotor

class Reporte_Promovidos(ListView):
    template_name = 'home/promovidos.html'
    model = Promovido

def csv_No_Votaron(request):
	respuesta = HttpResponse(content_type='text/csv')
	respuesta['Content-Disposition'] = 'attachment; filename=votaron.csv'
	voto = csv.writer(respuesta)
	votaron = Promovido.objects.filter(voto="No")
	voto.writerow([votaron])
	return respuesta

def csv_Si_Votaron(request):
	respuesta = HttpResponse(content_type='text/csv')
	respuesta['Content-Disposition'] = 'attachment; filename=votaron.csv'
	voto = csv.writer(respuesta)
	votaron = Promovido.objects.filter(voto="Si")
	voto.writerow([votaron])
	return respuesta
