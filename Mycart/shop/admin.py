from django.contrib import admin

# Register your models here.

from .models import Product,ContactUs,Orders,OrderUpdate,ProductImage
class ProductImageAdmin(admin.StackedInline):
    model=ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageAdmin]

    class Meta:
        model=Product

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass



admin.site.register(ContactUs)
admin.site.register(Orders)
admin.site.register(OrderUpdate)