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
- [Marketing Strategy](#marketing-strategy)
    - [Social Media Marketing](#social-media-marketing)
    - [Newsletter Marketing](#newsletter-marketing)
- [Search Engine Optimization](#search-engine-optimization)
    - [Keywords](#keywords)
    - [Meta Tags](#meta-tags)
    - [Sitemap.xml](#sitemapxml)
    - [Robots.txt](#robotstxt)

- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [Tools](#tools)

- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Validations](#validations)
    - [Browser Testing](#browser-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Present Bugs](#present-bugs)

- [Deployment](#deployment)
    - [PostgreSQL from Code Institute](#postgresql-from-code-institute)
    - [Heroku Deployment](#heroku-deployment)
        - [Preparation](#preparation)
        - [Deployment](#deployment-1)
    - [Amazon - AWS Hosting](#amazon---aws-hosting)
        - [S3 Bucket](#s3-bucket)
        - [IAM](#iam)
        - [Final Setup](#final-setup)
    - [Stripe](#stripe)
    - [Google Mail API](#google-mail-api)

- [Development](#development)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Download ZIP](#download-as-zip)

- [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

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
  - My Account, with Icon for bigger screens
  - Wishlist, with Icon for bigger screens
  - Shopping Bag Icon, with the total amount under it
  - Burger Icon on small and medium screens
  - Home button for small and medium screens

[Back to Top](#table-of-contents)

### Footer

- Desktop

![Footer-Desktop](static/images/features/5-footer-desktop.png)

- Mobile

![Footer-Mobile](static/images/features/6-footer-mobile.png)

- The Footer is pretty simple and self explanatory.
- The Footer is present at every page.
- The Links towards the social networks are being opened within the new tab as good UX practices.
- Privacy Policy also opens an independent page where the Policy is.

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

- The sales page could be used to introduce the discount possibilities.

- Add wishlist button to the All Products Page to improve UX.

[Back to Top](#table-of-contents)

### Business Model

- The Site CookTopia is an e-commerce store, operating on the principles of Business to Customer model(B2C). For the sake of practicality, the site is designed so that both authenticated and non-authenticated users can make purchases.

[Back to Top](#table-of-contents)

### Marketing Strategy

#### Social Media Marketing
- The main task of this page on the social network Facebook is to inform others about our new products, as well as place targeted advertising.

  <details>
  <summary>Facebook Marketing First
  </summary>

  ![Facebook Marketing First](static/images/marketing/facebook-page-1.png)
  </details>

  <details>
  <summary>Facebook Marketing Second
  </summary>

  ![Facebook Marketing Second](static/images/marketing/facebook-page-2.png)
  </details>


#### Newsletter Marketing
- At the Home Page is the Mailchimp newsletter form, where the customers can subscribe and get informed about the new arrivals.

  <details>
  <summary>Mailchimp Marketing
  </summary>

  ![Mailchimp Marketing](static/images/features/35-mailchimp-successfull.png)
  </details>

[Back to Top](#table-of-contents)

### Search Engine Optimization

#### Keywords

- I tested several long-tail keywords using the websites [Wordtracker](https://www.wordtracker.com/), [Moz](https://moz.com/). Most keywords showed low volume and competition.

  <details>
  <summary>Keyword - Moz
  </summary>

  ![Keyword Moz](static/images/marketing/moz-key-research.png)
  </details>

  <details>
  <summary>Keyword - Wordtracker First
  </summary>

  ![Keyword Wordtracker First](static/images/marketing/wordtracker-1.png)
  </details>

  <details>
  <summary>Keyword - Wordtracker Second
  </summary>

  ![Keyword Wordtracker Second](static/images/marketing/wordtracker-2.png)
  </details>


#### Meta Tags

- In the head of base.html, under the Meta Tags section `<meta name="description"` ... and `<meta name="keywords"` ... tags were included.

#### Sitemap.xml

- I created a sitemap.xml file using [XML-Sitemaps](https://www.xml-sitemaps.com/), for the SEO improvements.

#### Robots.txt

- I created a robots.txt file within my root directory.

  <details>
  <summary>Robots.txt
  </summary>

  ![Robots.txt](static/images/marketing/robots-txt.png)
  </details>

- The file instructs search engines which directories not to crawl and index. It also links to the sitemap. The existence of this file signals a level of quality to search engines and so improves SEO ranking as a result.

[Back to Top](#table-of-contents)

## Technologies Used

### Languages

- HTML
- CSS
- Python
- Javascript

[Back to Top](#table-of-contents)

### Frameworks and Libraries

- [Django v3.2](https://docs.djangoproject.com/en/4.2/releases/3.2/) developement framework
- [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) for template rendering
- [AllAuth v0.41](https://django-allauth.readthedocs.io/) for authentication
- [django-crispy-forms v1.14.0](https://pypi.org/project/crispy-bootstrap4/) for form rendering
- [boto3 v1.34.86](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for AWS CRUD with Python scripts
- [dj-database-url v0.5.0](https://pypi.org/project/dj-database-url/) for DATABASE_URL
- [django-countries v7.2.1](https://pypi.org/project/django-countries/) for country field rendering in checkout form
- [django-storages v1.14.2](https://django-storages.readthedocs.io/en/latest/) for handling static and media files
- [gunicorn v22.0.0](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/gunicorn/) apure-Python WSGI server for UNIX
- [oauthlib v3.2.2](https://pypi.org/project/oauthlib/) OAuth request-signing logic
- [psycopg2 v2.9.9](https://pypi.org/project/psycopg2/) s PostgreSQL database adapter for Python
- [Stripe v9.1.0](https://stripe.com/en-ie) for payment system

[Back to Top](#table-of-contents)

### Tools

- [Balsamiq](https://balsamiq.com/) used to create wireframes
- [Drawsql.app](https://drawsql.app/) used to create ERD
- [GitPod](https://gitpod.io/) used as IDE
- [Git](https://git-scm.com/) used for version control
- [GitHub](https://github.com/) used for online storage of codebase and projects tool
- [Heroku](https://heroku.com/) used for site hosting
- [AWS - Amazon Web Services (S3)](https://aws.amazon.com/) used to host static and media files
- [Image Resizer](https://www.simpleimageresizer.com/) used for handling the images(resizing, cropping, formating...)
- [Favicon](https://favicon.io/) used to create favicon
- [Amiresponsive](https://ui.dev/amiresponsive) used to create a mockup image of the CookTopia site
- [Perplexity AI](https://www.perplexity.ai/) used for debugging and problem solving
- [Slack](https://slack.com/) used for connecting as well as debugging and problem-solving during development
- [Mailchimp](https://mailchimp.com/) used for newsletter subscription service
- [Gmail](https://mail.google.com/) used for real e-mail sending
- [XML Sitemaps](https://www.xml-sitemaps.com/) used to generate sitemap.xml file
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/) used to create policy

[Back to Top](#table-of-contents)

## Testing

### Manual Testing

- For complete manual testings head to: [TESTING.md](TESTING.md)

### Validations

### Browser Testing

- Complete functionality and layout of the site was tested across next browsers:

  | Browser     | Layout      | Functionality |
  | :---------: | :----------:| :-----------: |
  | Brave       | ✔          | ✔             |
  | Edge        | ✔          | ✔             |
  |  Opera GX   | ✔          | ✔             |
  |    Safari   | ✔          | ✔             |

[Back to Top](#table-of-contents)

### Fixed Bugs

 - #### Bug 1 - Shopping Bag Quantity Button
   - Before fixing, users were able to press the "-" button even after 1(going to 0, -1, -2, and so on). The "+" button was disabled when the number hit 99, but users could enter numbers bigger than 99 by keyboard, so this needed fixing too, as the idea was to set 99 as the biggest possible amount to choose.

 - #### Fix 1
   <details>
   <summary>Quantity Button Fix
   </summary>

   ![Quantity Button Fix](static/images/bugs/qty-button-fix.png)
   </details>

- #### Bug 2 - Server Error (500)
  - In the case of non-authenticated user, when the user wanted to open a product_detail page, a 500 Server Error was prompted.
    <details>
    <summary>Server Error (500)
    </summary>

    ![Server Error 500](static/images/bugs/500-server-error.png)
    </details>

- #### Fix 2
   <details>
   <summary>Server Error (500) Fix
   </summary>

   ![500 Server Error Fix](static/images/bugs/500-server-error-fix.png)
   </details>

- #### Bug 3 - Footer
  - In the case of a page with no or little content, the footer was jumping up.
    <details>
    <summary>Footer Bug
    </summary>

    ![Footer Bug](static/images/bugs/footer-bug.png)
    </details>

- #### Fix 3
  - This issue was fixed by setting:
    - min-height: 100vh;(body)
    - flex-grow: 1;(allowing main container on the page to take all extra space)
    - margin-top: auto;(footer)

    <details>
    <summary>Footer Fix
    </summary>

    ![Footer Fix](static/images/bugs/footer-fix.png)
    </details>

[Back to Top](#table-of-contents)

### Present Bugs
 - There are no known bugs.

[Back to Top](#table-of-contents)

## Deployment

A live version of the site is deployed to [Heroku](https://www.heroku.com/) and can be found here: [CookTopia](https://cooktopia-3a5b4620860d.herokuapp.com/).

### PostgreSQL from Code Institute

- Since the recent change at ElephantSQL, I've decided to go with the database CI provided for us.
- To make the database for the project, the steps are next:
- First go to [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/), enter your e-mail address and click submit.

  <details>
    <summary>Step 1
    </summary>

    ![Step 1](static/images/ci-postgresql/step-1.png)
  </details>

- Your database will get generated automatically and you will receive an e-mail with the info about your database.

  <details>
    <summary>Step 2
    </summary>

    ![Step 2](static/images/ci-postgresql/step-2.png)
  </details>

- Within the e-mail, you will have a link to your database dashboard. Here you can see all of the needed information about your database or delete them if you'd like to.

  <details>
    <summary>Step 3
    </summary>

    ![Step 3](static/images/ci-postgresql/step-3.png)
  </details>

- After you click the `Info` button, a list with all the needed information will pop up.

  <details>
    <summary>Step 4
    </summary>

    ![Step 4](static/images/ci-postgresql/step-4.png)
  </details>

[Back to Top](#table-of-contents)

### Heroku Deployment

#### Preparation

- Before the deployment, the following steps were taken to prepare the application for the deployment on Heroku:

- The setting `DEBUG` in the settings.py has to be set to `FALSE`. 
- It was achieved by the next lines:
- Within `settings.py`:
    ````
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
          import env
    ````
    ````
      DEBUG = 'DEVELOPMENT' in os.environ
    ````
- Within `env.py`:
    ````
      os.environ["DEVELOPMENT"] = 'False'
    ````
- Allow Heroku as host: In `settings.py` add `ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']`
- All the dependencies were stored in the requirements.txt file with the command `pip3 freeze --local > requirements.txt`.
- The start command for the application `web: gunicorn cooktopia.wsgi:application` was stored in a Procfile.

[Back to Top](#table-of-contents)


#### Deployment

1. Go to [Heroku](https://id.heroku.com/login), create account if you don't have and log in.

2. Head to your dashboard and click `New`, then `Create new app`

    <details>
    <summary>New/CreateNewApp
    </summary>
              
    ![New/CreateNewApp](static/images/heroku/step1-create-new-app.png)
    </details>

3. Next step is to give your app a name and to choose region. After that click on `Create app`.

    <details>
    <summary>Name/Region/Create
    </summary>
              
    ![Name/Region/Create](static/images/heroku/step2-create-app.png)
    </details>

4. After that head to `Settings` tab which you can find on top of your Heroku page and under the `Config Vars` set your Key/Value Pairs.

    <details>
    <summary>Config Vars
    </summary>
              
    ![Config Vars](static/images/heroku/step3-config-vars.png)
    </details>

5. Then in the `Buildpacks` section you will need to add buildpacks. In this case `Heroku/Python` was already set, so I didn't need to change anything.

    <details>
    <summary>Buildpacks
    </summary>
              
    ![Buildpacks](static/images/heroku/step8-buildpacks.png)
    </details>

6. Then head to the `Deployment` tab which you can also find on top of your Heroku page and under `Deployment method` click on `GitHub`(in my case that's where my repository is).

    <details>
    <summary>GitHub
    </summary>
              
    ![GitHub](static/images/heroku/step4-deployment-method.png)
    </details>

7. After that, just under the `Deployment method` section is `Connect to GitHub` section where you need to find your repository and then click on `Connect`.

    <details>
    <summary>Connect
    </summary>
              
    ![Connect](static/images/heroku/step5-connect-to-github-repo.png)
    </details>

8. Just under `Connect to GitHub` section is `Automatic deploys` section where you can click on `Enable Automatic Deploys` if that's what you want and just under is `Manual Deploy` section, where you need to click on `Deploy Manually`.

    <details>
    <summary>Enable Automatic Deploys
    </summary>
              
    ![EnableAutomaticDeploys](static/images/heroku/step6-automatic-deployments.png)
    </details>

    <details>
    <summary>Deploy Manually
    </summary>
              
    ![EnableAutomaticDeploys](static/images/heroku/step7-deploy.png)
    </details>

[Back to Top](#table-of-contents)

### Amazon - AWS Hosting

- This project uses [AWS](https://aws.amazon.com) to store media and static files online, because Heroku doesn't persist this type of data.

- Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
- Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click `Save`.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click `Add Statement`
	- Click `Generate Policy`
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Version": "2012-10-17",
      "Id": "Policy111111111111",
      "Statement": [
				{
					"Sid": "Stmt11111111111",
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::bucket-name/*"
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click `Save`.
- From the **Access Control List (ACL)** section, click `Edit` and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled**.

[Back to Top](#table-of-contents)

#### IAM

From the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click `Create New Group`.
	- Suggested Name: **manage-cooktopia** (manage + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click `Attach Policies`.
- Select the policy, then click `Add Permissions` at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::bucket-name",
						"arn:aws:s3:::bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click `Review Policy`.
	- Suggested Name: `cooktopia-policy` (site name-policy)
	- Click **Create Policy**.
- From **User Groups**, click your `manage-cooktopia`.
- Click `Attach Policy`.
- Search for the policy you've just created ("cooktopia-policy") and select it, then **Attach Policy**.
- From **User Groups**, click `Add User`.
	- Suggested Name: `cooktopia-staticfiles-user ` (site name + staticfiles-user)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `manage-cooktopia`
- Tags are optional, but you must click it to get to the **review user** page.
- Click `Create User` once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

[Back to Top](#table-of-contents)

#### Final Setup

- The `DISABLE_COLLECTSTATIC` within Heroku Config Vars can be removed now, as AWS will handle the static files from now on.
- Within you **S3** Bucket, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click `Upload`.

[Back to Top](#table-of-contents)

### Stripe

- Stripe's API is used to handle payments. To setup Stripe follow next steps:

  - Create if you don't have and Log In to a Stripe account.
  - In the Stripe Dashboard -> **Get your test API keys.**
  - Add your `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` to your env.py, connect to your settings.py using your environment variables and then enter them into your project's Heroku Config Vars.
  - Including Stripe's Webhooks creates a failsafe if a customer exits the page during payment authorisation. In Stripe's Dashboard -> **Developers** -> **Webhooks** -> **Add Endpoint**: 'herokuapp url/checkout/wh'
  -  Choose **Retrieve all events** -> **Add Endpoint**.
  -  Add new key **STRIPE_WH_SECRET** to env.py, settings.py and Heroku Config Vars as before.

[Back to Top](#table-of-contents)

### Google Mail API

- Setup a Gmail Account that will be used to hold and store the emails for your project.
- Log In and navigate to **Settings** -> **See All Settings** -> **Accounts and Import** -> **Other Google Account settings**
- Activate 2-Step Verification
- Once verified access **App Passwords** -> enter a name for the password.(e.g. Django-Project Name)
- Click `Create` -> copy the 16 digit password that is generated.
- In your `settings.py` add the following Email Settings:
````
# Sending Emails
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'cooktopia@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
````  
- Add `EMAIL_HOST_PASS`, `EMAIL_HOST_USER` to your Heroku Config Vars.

[Back to Top](#table-of-contents)

## Development

### Fork

- A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

- To fork a project, follow next steps:

  - Log into GitHub and click on repository to download: [CookTopia](https://github.com/AleksandarJavorovic/cooktopia)
  - Click the `Fork` button in the top right-hand corner
  - Select a different owner, if desired
  - Click `Create Fork`
  - The repo is now in your chosen account

[Back to Top](#table-of-contents)

### Clone

- Changes made to a cloned repository will affect the original one if the branch to push to isn't changed.

- To clone, follow the steps under:

  - Navigate to the main page of the repostitory (this could be a forked instance)
  - Click on the `Code` dropdown menu above the list of files
  - Choose a method to copy the URL for the repository: either via `HTTPS`, by using an `SSH key`, or by using `GitHub CLI`
  - In your work environment, open Git Bash and change current directory to target location for cloned repository
  - Type ``git clone`` followed by the copied URL and press enter `Enter`

[Back to Top](#table-of-contents)

### Download as ZIP

- Log In to GitHub and click on repository to download: [CookTopia](https://github.com/AleksandarJavorovic/cooktopia)
- Click on the `Code` dropdown menu and click `Download Zip` file
- Once downloaded, extract ZIP file and use in your local IDE

[Back to Top](#table-of-contents)

## Credits

### Code

- The main guide for this project was the CI walkthrough project [BoutiqueAdo](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218).
- [Sportswear](https://github.com/CodeWizard-1/e-commerce?tab=readme-ov-file) was used as inspiration for `README.md` file.
- [Chirpy Chooks](https://github.com/Kay-ddggxh/chirpy_chooks?tab=readme-ov-file#source-credits) was used as inspiration for `README.md` file.
- [Everneed](https://github.com/amylour/everneed/blob/main/README.md#google-mail-setup) was used as inspiration for `README.md` file, as well as inspiration for the wishlist feature.
- [Perplexity.ai](https://www.perplexity.ai/) was used for debugging during development process.
- [Review and Rating System](https://www.youtube.com/watch?v=3KCBN7WJXMY&list=PLFNQLcwO1GaY3dy2i6F5vQ60YGDRUD-bX), this video was used for inspiration to create review section within the project.
- Many code bugs were solved thanks to CI Slack channels.
- [Simple website footer example](https://codepen.io/alvarotrigo/pen/ZExxeRz), used as inspiration for the footer.
- [Average for Ratings in Django](https://stackoverflow.com/questions/60602349/average-for-ratings-in-django), helped with calculating average ratings of a product

[Back to Top](#table-of-contents)

### Media

- Images used for this project are from [Unsplash](https://unsplash.com/).
- [XXXLutz](https://www.xxxlutz.de/) was used as inspiration while planning

[Back to Top](#table-of-contents)

### Media

- Images used for this project are from [Unsplash](https://unsplash.com/).
- [XXXLutz](https://www.xxxlutz.de/) was used as inspiration while planing the look of the site.

[Back to Top](#table-of-contents)

### Acknowledgements

- I want to say to my wife:"Thank you for all your love and support. <3"
- I want to thank my mentor Mitko Bachvarov for tips and suggestions.
- I want to thank our facilitator Kristyna, as well as our cohort members for advices and moral support during the course.
- I want to thank to tutors at CI Tutor Support for all their help.
- I want to thank to CI Student Support for their understaing and help.

[Back to Top](#table-of-contents)