## Full-Stack-Web-Development-Instapix-Project
### Overview:
#### About the application:</br>
Instapix is a photo sharing application, which allows users to share photos, follow other users and view the posts of their followers. Every user who creates an Instapix account has a profile and a newsfeed.
Instapix application has got the following features - account creation and logging in to it, viewing the newsfeed, and most importantly uploading pictures (creating posts), follow the users who are not in the user’s account.

#### High level Design:</br>
a. On load of the application, the program displays the home page with sign up and sign in sections.
b. When clicked on Sign Up button by providing mandatory information, user gets registered with a unique account details. For registered users, click on the Login button, redirects to login page.
c. After login, user redirected to the newsfeed page (timeline) where user can view photos/posts posted by other users.
d. When the upload icon (+) is clicked, program should redirect to the photo upload form

#### Features:</br>
1. Sign Up and Sign In</br>
Every new user shall register in the application through the signup process. The sign-up page shall have mobile number, email address, full name and password as mandatory fields. The phone number, email and username shall be unique to every user and duplicates shall not be accepted. The sign in page for already registered users will have username and password fields. When a user tries to sign into the application, these details are authenticated against the database. At the time of user’s registration (sign up), Provided details are saved into the database and retrieve from it, when User logs into the application. Based on the feasibility, password complexity requirements shall also be enforced.</br>
2. View Timeline/Newsfeed</br>
News feed is a series of photos uploaded by the user in the application. Every user in the application shall be able to see all the photos uploaded by other users.</br>
3. Create Posts</br>
Every user will have an option to create posts by uploading pictures. The uploaded pictures are visible to self as well as other users of the application.</br>
4. Profile</br>
Displays the user’s information and the pictures posted by the user.</br>
5. Sign out</br>
Whenever the user wishes to logout, by clicking on the logout button, he will be redirected out of the application to logout page.</br>

Stack:</br>
Frontend – HTML, CSS, Bootstrap, JavaScript</br>
Backend - Python Flask, Jinja template</br> 
Database - SQLite3</br>

Technical Details:</br>
Frontend designed using HTML, CSS and JavaScript:</br>
Sign Up/Sign In – Designed signup and signin form using html, and styled the elements using css, used attribute selectors for styling forms, used float on image elements, used bootstrap for styling buttons.</br>

Navigation bar – used keyframes to slide navigation links. Used flex display for navigation bar and positioned navigation bar elements with space in between using space-between justify content. In navigation bar, positioned newsfeed logo following Instapix title on left side, centered signed in user’s profile picture and user name, positioned navigation links for creating posts, explore, profile, and logout.</br> 

Newsfeed – used flex layout for the display of newsfeed page, aligned items in the center, and used flex column direction, used block display for displaying user picture and user name of that particular post.</br>

Createpost – used flex layout to control the alignment of elements. Displayed user picture along with text area to provide some text about post. Displayed camera icon using font awesome for uploading multiple pictures.</br>

Explore - used flex layout for the display of users along with checkbox in column direction followed by follow button.</br>

Profile – Used flex layout and styled profile container by displaying username and full name next to image by applying space in between the elements.</br>

Signout – Passes a html form in signout icon to display logout page and applied styles accordingly.</br>

Issues Faced:
Faced alignment issues in most of the screens, In particular, when working on explore screen, css changes didn’t reflect and elements got misaligned after adding jinja backend code.  
