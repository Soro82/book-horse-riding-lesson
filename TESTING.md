## Testing

Click [here](README.md) to return to the readme file.

## Table of Contents

### [Code Validation](#code-validation)
### [Lighthouse Testing](#lighthouse-testing)
### [Manual Testing](#manual-testing)
### [Bugs](#bugs)

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
| Navbar | Click on Login | Opens the login page | Passed |
|  | Click on Sign Up | Opens the signup page | Passed |
|  | Click on Horses | Opens the horses page | Passed |
|  | Click on Logout | Opens the logout page | Passed |
|  | Click on Heading in navbar | Opens the home page | Passed |
|  | User Logged In | Sign Up and Login links change to User's name | Passed |
|  | User Logged Out | User's name link change to Sign Up and Login | Passed |
| Popular Horses | Click on Login | Opens the login page | Passed |
|  | Click on Book Now | Opens the booking page | Passed |
|  | User Logged In | Book Now button displayed | Passed |
|  | User Logged Out | Login button displayed | Passed |
| Horses Page | Click on Login | Opens the login page | Passed |
|  | Click on Next | Display next 3 horses | Passed |
|  | Click on Previous | Display previous 3 horses | Passed |
|  | Click on Book Now | Opens the booking page | Passed |
|  | User Logged In | Book Now button displayed | Passed |
|  | User Logged Out | Login button displayed | Passed |
| Login Page | Enter invalid username | Error message displayed | Passed |
|  | Enter invalid password | Error message displayed | Passed |
|  | Click on Sign Up | Opens the signup page | Passed |
|  | No password entered | Please fill in this field | Passed |
|  | No username entered | Please fill in this field | Passed |
|  | Enter valid username and password | Successfully logged in message | Passed |
| Booking Page |  | Horse name displayed above Lesson Date field | Passed |
|  | No date entered | Please fill in this field | Passed |
|  | Date earlier than today | Correct Error message displayed | Passed |
|  | Date earlier than today | Message fades away after 3 seconds | Passed |
|  | Date and time already booked | Correct Error message displayed | Passed |
|  | Date and time already booked | Message fades away after 3 seconds | Passed |
|  | Two users book same lesson date and time | Booking Confirmed | Passed |
|  | Horse already booked | Correct Error message displayed | Passed |
|  | Horse already booked | Message fades away after 3 seconds | Passed |
|  | Lesson fully booked | Correct Error message displayed | Passed |
|  | Lesson fully booked | Message fades away after 3 seconds | Passed |
|  | Click on Submit | Confirmation Message displayed | Passed |
|  | Click on Submit | Message fades away after 3 seconds | Passed |
|  | Click on Submit | Form fields cleared | Passed |
| My Bookings Page | Click on Edit | Opens the edit booking page | Passed |
|  | Click on Delete | Opens the delete booking page | Passed |
| Edit Booking Page |  | Horse name displayed above Lesson Date field | Passed |
|  | No date entered | Please fill in this field | Passed |
|  | Date earlier than today | Correct Error message displayed | Passed |
|  | Date earlier than today | Message fades away after 3 seconds | Passed |
|  | Date and time already booked | Correct Error message displayed | Passed |
|  | Date and time already booked | Message fades away after 3 seconds | Passed |
|  | Horse already booked | Correct Error message displayed | Passed |
|  | Horse already booked | Message fades away after 3 seconds | Passed |
|  | Lesson fully booked | Correct Error message displayed | Passed |
|  | Lesson fully booked | Message fades away after 3 seconds | Passed |
|  | Click on Update Booking | Confirmation Message displayed | Passed |
|  | Click on Update Booking | Message fades away after 3 seconds | Passed |
|  | Click on Update Booking | Return to bookings page | Passed |
| Delete Booking Page | Click on Confirm Delete | Booking deleted | Passed |
|  | Click on Confirm Delete | Confirmation Message displayed | Passed |
|  | Click on Confirm Delete | Message fades away after 3 seconds | Passed |
|  | Click on Confirm Delete | Return to bookings page | Passed |
| 404 Error Page | Enter incorrect URL | 404 Error Page opens | Passed |
|  | Click on Take Me Home | Returns to Home Page | Passed |
| 500 Error Page | Admin raises an exception | 500 Error Page opens | Passed |
|  | Click on Take Me Home | Returns to Home Page | Passed |

[Back to Top](#testing)

### Bugs

#### Fixed Bugs
| Bug | Solution | Result |
| :-: | :------: | :----: |
| User able to double book a horse | Validate if booking exits | Passed |
| User able to double book a time | Validate if booking time exits | Passed |
| Multiple bookings for same time and date | Validate if booking is full | Passed |
| User able to book previous date to today | Validate booking date | Passed |
| Booking time displayed as integer | booking.get_lesson_time_display | Passed |
| Two users unable to book the same time | Check user against request.user | Passed |
| Navbar dropdown causing page scrollbar | Add "me-lg-4" class | Passed |
| Insecure Requests error in console | cloudinary.config(secure = True) | Passed |
| My Bookings in order of date but not time | Order by date and time | Passed |


#### Unfixed Bugs
* There are no unfixed bugs.
