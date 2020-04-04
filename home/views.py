from django.shortcuts import render
import shopify
from shopify_app.decorators import shop_login_required
from bs4 import BeautifulSoup
from .forms import CreateCollectionForm

@shop_login_required
def index(request):
    # products = shopify.Product.find(limit=3, order="created_at DESC")
    print("Got products")
    # orders = shopify.Order.find(limit=3, order="created_at DESC")
    # print("Got orders")
    # for product in products:
    #     print(f"{product.title}:  {product.id}")
    return render(request, 'home/test.html', {'products': []})



@shop_login_required
def normalize_description(request, product_id):
    product = shopify.Product.find(product_id)
    print("getting into if")
    if request.method=="GET":
        print(product)
        return render(request, 'home/normalize_description.html', {'product': product})
    else:
        html_doc = product.body_html
        soup = BeautifulSoup(html_doc, 'html.parser')
        try:
            new_description = soup.find("div", attrs={"class":'text-section'})
            # print(new_description, ":::" ,type(new_description))
            product.body_html = str(new_description)
            product.save()
        except:
            new_description = "<h1>COuld Not Do IT <h1>"
        return render(request, 'home/normalize_description.html', {'product': product, 'new_description': str(new_description)})



@shop_login_required
def remove_last_line(request):
    done = []
    not_done = []
    products = shopify.Product.find(limit=250, order="created_at ASC")
    for product in products:
        print("getting into if")
        html_doc = product.body_html
        try:
            print(f"Got Product {product.id}")
            to_remove = r'<div align="left" style="font-size: 17.5px;"><span style="font-size: 14pt;">**Please check out our updated eBay shop by clicking on the link above**</span></div>'
            to_remove2 = r'**Please check out our updated eBay shop by clicking on the link above**'
            new_description = html_doc.replace(to_remove, "")
            new_description = html_doc.replace(to_remove2, "")
            # print(new_description, ":::" ,type(new_description))
            product.body_html = new_description
            product.save()
            done.append(product)
        except:
            print("Could do it")
            not_done.append(product)
    return render(request, 'home/remove_last_line.html', {'not_done': not_done, 'done': done})


@shop_login_required
def create_collection(request):
    if request.method == "GET":
        form = CreateCollectionForm()
        collections = shopify.CustomCollection.find(limit=20)
        return render(request, 'home/create_collection.html', {'form': form, 'collections': collections})
    else:
        if form.is_valid():
            name = form.cleaned_data.get('name')
            try:
                collection = shopify.CustomCollection.create({'title': name})
            except:
                print("Couldnt create collection")
    return render(request, 'home/create_collection.html', {'form': CreateCollectionForm()})
        
    
@shop_login_required
def normalize_all_description(request):
    products = shopify.Product.find(limit=250, order="created_at DESC")
    done = []
    not_done = []
    for product in products:
        print("getting into if")
        if request.method=="GET":
            # print(product)
            return render(request, 'home/bulk_normalize.html', {'product': product})
        else:
            html_doc = product.body_html
            soup = BeautifulSoup(html_doc, 'html.parser')
            try:
                new_description = soup.find("div", attrs={"class":'text-section'})
                # print(new_description, ":::" ,type(new_description))
                product.body_html = str(new_description)
                product.save()
                done.append(product)
            except:
                not_done.append(product)
            
    return render(request, 'home/bulk_normalize.html', {'not_done': not_done, 'done': done})