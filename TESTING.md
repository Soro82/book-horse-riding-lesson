## Testing

Click [here](README.md) to return to the readme file.

### Features Testing

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

### Validator Testing
