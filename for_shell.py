from rango.models import *
from rango.views import *

users = User.objects.all()
profile = UserProfile.objects.all()
for profile in profile:
  user = profile.user
  update_user_groups_permission(user, profile)
  print user, profile.user_cls, user.groups.all()

buyers = [u for u in users if is_buyer(u)]
sellers = [u for u in users if not is_buyer(u)]
for u in buyers:
  add_user_permission(u)

for u in buyers:
  print u.user_permissions.all()

jean = User.objects.get(username='jean')
o = Order.objects.get_or_create(user=jean, id='123')[0]
p = Product.objects.all()[0]
o.products.add(p)

sam = User.objects.get(username='sam')
sam.order_set.all()

ted = User.objects.get(username='ted')
ted.product_set.all()

for p in Product.objects.all():
  print p.order_set.all()

product = Product.objects.all()[0]
buyers = [order.user for order in product.order_set.all()]

product = Product.objects.get(product_num=2)
buyers = [order.user for order in product.order_set.all()]
for u in buyers:
  print u.get_username(), u.email


c = Category.objects.get(name='Music')
 [p for p in women if c in p.categories.all()]

comment = Comment.objects.all()[0]

reply = Reply(comment=comment, product=comment.product, content="Can't agree more!", user=ted)
reply.save()

jenny = User.objects.get(username='jenny')
reply = Reply(comment=comment, product=comment.product, content="Absolutely!", user=jenny)
reply.save()

for c in Comment.objects.all():
  print c.pk
