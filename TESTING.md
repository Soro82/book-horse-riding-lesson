## Testing

Click [here](README.md) to return to the readme file.

## Table of Contents

### [Code Validation](#code-validation-1)
### [Lighthouse Testing](#lighthouse-testing-1)
### [Manual Testing](#manual-testing-1)
### [Bugs](#bugs-1)
### [Responsiveness](#responsiveness-1)

### Code Validation

#### HTML Validation

<details>
<summary>Home Page</summary>

![Home Page HTML Validation](documentation/testing/html/home_page.png)

</details>

<details>
<summary>Horses Page</summary>

![Horses Page HTML Validation](documentation/testing/html/horses_page.png)

</details>

<details>
<summary>Horses Page Logged In</summary>

![Horses Page Logged In HTML Validation](documentation/testing/html/horses_page_logged_in.png)

</details>

<details>
<summary>Login Page</summary>

![Login Page HTML Validation](documentation/testing/html/login_page.png)

</details>

<details>
<summary>Make Booking Page</summary>

![Make Booking Page HTML Validation](documentation/testing/html/make_booking.png)

</details>

<details>
<summary>My Booking Page</summary>

![My Booking Page HTML Validation](documentation/testing/html/my_bookings.png)

</details>

<details>
<summary>Edit Booking Page</summary>

![Edit Booking Page HTML Validation](documentation/testing/html/edit_booking.png)

</details>

<details>
<summary>Delete Booking Page</summary>

![Delete Booking Page HTML Validation](documentation/testing/html/delete_booking.png)

</details>

<details>
<summary>404 Error Page</summary>

![404 Error Page HTML Validation](documentation/testing/html/404_page.png)

</details>

<details>
<summary>500 Error Page</summary>

![500 Error Page HTML Validation](documentation/testing/html/500_page.png)

</details>

#### Python Validation

* book_lesson app

<details>
<summary>admin.py</summary>

![admin.py Python Validation](documentation/testing/python/admin_validation.png)

</details>

<details>
<summary>forms.py</summary>

![forms.py Python Validation](documentation/testing/python/forms_validation.png)

</details>

<details>
<summary>models.py</summary>

![models.py Python Validation](documentation/testing/python/models_validation.png)

</details>

<details>
<summary>urls.py</summary>

![urls.py Python Validation](documentation/testing/python/urls_validation.png)

</details>

<details>
<summary>views.py</summary>

![views.py Python Validation](documentation/testing/python/views_validation.png)

</details>

* horse_riding_lessons

<details>
<summary>settings.py</summary>

![settings.py Python Validation](documentation/testing/python/settings_validation.png)

</details>

<details>
<summary>urls.py</summary>

![urls.py Python Validation](documentation/testing/python/project_urls_validation.png)

</details>

#### CSS Validation

<details>
<summary>style.css</summary>

![style.css CSS Validation](documentation/testing/other/css_validation.png)

</details>

#### JavaScript Validation

<details>
<summary>script.js</summary>

![script.js JavaScript Validation](documentation/testing/other/javascript_validation.png)

</details>

#### WAVE Validation

<details>
<summary>WAVE Validation</summary>

![WAVE Validation](documentation/testing/other/wave_validation.png)

</details>

### Lighthouse Testing

<details>
<summary>Home Page</summary>

![Home Page Lighthouse Testing](documentation/testing/lighthouse/home_page.png)

</details>

<details>
<summary>Horses Page</summary>

![Horses Page Lighthouse Testing](documentation/testing/lighthouse/horses_page.png)

</details>

<details>
<summary>Sign Up Page</summary>

![Sign Up Page Lighthouse Testing](documentation/testing/lighthouse/sign_up.png)

</details>

<details>
<summary>Login Page</summary>

![Login Page Lighthouse Testing](documentation/testing/lighthouse/sign_in.png)

</details>

<details>
<summary>Make Booking Page</summary>

![Make Booking Page Lighthouse Testing](documentation/testing/lighthouse/make_booking.png)

