from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product,ContactUs,Orders,OrderUpdate,ProductImage
from math import ceil
import json

# Create your views here.

def index(request):
    #return HttpResponse('hello world')
    #products=Product.objects.all()
    #print(products)
    #prams={"no_os_slides":nslides,"product":products,"range":range(1,nslides+1)}
    #allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    allprods=[]
    prods=Product.objects.values('subcategory','id')
    cats={item['subcategory'] for item in prods}
    for cat in cats:
        products=Product.objects.filter(subcategory=cat)
        n=len(products)
        nslides=(n//4+ceil((n/4)-(n//4)))
        allprods.append([products,range(1,nslides),nslides])
    prams={"allprods":allprods}
    return render(request,'shop/index.html',prams)

def searchmatch(query,item):
    if query in (item.product_name.lower() or item.desc.lower() or item.category.lower()):
        return True
    else:
        return False
    # return False


def search(request):
    #return HttpResponse('this is search page')
    queryy=request.GET.get('search')
    query=queryy.lower()
    #print(query)
    allprods=[]
    prods=Product.objects.values('category','id')
    #print(prods)
    cats={item['category'] for item in prods}
    #print(cats)
    for cat in cats:
        filter_prods=Product.objects.filter(category=cat)
        #print(filter_prods,123)
        products=[]
        for item in filter_prods:
            if searchmatch(query,item):
                products.append(item)
        #products=[item for item in filter_prods if searchmatch(query,item)]
        #print(products,456)
        #print(products)
        n=len(products)
        nslides=(n//4+ceil((n/4)-(n//4)))
        if len(products)!=0:
            allprods.append([products,range(1,nslides),nslides])
    #print(allprods)
    prams={"allprods":allprods,"msg":""}
    if len(allprods)==0 or len(query)<=4:
        prams={'msg':"Please make sure to enter relevent search query"}
    return render(request,'shop/search.html',prams)

def about(request):
    return render(request,"shop/about.html")
    #return HttpResponse('this is about page')

def contact(request):
    #return HttpResponse('this is contact page')
    if request.method=="POST":
        #print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        #print(name,email,phone,desc)
        contact=ContactUs(username=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"shop/contact.html")

def tracker(request):
    #return HttpResponse('this is tracker page')
    if request.method=="POST":
        #print(request)
        #here value in bracket are those which are name in form at tracker.html-------
        orderid=request.POST.get('orderid','')
        email=request.POST.get('email','')
        try:
            #at left side values in bracket are above value
            order=Orders.objects.filter(order_id=orderid,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps({"status":'success',"updates":updates, "itemjson":order[0].items_json},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request,'shop/tracker.html')

def prodView(request,myid):
    #return HttpResponse('this is prodView page')
    #fetch the product using id
    product=get_object_or_404(Product, id=myid)
    prod_images=ProductImage.objects.filter(images=product)
    product=Product.objects.filter(id=myid)
    cat=product[0].subcategory
    prods=Product.objects.filter(subcategory=cat)
    n=len(prods)
    nslides=(n//4+ceil((n/4)-(n//4)))
    length=range(1,nslides)
    return render(request,"shop/productview.html",{'prod':product,'prod_images':prod_images,'prods':prods,'length':length})


def checkout(request):
    #return HttpResponse('this is checkout page')
    if request.method=="POST":
        #print(request)
        #here value in bracket are those which are name in form at checkout.html-------
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address1','')+" "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        #print(name,email,phone,desc)
        order=Orders(items_json=items_json,name=name,email=email,phone=phone,address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request,"shop/checkout.html",{"thank":thank,"id":id})
    return render(request,"shop/checkout.html")