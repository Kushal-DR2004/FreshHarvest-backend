from django.contrib import admin

from .models import Product
from .models import Review
from .models import LikeReview
from .models import UnlikeReview

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(LikeReview)
admin.site.register(UnlikeReview)


