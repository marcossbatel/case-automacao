*** Variables ***
# Login
${USERNAME_INPUT}    id:user-name
${PASSWORD_INPUT}    id:password
${LOGIN_BUTTON}    id:login-button

# Inventory
${INVENTORY_LIST}    class:inventory_list
${BACKPACK_ADD_BUTTON}    id:add-to-cart-sauce-labs-backpack
${CART_BADGE}    xpath://*[@class='shopping_cart_badge']
${CART_LINK}    xpath://a[@class='shopping_cart_link']

# Cart
${CART_TITLE}    Your Cart
${CART_ITEM_NAME}    Sauce Labs Backpack
${CHECKOUT_BUTTON}    id:checkout
${REMOVE_ITEM_BUTTON}    id:remove-sauce-labs-backpack

# Checkout
${FIRST_NAME_INPUT}    id:first-name
${LAST_NAME_INPUT}    id:last-name
${ZIP_CODE_INPUT}    id:postal-code
${CONTINUE_BUTTON}    id:continue
${FINISH_BUTTON}    id:finish
${CHECKOUT_COMPLETE_MESSAGE}    Thank you for your order!
