# CookTopia

CookTopia is an imaginary e-commerce site, selling modern, functional kitchenware. Currently, the e-store specializes in selling knives, pots, pans, and some extra accessories with the intention of expanding the scope.

Our target customers are anyone in need of functional, modern, high-quality products for domestic or professional use.

[CookTopia live project here.](https://cooktopia-3a5b4620860d.herokuapp.com/)

![Am I Responsive](static/images/am-I-responsive-cooktopia.png)

## Table of Contents

- [UI/UX](#uiux)
    - [Agile Development](#agile-development)
      - [MoSCoW Prioratization](#moscow-prioratization)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Site Goals](#site-goals)
    - [Design Choices](#design-choices)

- [Database Design](#database-design)
    - [Database Model](#database-model)
    - [Custom Models](#custom-models)

- [Features](#features)
    - [Home Page](#home-page)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [My Account](#my-account)
    - [Product Management](#product-management)
    - [My Profile](#my-profile)
    - [Wishlist](#wishlist)
    - [Shopping Bag](#shopping-bag)
    - [Secure Checkout](#secure-checkout)
    - [Thank You Page](#thank-you-page)
    - [Search Bar](#search-bar)
    - [All Products Page](#all-products-page)
    - [Product Page](#product-page)
    - [Review Section](#review-section)
    - [Authentication](#authentication)
    - [Password Reset](#password-reset)
    - [Additional Features](#additional-features)
    - [404 Page](#404-page)
    - [Future Features](#future-features)

- [Business Model](#business-model)

- [Technologies Used](#technologies-used)
    - [Work Environments and Hosting](#work-environments-and-hosting)
    - [Python Libraries](#python-libraries)
    - [Django Libraries](#django-libraries)
    - [Payment processing](#payment-processing)
    - [Emails/Newsletter](#emailsnewsletter)
    - [SEO/Marketing](#seomarketing)

- [Testing](#testing)
    - [Test Guide](#test-guide)
    - [Validator Testing](#validator-testing)
    - [Browser Testing](#browser-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)

- [Deployment](#deployment)

- [Development](#development)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Download ZIP](#download-as-zip)

- [Source Credits](#source-credits)
    - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
    - [Media and Styling](#media-and-styling)
    - [Content/Data](#contentdata)

## UI/UX

The design of the site is pretty simplistic yet modern I would say, with the easy-to-see navbar presenting the products the site is offering. The site follows a mostly black-and-white theme, where the fancy shade of red was used for some detailing.

The main background shows the first-time visitor what the site is about, and that the site is for those who cook with passion and expect nothing but quality.

The site is fully responsive, making it easy to use on phones as well as on PCs.

### Agile Development

The site is developed according to the Agile Methodology, where the GitHub Project feature was used to utilize the Kanban board for this purpose.

While developing, I chose one issue to work on from the "Todo" column of the Kanban board and moved it into the "In Progress" column.

After I was done with the issue by fulfilling all the acceptance criteria, I moved the issue into the "Done" Column.

#### MoSCoW Prioratization

I chose to follow the MoSCoW Prioritization method to label my issues(user stories/features):
  - Must Have
  - Should Have
  - Could Have
  - Won't Have

The Must Have having the highest priority, next being Should Have and then Could Have, Won't Have presenting the features not being implemented at this point and time.

[Back to Top](#table-of-contents)

### User Stories
| User Story | Priority |
|------------|------------------|
| As a ***customer***, I can ***view listed products***, so that ***I can find something to buy***. | **MUST HAVE** |
| As a ***customer***, I can ***view a detailed preview of the product***, so that ***I can get more information about it(price, description, image...)***. | **MUST HAVE** |
| As a ***customer***, I can ***search for the desired product by name or description***, so that ***I can find the specific product I want to buy***. | **MUST HAVE** |
| As a ***customer***, I can ***see the total cost of the items in my bag***, so that ***I can see if I am getting out of my budget***. | **MUST HAVE** |
| As a ***customer***, I can ***sort specific categories of products***, so that ***I can find the cheapest/best-rated product in the given category***. | **SHOULD HAVE** |
| As a ***customer***, I can ***sort the list of products***, so that ***I can easily find the best-priced/best-rated one***. | **SHOULD HAVE** |
| As a ***customer***, I can ***change the quantity of the added items within the shopping bag***, so that ***I can add/remove specific items if desired***. | **SHOULD HAVE** |
| As a ***customer***, I can ***easily view the items added to my shopping bag***, so that ***I can have an overview of the all items added and total cost***. | **MUST HAVE** |
| As a ***customer***, I can ***select the quantity of the products***, so that ***I can be sure to add the right quantity of the products to my shopping bag***. | **MUST HAVE** |
| As a ***customer***, I can ***enter my payment information***, so that ***I can checkout easily without any issues***. | **MUST HAVE** |
| As a ***customer***, I can ***have insight into the order confirmation details***, so that ***I can be sure I made no mistakes***. | **SHOULD HAVE** |
| As a ***customer***, I can ***get registered***, so that ***I can have a personal account/profile***. | **MUST HAVE** |
| As a ***customer***, I can ***view my profile***, so that ***I can view my order history and save/update shipping/paying information***. | **SHOULD HAVE** |
| As a ***customer***, I can ***receive the confirmation email***, so that ***I can be sure everything went well and keep it for just in case***. | **SHOULD HAVE** |
| As a ***customer***, I can ***receive email confirmation after filling in the register form***, so that ***I can verify my account registration was successful***. | **SHOULD HAVE** |
| As a ***customer***, I can ***add items to wishlist***, so that ***I don't need to search for them all over again when I decide to buy them***. | **SHOULD HAVE** |
| As a ***customer***, I can ***recover my password***, so that ***I can get access to my account in case I forget my password***. | **SHOULD HAVE** |
| As a ***customer***, I can ***rate the product I already bought***, so that ***I can leave positive/negative feedback***. | **SHOULD HAVE** |
| As a ***customer***, I can ***see if there are any special offers/deals***, so that ***I can enjoy the discounted price and save some money***. | **WON'T HAVE** |
| As a ***admin***, I can ***perform CRUD operations***, so that ***I can manipulate the site as desired***. | **MUST HAVE** |

[Back to Top](#table-of-contents)

### Wireframes

I have created wireframes within [Balsamiq](https://balsamiq.com/) to get initial idea of how the site will look like.

- #### Mobile and Tablet
  

    <details>
    <summary>Home Page
    </summary>

    ![Home Page](static/images/wireframes/home-page-mobile.png)
    </details>

    <details>
    <summary>Shop
    </summary>

    ![Shop](static/images/wireframes/shop-page-mobile.png)
    </details>

    <details>
    <summary>Product
    </summary>

    ![Product](static/images/wireframes/product-page-mobile.png)
    </details>

    <details>
    <summary>Shopping Bag
    </summary>

    ![Shopping Bag](static/images/wireframes/shopping-bag-mobile.png)
    </details>

    <details>
    <summary>Shopping Bag Empty
    </summary>

    ![Shopping Bag Empty](static/images/wireframes/shopping-bag-empty-mobile.png)
    </details>

    <details>
    <summary>Checkout
    </summary>

    ![Checkout](static/images/wireframes/checkout-mobile.png)
    </details>

    <details>
    <summary>Order Confirmed
    </summary>

    ![Order Confirmed](static/images/wireframes/order-confirm-mobile.png)
    </details>

    <details>
    <summary>Profile Details
    </summary>

    ![Profile Details](static/images/wireframes/profile-details-mobile.png)
    </details>

    <details>
    <summary>Sign Up
    </summary>

    ![Sign Up](static/images/wireframes/signup-mobile.png)
    </details>

    <details>
    <summary>Sign In
    </summary>

    ![Sign In](static/images/wireframes/signin-mobile.png)
    </details>

    <details>
    <summary>Sign Out
    </summary>

    ![Sign Out](static/images/wireframes/signout-mobile.png)
    </details>

    <details>
    <summary>Wishlist
    </summary>

    ![Wishlist](static/images/wireframes/wishlist-mobile.png)
    </details>

- #### Desktop

    <details>
    <summary>Home Page
    </summary>

    ![Home Page](static/images/wireframes/home-page-desktop.png)
    </details>

    <details>
    <summary>Shop
    </summary>

    ![Shop](static/images/wireframes/shop-page-desktop.png)
    </details>

    <details>
    <summary>Product
    </summary>

    ![Product](static/images/wireframes/product-page-desktop.png)
    </details>

    <details>
    <summary>Shopping Bag
    </summary>

    ![Shopping Bag](static/images/wireframes/shopping-bag-desktop.png)
    </details>

    <details>
    <summary>Shopping Bag Empty
    </summary>

    ![Shopping Bag Empty](static/images/wireframes/shopping-bag-empty-desktop.png)
    </details>

    <details>
    <summary>Checkout
    </summary>

    ![Checkout](static/images/wireframes/checkout-desktop.png)
    </details>

    <details>
    <summary>Order Confirmed
    </summary>

    ![Order Confirmed](static/images/wireframes/order-confirm-desktop.png)
    </details>

    <details>
    <summary>Profile Details
    </summary>

    ![Profile Details](static/images/wireframes/profile-details-desktop.png)
    </details>

    <details>
    <summary>Sign Up
    </summary>

    ![Sign Up](static/images/wireframes/signup-desktop.png)
    </details>

    <details>
    <summary>Sign In
    </summary>

    ![Sign In](static/images/wireframes/signin-desktop.png)
    </details>

    <details>
    <summary>Sign Out
    </summary>

    ![Sign Out](static/images/wireframes/signout-desktop.png)
    </details>

    <details>
    <summary>Wishlist
    </summary>

    ![Wishlist](static/images/wireframes/wishlist-desktop.png)
    </details>

[Back to Top](#table-of-contents)

### Site Goals

CookTopia is an e-commerce site offering a variety of kitchenware. It is currently focused on knives, pots, pans, and a few extra accessories. Customers are able to pay with cards thanks to the implemented Stripe payment system and get the products delivered to their door.

CookTopia is still in the growing phase with the intention of expanding the range of products offered, focusing on modern design, functionality, and above everything, high quality of products.

Simply said the goal is to become the final destination for those searching for high-quality kitchenware products.

[Back to Top](#table-of-contents)

### Design Choices

#### Color Scheme

The site uses a kind of minimalistic approach, using black and white throughout the the site, gray for some hover effects, and a fancy shade of red for some extra details such as within the logo itself, delivery banner, and some buttons.

![Design Colors](static/images/design-colors.png)

#### Font and Icons

The font used is [Lato](https://fonts.google.com/specimen/Lato?query=Lato), from Google Fonts, which is a versatile, open-source humanist sans-serif font family that has gained immense popularity for its warmth, legibility, and multilingual support across print and digital mediums.

Icons used are from the [Font Awesome](https://fontawesome.com/icons) free packet of icons.

#### Images

Images used for the products are taken artistically for a nice presentation, with an attempt to bring the practicality of the products closer to the customers.

[Back to Top](#table-of-contents)

## Database Design

### Database Model

The database model or so-called ERD(entity relationship diagram) was created to visualize the connection between models within the project. The diagram was created using Drawsql.app, here is the link to the diagram itself: [CookTopia-ERD](https://drawsql.app/teams/alexs-team-145/diagrams/cooktopia).

<details>
<summary>CookTopia - ERD
</summary>

![CookTopia - ERD](static/images/erd/cooktopia-erd.png)
</details>

### Custom Models

The custom models made for this project were:
 - Product(extended BoutiqueAdo's model)
 - ReviewRating
 - Wishlist

[Back to Top](#table-of-contents)

## Features

### Home Page

![Home Page](static/images/features/1-home-page.png)

- The landing page consists of Navbar, Main Section where we can find Shop Now button which takes us to the list of all products present at the site, Newsletter sign up option from MailChimp as well as Footer at the bottom of the page.

[Back to Top](#table-of-contents)

### Navbar
- Desktop

![Navbar-Desktop](static/images/features/2-navbar-desktop.png)

- Mobile-Collapsed

![Navbar-Mobile-Collapsed](static/images/features/3-navbar-mobile-collapsed.png)

- Mobile-Open

![Navbar-Mobile-Open](static/images/features/4-navbar-mobile-open.png)

- Navbar is fully responsive. Here we can find:
  - Logo, which acts as a Home button
  - Search Bar
  - My Account Icon
  - Wishlist Icon
  - Shopping Bag Icon, with total amount under it
  - Burger Icon on small and medium screens
  - Home button for smaller and medium screens

[Back to Top](#table-of-contents)

### Footer

- Desktop

![Footer-Desktop](static/images/features/5-footer-desktop.png)

- Mobile

![Footer-Mobile](static/images/features/6-footer-mobile.png)

- The Footer is pretty simple and self explanatory.
- The Footer is present at every page.
- The Links towards the social networks are being opened within the new tab as good UX practices.

[Back to Top](#table-of-contents)

### My Account

- Not Authenticated

![My Account Not Authenticated](static/images/features/7-my-account-logedout.png)

- Authenticated

![My Account Authenticated](static/images/features/8-my-account-logedin.png)

- My Account section is a drop-down with few different options for the authenticated and not authenticated user as well as Product Managment Tab for the admins.

[Back to Top](#table-of-contents)

### Product Management

![Product Management 1](static/images/features/9-product-management-1.png)
![Product Management 2](static/images/features/10-product-management-2.png)

- Product Management is a page available to the admins, which enables them to add the products to the e-store.

[Back to Top](#table-of-contents)

### My Profile

![My Profile](static/images/features/11-my-profile.png)

- This page consist of 2 sections:
  - Delivery Informations, which is there to store personal info about the users, address, number, country...
  - Order History, contains all of the previous orders, if there are any.

[Back to Top](#table-of-contents)

### Wishlist

- Empty

![Wishlist Empty](static/images/features/12-wishlist-empty.png)

- Not Empty

![Wishlist Not Empty](static/images/features/13-wishlist-populated.png)

- Wishlist is an feature coming handy for storing desired items for some future purchase. The products can be removed from the wishlist as well by clicking on the heart icon.

[Back to Top](#table-of-contents)

### Shopping Bag

- Empty

![Shopping Bag Empty](static/images/features/14-shopping-bag-empty.png)

- Not Empty

![Shopping Bag Empty](static/images/features/15-shopping-bag-populated.png)

- Shopping Bag is a page, where we can see details of the added items and cost of the planned purchase.
- We are also able to directly change the quantity of item/s to buy or completely remove them if needed.
- We can also continue shopping by clicking on the Keep Shopping button or proceed to Secure Checkout by pressing the aforementioned button.

[Back to Top](#table-of-contents)

### Secure Checkout

- Checkout consists of 2 sections:
  - Left Side, where we need to enter personal and delivery details, as well as payment details at the bottom
  - Right Side, where we have Order Summary once again to ensure everything is as desired.

![Secure Checkout](static/images/features/16-checkout.png)

- Payment Details, here we need to enter the card number, date of expiration and bic/swift code.

![Secure Checkout Buttons](static/images/features/177-checkout-buttons-2.png)

- Here is an example of the testing the payment process, provided by Stripe. For this testing to work the month must be the present one or any month in the future.

![Secure Checkout Buttons Test](static/images/features/17-checkout-buttons.png)

- Loading process/making payment, symbolically presented with a loading symbol, letting the customer know that the order is being processed.

![Secure Checkout Loading](static/images/features/18-checkout-loading.png)

[Back to Top](#table-of-contents)

### Thank You Page

- After the successfully placed order, the customer is taken to the Thank You Page, where once again he/she is being presented with the order summery.
- At the bottom is the Checkout Other Products button in case the customer wants to keep on searching through the site.
- The Customer is also being informed that the confirmation e-mail has been sent to the provided e-mail address.

![Thank You Page](static/images/features/19-thankyou-page.png)

[Back to Top](#table-of-contents)

### Search Bar
- No Search Criteria, in case someone clicks on search without typing in anything, the toast message will pop out.

![Search Bar](static/images/toasts/13-no-search-criteria.png)

- No Matching, the look of the search page in case there are no matches. With the small line of text saying:"0 Products found for..."

![Search Bar](static/images/features/20-search-no-products.png)

- Products Found, the look of the search page in case at least 1 product has been founded, in this case the line informs us that:"3 Products found for..."

![Search Bar](static/images/features/21-search-with-products.png)

[Back to Top](#table-of-contents)

### All Products Page

- By clicking on the All Products drop-down menu, we can choose to open the All Products page, sorting by one of the given criteria.
- Similarly we can open one of the other sections, be it a Knives, Pans, Pots or Accessories.

![All Products Drop-Down](static/images/features/22-allproducts-toggle-open.png)

- All Products Page, lists all of the present products at the site, with possibility of sorting the products by:
  - Price
  - Rating
  - Name
  - Brand
  - Category

![All Products Page](static/images/features/41-all-products-page.png)

- Under the picture of each product is a small section, where we can find:
  - Product Name
  - Brand
  - Price in €
  - Badge, representing the group of products
  - Rating
  - Edit/Delte Buttons (only for admins)
  - Add To Bag button
  - Quantity Button
  - Heart Icon, acting as add to wishlist button

![All Products Page Closed Up View](static/images/features/23-closeup-view-allproducts.png)

- Edit button takes the Admin to the Product Management page, in case some changes need to be done.
- Delete button, deletes the product from the e-store.

[Back to Top](#table-of-contents)

### Product Page

- This page contains all info about the product as well as Review/Comment section under the Product.
- The info about the Product from the All Products page is extended, and here we have added Description and Product Info.
- Under the Product Info, we have:
  - Material
  - Diametar
  - Volume
  - Country of Origin

![Product Page](static/images/features/24-detailed-view-product.png)

[Back to Top](#table-of-contents)

### Review Section

- This section can be found under the Product Info on the Product Page.
- In case the customer is authenticated and the given product is already in his order history, meaning he/she has already bought the product, the customer can leave a review.

![Review Section](static/images/features/25-review-section-detailed-product.png)

- Authenticated, but the product is not in the order history

![Review Section](static/images/features/26-no-reviews-yet.png)

- Authenticated, the product is in the order history

![Review Section](static/images/features/27-no-reviews-bought-already.png)

- Not Authenticated

![Review Section](static/images/features/42-review-logedout.png)

[Back to Top](#table-of-contents)

### Authentication

- Depending on the status of the site user, different options will be rendered.
- Not Authenticated users will see the option to Log In or Register
- Authenticated users will have the option to Logout
- The pages to Sign Up, Sign In, and Sign Out are pretty self-explanatory.

- Sign Up

![Sign Up](static/images/features/29-signup.png)

- Sign In

![Sign In](static/images/features/30-signin.png)

- Sign Out

![Sign Out](static/images/features/28-signout.png)

[Back to Top](#table-of-contents)

### Password Reset

- In case the customer forgets the password, there is a feature for password recovery.
- It can be accessed from the Sign In Page, by clicking the `Forgot Password?` link.

- Password Reset Form

![Password Reset Form](static/images/features/31-forgot-password.png)

- Password Reseted, the info customer gets after he clicks `Reset My Password` button. At this moment the e-mail to reset the password is being sent to the customer.

![Password Reseted](static/images/features/32-password-reseted.png)

- Password Change, the page customer is redirected to from the password reset e-mail.

![Password Change](static/images/features/33-password-change.png)

- Password Changed, the page the customer lands on after the customer types in new passwords 2 times and clicks on the `Change Password` button.

![Password Changed](static/images/features/34-password-changed.png)

[Back to Top](#table-of-contents)

### Additional Features

- Successful Registration 

![Successful Registration](static/images/features/37-successfully-registered.png)

- Registration E-Mail Confirmation, the page the user lands on after clicking on the confirmation link within the registration confirmation e-mail.

![Registration Confirmation](static/images/features/38-confirm-email.png)

- Product Badges, cards/links preseting groups of products, can be found at pages as Knives, Pots, Pans, and Accessories.

![Product Badges](static/images/features/39-product-badges.png)

[Back to Top](#table-of-contents)

### 404 Page

- The page that is rendered in case the user tries to open a non-existing page or simply appends `/404` to the address of the site.

![Password Changed](static/images/features/40-error-404-page.png)

[Back to Top](#table-of-contents)

### Future Features

- A blog could be added, as a way of presenting the products to future customers to help them decide if the given product is the right one for them.

- About Us Page, could be used to describe CookTopia as a reliable provider of high-quality kitchenware.

- Some kind of counter where the staff, as well as customers, can see the most sold items.

[Back to Top](#table-of-contents)

### Business Model

- The Site CookTopia is an e-commerce store, operating on the principles of Business to Customer model(B2C). For the sake of practicality, the site is designed so that both authenticated and non-authenticated users can make purchases.

[Back to Top](#table-of-contents)

#### Marketing Strategy

- Social Media Marketing (Facebook)
- The main task of this page on the social network Facebook is to inform others about our new products, as well as place targeted advertising.

![Facebook Marketing](static/images/marketing/facebook-page-1.png)
![Facebook Marketing](static/images/marketing/facebook-page-2.png)

- Newsletter Marketing (Mailchimp)
- At the Home Page is the Mailchimp newsletter form, where the customers can subscribe and get informed about the new arrivals.

![Mailchimp Marketing](static/images/features/35-mailchimp-successfull.png)

[Back to Top](#table-of-contents)