#  Snapz

[View project here](https://snapzapp.herokuapp.com/)

---

Snapz is a modern photosaring app thats a cross between Reddit style piosting and Instagram UI. The propject is currenctly in MVP state and allows the user to post, comment, like, and view other users pages

![Am I responsive image](https://i.imgur.com/dTeHmTE.png)

Responsiveness was checked using [Am I responsive](http://ami.responsivedesign.is/)

## Deployment
Project is deployed using Heroku for both the server and database

To ensure the correct packages are installed you need to use the `pip3 freeze --local > requirments.txt` to build out the requirments.txt

When applying the product to heroku you need to log in and;

**App**
- Create a new app
- Add enviroment variables
- Link the heroku app to Github repo
- Build project from repo

**Database**
- In youyr project click on *configure ad ons*
- Select Heroku Postgress
- Copy the login the add on details to use later 

## Features
---

- **Account page:** Rather then needing to log into the django admin a page was created to allow other users to view all posts for themselves or other users.
- **Liking posts:** This features allows users to like each others posts to show interest in the photos which were uplaoded
- **Commenting:** This featuire allows users to comment and have a discussion on each others posts
- **Posting new images:** USers are able to post images through a form while logged into their account, this redices the reisk of users who are noght siged up from uploading images to the site

## Testing 
---
- The site has been tested on the desktop versions of Chrome, Safari, and firefox.
- The site tested using the dev tools device tool to make sure the breakpoints function on all sizes
- The site was tested on mobile devices of different screen sizes to check for breakpoints and responsiveness
- The site was tested by several expernal users 

### Validation Testing
PEP8 formatting was followed for the project, some of the code that Django generated was too long to be in line with PEP 8 Formatting

## Bugs:
#### Solved bugs:
- Creating a form to allow users to post without having to view the admin page and have the correct formatting apply

#### Unsolved bugs:
- Project wll not run without being in debig mode
- PEP8 Formatting on Django generated code
  - ![PEP* Errors](https://i.imgur.com/uQVN3JR.png)
## Content
---
#### Credits
- A similar layout in the coding structure was as [I think therefore I blog app](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) which was shown in the course.

#### Media

- Logo and favi con were made for the project
- The lion image was sourced through Google
- The other images were taken by myself

## Technologies used
- HTML 5
- CSS 3
- JavaScript
- Font Awsome
- Django
- Heroku
- Cloudinary