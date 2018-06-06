from django.shortcuts import render, render_to_response

# Create your views here.
from webapp.models import Store, StoreCategory

def homeView(request):
	shoppingCat=StoreCategory.objects.get(name__icontains='shopping')
	utilityCat=StoreCategory.objects.get(name__icontains='utility')
	return render(request, 'index.html', {
			'shoppingStores':shoppingCat.stores.filter(featured=True),
			'utilityStores':utilityCat.stores.filter(featured=True),
		})

def aboutView(request):
	return render(request, 'about.html', {})

def teamView(request):
	return render(request, 'team.html', {})

def contactView(request):
	return render(request, 'contact.html', {})

def categoryView(request, catName):
	category=StoreCategory.objects.filter(name__icontains=catName)
	return render(request, 'stores-list.html', {'category': category.first()})

def categoryListView(request):
	return render(request, 'categories.html', {'categories': StoreCategory.objects.all()})

def storeDetailView(request, pk):
	return render(request, 'store-details.html', {'store': Store.objects.get(pk=pk)})

def gallaryView(request):
	return render(request, 'gallery.html',{})