</details>

<details>
<summary>My Booking Page</summary>

![My Booking Page Lighthouse Testing](documentation/testing/lighthouse/my_bookings.png)

</details>

<details>
<summary>Edit Booking Page</summary>

![Edit Booking Page Lighthouse Testing](documentation/testing/lighthouse/edit_booking.png)

</details>

<details>
<summary>Sign Out Page</summary>

![Sign Out Page Lighthouse Testing](documentation/testing/lighthouse/sign_out.png)

</details>


[Back to Top](#testing)

### Manual Testing

| Location | Test | Expected Result | Result |
| :------: | :--: | :-------------: | :----: |
| Navbar | Click on Login | Opens the login page | Pass |
|  | Click on Sign Up | Opens the signup page | Pass |
|  | Click on Horses | Opens the horses page | Pass |
|  | Click on Logout | Opens the logout page | Pass |
|  | Click on Heading in navbar | Opens the home page | Pass |
|  | User Logged In | Sign Up and Login links change to User's name | Pass |
|  | User Logged Out | User's name link change to Sign Up and Login | Pass |
| Popular Horses | Click on Login | Opens the login page | Pass |
|  | Click on Book Now | Opens the booking page | Pass |
|  | User Logged In | Book Now button displayed | Pass |
|  | User Logged Out | Login button displayed | Pass |
| Horses Page | Click on Login | Opens the login page | Pass |
|  | Click on Next | Display next 3 horses | Pass |
|  | Click on Previous | Display previous 3 horses | Pass |
|  | Click on Book Now | Opens the booking page | Pass |
|  | User Logged In | Book Now button displayed | Pass |
|  | User Logged Out | Login button displayed | Pass |
| Login Page | Enter invalid username | Error message displayed | Pass |
|  | Enter invalid password | Error message displayed | Pass |
|  | Click on Sign Up | Opens the signup page | Pass |
|  | No password entered | Please fill in this field | Pass |
|  | No username entered | Please fill in this field | Pass |
|  | Enter valid username and password | Successfully logged in message | Pass |
| Booking Page |  | Horse name displayed above Lesson Date field | Pass |
|  | No date entered | Please fill in this field | Pass |
|  | Date earlier than today | Correct Error message displayed | Pass |
|  | Date earlier than today | Message fades away after 3 seconds | Pass |
|  | Date and time already booked | Correct Error message displayed | Pass |
|  | Date and time already booked | Message fades away after 3 seconds | Pass |
|  | Two users book same lesson date and time | Booking Confirmed | Pass |
|  | Horse already booked | Correct Error message displayed | Pass |
|  | Horse already booked | Message fades away after 3 seconds | Pass |
|  | Lesson fully booked | Correct Error message displayed | Pass |
|  | Lesson fully booked | Message fades away after 3 seconds | Pass |
|  | Click on Submit | Confirmation Message displayed | Pass |
|  | Click on Submit | Message fades away after 3 seconds | Pass |
|  | Click on Submit | Form fields cleared | Pass |
| My Bookings Page | Click on Edit | Opens the edit booking page | Pass |
|  | Click on Delete | Opens the delete booking page | Pass |
| Edit Booking Page |  | Horse name displayed above Lesson Date field | Pass |
|  | No date entered | Please fill in this field | Pass |
|  | Date earlier than today | Correct Error message displayed | Pass |
|  | Date earlier than today | Message fades away after 3 seconds | Pass |
|  | Date and time already booked | Correct Error message displayed | Pass |
|  | Date and time already booked | Message fades away after 3 seconds | Pass |
|  | Horse already booked | Correct Error message displayed | Pass |
|  | Horse already booked | Message fades away after 3 seconds | Pass |
|  | Lesson fully booked | Correct Error message displayed | Pass |
|  | Lesson fully booked | Message fades away after 3 seconds | Pass |
|  | Click on Update Booking | Confirmation Message displayed | Pass |
|  | Click on Update Booking | Message fades away after 3 seconds | Pass |
|  | Click on Update Booking | Return to bookings page | Pass |
| Delete Booking Page | Click on Confirm Delete | Booking deleted | Pass |
|  | Click on Confirm Delete | Confirmation Message displayed | Pass |
|  | Click on Confirm Delete | Message fades away after 3 seconds | Pass |
|  | Click on Confirm Delete | Return to bookings page | Pass |
| 404 Error Page | Enter incorrect URL | 404 Error Page opens | Pass |
|  | Click on Take Me Home | Returns to Home Page | Pass |
| 500 Error Page | Admin raises an exception | 500 Error Page opens | Pass |
|  | Click on Take Me Home | Returns to Home Page | Pass |

[Back to Top](#testing)

### Bugs

#### Fixed Bugs
| Bug | Solution | Result |
| :-: | :------: | :----: |
| User able to double book a horse | Validate if booking exits | Pass |
| User able to double book a time | Validate if booking time exits | Pass |
| Multiple bookings for same time and date | Validate if booking is full | Pass |
| User able to book previous date to today | Validate booking date | Pass |
| Booking time displayed as integer | booking.get_lesson_time_display | Pass |
| Two users unable to book the same time | Check user against request.user | Pass |
| Navbar dropdown causing page scrollbar | Add "me-lg-4" class | Pass |
| My Bookings in order of date but not time | Order by date and time | Pass |
| Insecure Requests error in console | cloudinary.config(secure = True) | Pass |
| Unable to change location in edit booking | add validation check on location | Pass |
| Unable to change experience in edit booking | add validation check on experience | Pass |

#### Unfixed Bugs
* There are no unfixed bugs.

[Back to Top](#testing)

### Responsiveness

#### Home Page

![Home Page](documentation/screenshots/desktop/home_logged_out.png)

![Home Page Tablet](documentation/screenshots/tablet/home_page.png) ![Home Page Mobile](documentation/screenshots/mobile/home_logged_in.png)
#### Navbar

![Navbar](documentation/screenshots/desktop/navbar_logged_out.png)

![Navbar Tablet](documentation/screenshots/tablet/navbar.png) ![Navbar Mobile](documentation/screenshots/mobile/navbar.png)

#### Popular Horses

![Popular Horses](documentation/screenshots/desktop/popular_horses_logged_in.png)

![Popular Horses Tablet](documentation/screenshots/tablet/popular_horses.png) ![Popular Horses Mobile](documentation/screenshots/mobile/popular_horses_logged_in.png)

#### Horses Page

![Horses Page](documentation/screenshots/desktop/horses_logged_out.png)

![Horses Page Tablet](documentation/screenshots/tablet/horses_page.png) ![Horses Page Mobile](documentation/screenshots/mobile/horses_page.png)

#### Make Booking Page

![Make Booking Page Desktop](documentation/screenshots/desktop/make_booking.png)

![Make Booking Page Tablet](documentation/screenshots/tablet/make_booking.png) ![Make Booking Page Mobile](documentation/screenshots/mobile/make_booking.png)

#### My Bookings Page

![My Bookings Page](documentation/screenshots/desktop/my_bookings.png)

![My Bookings Page Tablet](documentation/screenshots/tablet/my_bookings.png) ![My Bookings Page Mobile](documentation/screenshots/mobile/my_bookings.png)

#### Delete Booking Page

![Delete Booking Page](documentation/screenshots/desktop/delete_confirmation.png)

![Delete Booking Page Tablet](documentation/screenshots/tablet/delete_booking.png) ![Delete Booking Page Mobile](documentation/screenshots/mobile/delete_booking.png)

#### Login Page

![Login Page Desktop](documentation/screenshots/desktop/login.png)

![Login Page Tablet](documentation/screenshots/tablet/sign_in.png) ![Login Page Mobile](documentation/screenshots/mobile/login.png)

#### Footer

![Footer](documentation/screenshots/desktop/footer.png)

![Footer Mobile](documentation/screenshots/mobile/footer.png)

[Back to Top](#testing)