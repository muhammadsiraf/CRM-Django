from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views.generic.detail  import DetailView
from django.views.generic.list import ListView

from .models import Lead,User,User, Item, Instance_Item
from .forms import LeadForm, ItemForm, ItemInstanceForm, LeadFormModel

# Create your views here.
def index(request):
    return render(request, 'landing.html')


# KHUSUS LEAD
def home_view(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }

    return render(request, "lead_list.html",context = context)


def detail_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    context = {
        "lead":lead
    }
    return render(request, "lead_detail.html", context=context)

def update_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadFormModel(request.POST, instance=lead)
        if form.is_valid:
            form.save()
            return redirect('detail_lead', pk=pk)
    else:
        form = LeadFormModel(instance = lead)
        context = {
            'form' : form
            
        }
        return render(request, 'lead_update.html', context = context)


def create_lead(request):
    
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = Lead.objects.create(
                first_name = form.cleaned_data.get('lead_first_name'),
                last_name  = form.cleaned_data.get('lead_last_name'),
                age = form.cleaned_data.get('lead_age'),
                agent = form.cleaned_data.get('lead_agent'),
            )
            return redirect("index")
    else:
        form = LeadForm
    context = {
        'form':form
    }
    return render(request, "lead_create.html", context=context)

def delete_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.delete()
    return redirect('index')


# KHUSUS ITEMS

def item_list(request):
    items = Item.objects.all()
    context = {
        'items':items
    }
    return render(request, "item_list.html", context=context)

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item':item
    }
    return render(request, "item_detail.html", context=context)

def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("item-list")
    else:
        form = ItemForm()

    context = {
        'form':form
    }

    return render(request, "item_create.html", context=context)

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if item:
        if request.method=='POST':
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("item-list")
        else:
            form = ItemForm(instance = item)

    context = {
        'form':form
    }

    return render(request, "item_update.html", context=context)

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)

    item.delete()
    return redirect('item-list')


# Instance Item
class InstanceItemDetail(TemplateView):
    template_name = 'InstanceDetail.html'


class InstanceDetail(DetailView):
    model = Instance_Item
    template_name = 'InstanceDetail.html'

    def get_context_data(self, pk):
        context = super().get_context_data()
        context['instances'] = Instance_Item.objects.get(pk=pk)

class InstanceListperUser(ListView):

    template_name = 'instance_item_list.html'
    model = Instance_Item
    paginated_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instances'] = Instance_Item.objects.filter(lead__pk=self.kwargs['user_id'])  
