## Testing

### Features Testing

| Location | Test | Expected Result | Result |
| :------: | :--: | :-------------: | :----: |
| Navbar | Click on Login | Opens the login page | Passed |
|  | Click on Sign Up | Opens the signup page | Passed |
|  | Click on Horses | Opens the horses page | Passed |
|  | Click on Logout | Opens the logout page | Passed |
|  | Click on Heading in navbar | Opens the home page | Passed |
|  | Login | Sign Up and Login links change to User's name | Passed |
|  | Logout | User's name link change to Sign Up and Login | Passed |
| Popular Horses | Click on Login | Opens the login page | Passed |
|  | Click on Book Now | Opens the booking page | Passed |
| Horses Page | Click on Login | Opens the login page | Passed |
|  | Click on Next | Display next 3 horses | Passed |
|  | Click on Previous | Display previous 3 horses | Passed |
|  | Click on Book Now | Opens the booking page | Passed |
| Login Page | enter invalid username | Error message displayed | Passed |
|  | Enter invalid password | Error message displayed | Passed |
|  | Click on Sign Up | Opens the signup page | Passed |
|  | No password entered | Please fill in this field | Passed |
|  | No username entered | Please fill in this field | Passed |
|  | Enter valid username and password | Successfully logged in message | Passed |
| Booking Page | No date entered | Please fill in this field | Passed |
|  | Horse not choosen | Please fill in this field | Passed |
|  | Date earlier than today | Error message displayed | Passed |
|  | Date and time already booked | Error message displayed | Passed |
|  | Horse already booked | Error message displayed | Passed |
|  | Lesson fully booked | Error message displayed | Passed |
|  | Click on Submit | Confirmation Message displayed | Passed |
|  | Click on Submit | Confirmation Message disappears after 3 seconds | Passed |
|  | Click on Submit | Form fields cleared | Passed |
| My Bookings Page | Click on Edit | Opens the edit booking page | Passed |
|  | Click on Delete | Opens the delete booking page | Passed |
| Edit Booking Page | No date entered | Please fill in this field | Passed |
|  | Horse not choosen | Please fill in this field | Passed |
|  | Date earlier than today | Error message displayed | Passed |
|  | Date and time already booked | Error message displayed | Passed |
|  | Horse already booked | Error message displayed | Passed |
|  | Lesson fully booked | Error message displayed | Passed |
|  | Click on Update Booking | Confirmation Message displayed | Passed |
|  | Click on Update Booking | Return to bookings page | Passed |
| Delete Booking Page | Click on Confirm Delete | Booking deleted | Passed |
|  | Click on Confirm Delete | Confirmation Message displayed | Passed |
|  | Click on Confirm Delete | Return to bookings page | Passed |
| 404 Error Page | Enter incorrect URL | 404 Error Page opens | Passed |
|  | Click on Take Me Home | Returns to Home Page | Passed |
| 500 Error Page | Admin raises an exception | 500 Error Page opens | Passed |
|  | Click on Take Me Home | Returns to Home Page | Passed |


### Fixed Bugs
* The validation to check if a booking time exists for a user was preventing other users from making a booking at the same time. I added a check to see if the time was booked for the user making the request.

### Unfixed Bugs