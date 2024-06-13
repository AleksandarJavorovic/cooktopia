[Back to README.md](/README.md#manual-testing)

# Table of Contents

- [User Story Testing](#user-story-testing)
- [Validations](#validations)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [Lighthouse Scores](#lighthouse-scores)
- [Manual Testing](#manual-testing)
- [Browser Testing](#browser-testing)
- [Fixed Bugs](#fixed-bugs)
- [Present Bugs](#present-bugs)

## User Story Testing

| User Story | Features | Status |
|------------|------------------|------------|
| As a ***customer***, I can ***view listed products***, so that ***I can find something to buy***. | Given the All Products page, the user can easily view all of them in order to buy what he wants. | ✔ |
| As a ***customer***, I can ***view a detailed preview of the product***, so that ***I can get more information about it(price, description, image...)***. | Given the Product Detail page, user can easily see all the information about the product. | ✔ |
| As a ***customer***, I can ***search for the desired product by name or description***, so that ***I can find the specific product I want to buy***. | Given the search-bar within the navbar user can easily search for a desired product. | ✔ |
| As a ***customer***, I can ***see the total cost of the items in my bag***, so that ***I can see if I am getting out of my budget***. | Given the amount status under the shopping bag icon or when the user goes to the shopping bag page, total cost of the items is easily seen. | ✔ |
| As a ***customer***, I can ***sort specific categories of products***, so that ***I can find the cheapest/best-rated product in the given category***. | Given the groups of products within the navbar, as well as badges within the product info, the user can search through desired group of products and sort them as desired through sorting filters. | ✔ |
| As a ***customer***, I can ***sort the list of products***, so that ***I can easily find the best-priced/best-rated one***. | Given the filtering options, this is easily achievable. | ✔ |
| As a ***customer***, I can ***change the quantity of the added items within the shopping bag***, so that ***I can add/remove specific items if desired***. | Given the quantity button within the shopping bag, as well as Update/Remove buttons, the user can easily achieve this. | ✔ |
| As a ***customer***, I can ***easily view the items added to my shopping bag***, so that ***I can have an overview of the all items added and total cost***. | Given the toast messages, whenever the user adds something to the shopping bag, the toast message containing the items and total cost will pop up. The user can also visit shopping bag page to view all of this information as well. | ✔ |
| As a ***customer***, I can ***select the quantity of the products***, so that ***I can be sure to add the right quantity of the products to my shopping bag***. | Given the quantity button under the product image at the All Products page, or quantity button at the Product Detail page, this is easily achievable. | ✔ |
| As a ***customer***, I can ***enter my payment information***, so that ***I can checkout easily without any issues***. | Given the Form at the Checkout page, the user can easily fill out needed fields in order to checkout easily. | ✔ |
| As a ***customer***, I can ***have insight into the order confirmation details***, so that ***I can be sure I made no mistakes***. | After the successful checkout, the user is taken to Thank You page where all of the details are listed. The same order information are being saved within the My Profile->Order History section. | ✔ |
| As a ***customer***, I can ***get registered***, so that ***I can have a personal account/profile***. | Given the Sign Up page/Form the users can easily register at CookTopia site. | ✔ |
| As a ***customer***, I can ***view my profile***, so that ***I can view my order history and save/update shipping/paying information***. | Given the My Profile page where both Delivery Information and Order History sections are the authenticated user can do both things easily. | ✔ |
| As a ***customer***, I can ***receive the confirmation email***, so that ***I can be sure everything went well and keep it for just in case***. | Given the developed mailing system, after successful checkout, the user gets an email with all of those information. | ✔ |
| As a ***customer***, I can ***receive email confirmation after filling in the register form***, so that ***I can verify my account registration was successful***. | After successfully registering at CookTopia, the user gets an confirmation e-mail with confirmation link within. | ✔ |
| As a ***customer***, I can ***add items to wishlist***, so that ***I don't need to search for them all over again when I decide to buy them***. | Given the Wishlist page, and Heart button at Product Detail page, this is easily achievable. | ✔ |
| As a ***customer***, I can ***recover my password***, so that ***I can get access to my account in case I forget my password***. | Given the Forgot Password? button under the Home and Sign In buttons at  Sign In page, user can easily retrieve forgotten password. | ✔ |
| As a ***customer***, I can ***rate the product I already bought***, so that ***I can leave positive/negative feedback***. | Given the Review section at the Product Detail page, and form with options to rate and write a comment, this is easily achievable. | ✔ |
| As a ***admin***, I can ***perform CRUD operations***, so that ***I can manipulate the site as desired***. | Given the Edit and Delete buttons both under the image of the product at the All Products page, as well at Product Detail page, the admins can perform CRUD operations. This is also achievable from the Django Admin Page.| ✔ |
| As a ***customer***, I can ***see if there are any special offers/deals***, so that ***I can enjoy the discounted price and save some money***. | At this point I've decided to skip on this feature. | ❌ |

[Back to Top](#table-of-contents)

## Validations

### HTML Validation

- For my HTML file validation I have used [HTML W3C Validator](https://validator.w3.org/).
- Since all of the pages had no errors and all of the screenshots are the same, I have included only one.

| Page | Screenshot | No Errors |
| --- | --- | --- |
| Home | ![Home](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Sign Up | ![Register](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Sign In | ![Sign In](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Empty Wishlist | ![Empty Wishlist](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Wishlist | ![Wishlist](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Empty Shopping Bag | ![Empty Shopping Bag](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Shopping Bag | ![Shopping Bag](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| All Products | ![All Products](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| All Knives | ![All Knives](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| All Pans | ![All Pans](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| All Pots | ![All Pots](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Accessories | ![Accessories](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Product Detail | ![Product Detail](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| My Profile | ![My Profile](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Privacy Policy | ![Privacy Policy](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Checkout | ![Checkout](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Thank You | ![Thank You](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Product Management | ![Product Management](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Edit | ![Edit](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| 404 | ![404](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Password Reset | ![Password Reset](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |
| Sign Out | ![Sign Out](static/images/validation-images/html-validation/1-home-page-validation.png) | ✔ |

[Back to Top](#table-of-contents)

### CSS Validation

- For CSS file validation I have used [CSS Jigsaw W3C Validator](https://jigsaw.w3.org/css-validator/).

| File | Screenshot | No Errors |
| --- | --- | --- |
| base.css | ![Base](static/images/validation-images/css-validation/base-css.png) | ✔ |
| checkout.css | ![Checkout](static/images/validation-images/css-validation/checkout-css.png) | ✔ |
| profile.css | ![Profile](static/images/validation-images/css-validation/profile-css.png) | ✔ |
| rating.css | ![Rating](static/images/validation-images/css-validation/rating-css.png) | ✔ |

[Back to Top](#table-of-contents)

### JS Validation

- For JS file validation I have used a Static Code Analysis Tool [JS Hint](https://jshint.com/).

| File | Screenshot | No Errors/Note |
| --- | --- | --- |
| shopping-bag(postloadjs) | ![Shopping Bag](static/images/validation-images/js-validation/1-shopping-bag-js.png) | ✔ |
| countryfield.js | ![Countryfield](static/images/validation-images/js-validation/2-countryfield-js.png) | ✔ |
| add_product.html(postloadjs) | ![Add Product](static/images/validation-images/js-validation/3-add-product-js.png) | ✔ |
| edit_product.html(postloadjs) | ![Edit Product](static/images/validation-images/js-validation/4-edit-product-js.png) | ✔ |
| quantity-input-script.html(script) | ![Quantity Input Script](static/images/validation-images/js-validation/5-quantity-input-script-js.png) | ✔ |
| sort_and_button.html(script) | ![Sort and Button Script](static/images/validation-images/js-validation/6-sort-and-button-js.png) | ✔ |
| stripe_elements.js | ![Stripe Elements](static/images/validation-images/js-validation/7-stripe-elements-js.png) | One undefined variable |

[Back to Top](#table-of-contents)

### Python Validation

- For Python file validation I have used [CI Python Linter](https://pep8ci.herokuapp.com/).
- All of the files are without errors.

| django app | admin.py | apps.py |forms.py | models.py | urls.py | views.py | extra |
|---------|----------|----------|-----------|---------|----------|-------|--------|
| checkout | ![checkout](static/images/validation-images/python-validation/checkout/checkout-admin.png) | ![checkout](static/images/validation-images/python-validation/checkout/checkout-apps.png) | ![checkout](static/images/validation-images/python-validation/checkout/checkout-forms.png) | ![checkout](static/images/validation-images/python-validation/checkout/checkout-models.png) | ![checkout](static/images/validation-images/python-validation/checkout/checkout-urls.png) | ![checkout](static/images/validation-images/python-validation/checkout/checkout-views.png) | signals.py![checkout](static/images/validation-images/python-validation/checkout/checkout-signals.png) webhook_handler.py![checkout](static/images/validation-images/python-validation/checkout/checkout-webhook-handler.png) |
| cooktopia | N/A | N/A | N/A | N/A | ![cooktopia](static/images/validation-images/python-validation/cooktopia/cooktopia-urls.png) | ![cooktopia](static/images/validation-images/python-validation/cooktopia/cooktopia-views.png) | N/A |
| home | N/A | ![home](static/images/validation-images/python-validation/home/home-apps.png) | N/A | N/A | ![home](static/images/validation-images/python-validation/home/home-urls.png) | ![home](static/images/validation-images/python-validation/home/home-views.png) | N/A |
| products | ![products](static/images/validation-images/python-validation/products/products-admin.png) | ![products](static/images/validation-images/python-validation/products/products-apps.png) | ![products](static/images/validation-images/python-validation/products/products-forms.png) | ![products](static/images/validation-images/python-validation/products/products-models.png) | ![products](static/images/validation-images/python-validation/products/products-urls.png) | ![products](static/images/validation-images/python-validation/products/products-views.png) | N/A |
| profile | N/A | ![profile](static/images/validation-images/python-validation/profile/profile-apps.png) | ![profile](static/images/validation-images/python-validation/profile/profile-forms.png) | ![profile](static/images/validation-images/python-validation/profile/profile-models.png) | ![profile](static/images/validation-images/python-validation/profile/profile-urls.png) | ![profile](static/images/validation-images/python-validation/profile/profile-views.png) | N/A |
| shopping_bag | N/A | ![shopping_bag](static/images/validation-images/python-validation/shopping-bag/shopping-bag-apps.png) | N/A | N/A | ![shopping_bag](static/images/validation-images/python-validation/shopping-bag/shopping-bag-urls.png) | ![shopping_bag](static/images/validation-images/python-validation/shopping-bag/shopping-bag-views.png) | bag_tools.py![shopping_bag](static/images/validation-images/python-validation/shopping-bag/shopping-bag-bag-tools.png) contexts.py![shopping_bag](static/images/validation-images/python-validation/shopping-bag/shopping-bag-contexts.png) |
| wishlist | ![wishlist](static/images/validation-images/python-validation/wishlist/wishlist-admin.png) | ![wishlist](static/images/validation-images/python-validation/wishlist/wishlist-apps.png) | N/A | ![wishlist](static/images/validation-images/python-validation/wishlist/wishlist-models.png) | ![wishlist](static/images/validation-images/python-validation/wishlist/wishlist-urls.png) | ![wishlist](static/images/validation-images/python-validation/wishlist/wishlist-views.png) | contexts.py![wishlist](static/images/validation-images/python-validation/wishlist/wishlist-contexts.png) signals.py![wishlist](static/images/validation-images/python-validation/wishlist/wishlist-signals.png) |

[Back to Top](#table-of-contents)

### Lighthouse Score

- There is space for improvement on certain pages, especially when it comes to accessibility, things that can be fixed are next:
  - Buttons do not have an accessible name
  - Links do not have a discernible name
  - Links rely on color to be distinguishable
  - Background and foreground colors of the links do not have a sufficient contrast ratio
- Lower performance scores on certain pages are due to the use of a lot of external libraries
- Due to time constraints at the moment it will stay as it is

| Page | Desktop | Mobile |
| ---- | ----------------- | -------- |
| Home | ![lighthouse](static/images/validation-images/lighthouse/desktop-home-page.png) | ![lighthouse](static/images/validation-images/lighthouse/mobile-home-page.png) |
| All Products | ![lighthouse](static/images/validation-images/lighthouse/desktop-all-products.png) | ![lighthouse](static/images/validation-images/lighthouse/mobile-all-products.png) |
| Single Product | ![lighthouse](static/images/validation-images/lighthouse/desktop-single-product.png) | ![lighthouse](static/images/validation-images/lighthouse/mobile-single-product.png) |
| Shopping Bag | ![lighthouse](static/images/validation-images/lighthouse/desktop-shopping-bag.png) | ![lighthouse](static/images/validation-images/lighthouse/mobile-shopping-bag.png) |
| Privacy Policy | ![lighthouse](static/images/validation-images/lighthouse/desktop-privacy-policy.png) | ![lighthouse](static/images/validation-images/lighthouse/mobile-privacy-policy.png) |

[Back to Top](#table-of-contents)

## Manual Testing

### Home Page / Navbar


| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| CookTopia | User heads to https://cooktopia-3a5b4620860d.herokuapp.com/ | CookTopia Home Page is loaded | ✔ |
| CookTopia Logo | Click | User is redirected to the Home Page | ✔ |
| Search bar | Click on the button while search bar is empty | User is redirected to All Products page, all products are rendered and toast message:"You didn't enter any search criteria!", appears | ✔ |
| Search bar | Click on the button while: "aaa" within search bar | User is redirected to Products page while none of products is rendered but small message:"0 Products found for "aaa"" | ✔ |
| Search bar | Click on the button while "knife" is present in the search bar | User is redirected to Products page, while 3 products are rendered as they have word knife present in: name, description, brand, material, country of origin, or category fields of the product, as well as small message saying: "3 Products found for "knife"" | ✔ |
| Search bar | Click on the button while any word in the: name, description, brand, material, country of origin, or category fields of the product is present in the search bar | User is redirected to the Products page and the product/s are rendered, with apropriate small message | ✔ |
| My Account/Not-Authenticated | Click | Drop down menu opens with 2 options: Register and Login | ✔ |
| My Account/Authenticated/User | Click | Drop down menu opens with 2 options: My Profile and Logout | ✔ |
| My Account/Authenticated/Admin | Click | Drop down menu opens with 3 options: Product Management, My Profile, and Logout | ✔ |
| Wishlist/Not-Authenticated | Click | User is redirected to Login Page and small toast message pops up, saying:"Sorry, you must log in to view your Wishlist." | ✔ |
| Wishlist/Authenticated/Not-Empty | Click | User is redirected to the wishlist page and products are rendered | ✔ |
| Wishlist/Authenticated/Empty | Click | User is redirected to the wishlist page, and message:"Your wishlist is empty at the moment. Click the 🤍 to add a product or 🖤 to remove the product from the wishlist.", is being rendered | ✔ |
| Shopping Bag/Not-Empty | Click | User is redirected to the shopping bag page and products present in the shopping bag are rendered | ✔ |
| Shopping Bag/Empty | Click | User is redirected to the shopping bag page and small message:"Your bag is empty." is rendered | ✔ |
| All Products | Click | Drop-down menu opens with the available options | ✔ |
| All Products > Any available option | Click | User is redirected to the products page sorted according to the chosen option | ✔ |
| Knives | Click | Drop-down menu opens with the available options | ✔ |
| Knives > Any available option | Click | User is redirected to the products page sorted according to the chosen option | ✔ |
| Pans | Click | Drop-down menu opens with the available options | ✔ |
| Pans > Any available option | Click | User is redirected to the products page sorted according to the chosen option | ✔ |
| Pots | Click | Drop-down menu opens with the available options | ✔ |
| Pots > Any available option | Click | User is redirected to the products page sorted according to the chosen option | ✔ |
| Accessories | Click | Drop-down menu opens with the available options | ✔ |
| Accessories > Any available option | Click | User is redirected to the products page sorted according to the chosen option | ✔ |

### Home Page / Main Section

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Shop Now Button | Click | User is redirected to the All Products page | ✔ |
| Mail Subscribe/No Entry | Click | A small info message pops up saying: "This field is required." | ✔ |
| Mail Subscribe/Invalid Entry | Click | A small info message pops up saying: "Please enter a valid email address." | ✔ |
| Mail Subscribe/Valid Entry | Click | A small info message pops up saying: "Thank you for subscribing!" | ✔ |

### Home Page / Footer

| Feature | Action             | Expected Result                 | Pass |
| ----- | -----------------| ------------------------------| ---------- |
| Social Network Icons | Click | New tab opens and the user is redirected to the chosen site | ✔ |
| Home | Click | User is redirected to the Home page | ✔ |
| All Products | Click | User is redirected to the All products page | ✔ |
| Knives | Click | User is redirected to the Knives page | ✔ |
| Pans | Click | User is redirected to the Pans page | ✔ |
| Pots | Click | User is redirected to the Pots page| ✔ |
| Accessories | Click | User is redirected to the Accessories page | ✔ |
| Privacy Policy | Click | User is redirected to the Privacy Policy page | ✔ |

[Back to Top](#table-of-contents)

## Browser Testing

- Complete functionality and layout of the site was tested across next browsers:

  | Browser     | Layout      | Functionality |
  | :---------: | :----------:| :-----------: |
  | Brave       | ✔          | ✔             |
  | Edge        | ✔          | ✔             |
  |  Opera GX   | ✔          | ✔             |
  |    Safari   | ✔          | ✔             |

[Back to Top](#table-of-contents)

### Fixed Bugs

- Some of the stubborn bugs can be found in the table under.

| Bug | Detail | Fix |
| -------- | -------- | -------- |
| Shopping Bag Quantity Button | Before fixing, users could press the "-" button even after 1(going to 0, -1, -2, and so on). The "+" button was disabled when the number hit 99, but users could enter numbers bigger than 99 by keyboard, so this needed fixing too, as the idea was to set 99 as the biggest possible amount to choose. | quantity_input_script.html was updated to fix those issues |
| Server Error (500) | In the case of a non-authenticated user, when the user wanted to open a product_detail page, a 500 Server Error was prompted. | ![500 Server Error Fix](static/images/bugs/500-server-error-fix.png) |
| Footer Bug | In the case of a page with no or little content, the footer was jumping up. | This issue was fixed by setting: min-height: 100vh;(body), flex-grow: 1;(allowing main container on the page to take all extra space), margin-top: auto;(footer) |
| Minus Qty Button | Minus Qty button within shopping bag wasn't functioning | Deleted redundant lines of code within quantity_input_script.html to fix the issue |
| Stripe 401 Error | After making the purchase I was getting 401 Error on Stripe | I made my development address public |
| Stripe 400 Error | After making the purchase I was getting 400 Error on Stripe | Had to adjust Stripe WH Secret |

[Back to Top](#table-of-contents)

### Present Bugs
 - There are no known bugs.

[Back to Top](#table-of-contents)
