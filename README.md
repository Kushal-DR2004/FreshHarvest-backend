user API

api/v1/users/register/

api/v1/user/login/

api/v1/user/account/  -- get and update the user account 

product api

api/v1/products/productitems/  -- get all product

api/v1/products/productitems/{id} - get a individual product - along with reviews and farmer details

api/v1/products/productitems?search='name' -- search product by name or description

Review Api
api/v1/products/reviews/   - post 

api/v1/products/reviews/{id}/like

api/v1/products/reviews/{id}/unlike

cart
api/v1/carts/cartitems/  -- get user cart

api/v1/carts/cartdetails/ -- add cart to the cartDetails

api/v1/carts/cart/cartdetails/{id}/increase/ -- increse cart product quantity

api/v1/carts/cart/cartdetails/{id}/decrease/

orders
api/v1/carts/orders   -- order the items , and get the all user order

api/v1/carts/discountapply/{id} -- apply discount to cart

api/v1/carts/discounts/    --- get all discount_code available

farmer
api/v1/farmers  -- get all farmers

api/v1/farmers/{id}  - get a farmer along with farm/- details and product details

