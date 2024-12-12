# MUDDY PAWS

**Project Overview**

**Dog Grooming Business Management System**

This project is a web application designed specifically for a small dog grooming business. The primary goal of this system is to streamline the management of customer and pet information, thereby enhancing the efficiency of the business's booking process.

This web application serves as a vital tool for the dog grooming business owner, enabling her to slowly transition from paper-based bookings to a more organized digital system. By centralizing customer and pet information, the application not only saves time but also enhances customer service by allowing for more personalized interactions.

I have many future features planned for this project which I will outline further into the Readme.


![amiresponsive](/documentation/testing/AmIResponsive.png)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

**ERD**

I made my ERD with the midset of creating a booking system. While my initial goal was to create a full booking system, I pivoted to developing a customer management system for a dog grooming business. This experience taught me valuable lessons about adaptability, problem-solving, and time management. I gained hands-on experience with key concepts like user authentication, data handling, and UI/UX design.

Although I didn't achieve my original objective, I successfully created a functional system that supports customer management, and I now have a much clearer understanding of how to approach more complex booking functionality in the future. This experience has strengthened my technical skills and my ability to navigate challenges with resilience and creativity.

![ERD](/documentation/testing/ERD.png)

### User Stories

During the development process, it became clear that creating a complete booking system within the given timeframe was more challenging than initially anticipated. As a result, the project scope was adjusted to focus on core functionalities that could be successfully implemented and serve as a foundation for future development.

Shown below is my Project Board which shows the features i was not able to implement in the given timeline.

[Project Board](/documentation/testing/Project-board.png)

| **User Story ID** | **User Story Description**           | **MoSCoW Prioritization** |
|-------------------|--------------------------------------|--------------------------|
| #1                | View Home Page                      | Must Have                 |
| #2                | User Registration                   | Must Have                 |
| #3                | User Sign-In                        | Must Have                 |
| #4                | View Profile Dashboard              | Should Have               |
| #5                | Create a Booking                    | Could Have                |
| #6                | View Bookings                       | Could Have                |
| #7                | Update a Booking                    | Could Have                |
| #8                | Delete a Booking                    | Could Have                |
| #9                | Leave a Review                      | Could Have                |
| #10               | View Reviews                        | Could Have                |
| #11               | Add Pet Profile                     | Must Have                 |
| #12               | Edit Pet Profile                    | Must Have                 |
| #13               | Delete Pet Profile                  | Must Have                 |

**Agile**

The development of the customer management system was guided by Agile methodology, which emphasized adaptability, iterative progress, and continuous feedback. I broke the project into smaller, manageable user stories, each with clear objectives and acceptance criteria. This approach allowed me to prioritize essential features and make steady progress toward the overall goal.

By working in iterative sprints, I was able to regularly review and refine the system based on what was working well and what needed improvement. Daily reflections and retrospectives helped me identify blockers early and adjust my approach accordingly. While the initial goal of creating a full booking system shifted, the Agile process ensured that I still delivered a valuable, functional product. This experience taught me how to remain flexible, prioritize effectively, and maintain momentum even when project goals evolve.

## Design

### Colour Scheme

I chose this colour palette as the colours match the asthetic in the grooming parlour. 

![Colour Palette](/documentation/testing/Muddy%20Paws%20Palette.png)


### Typography

The font I used was:
![Just Another Hand Font](/documentation/testing/Font.png)

I chose this font because it wasnt too robotic, as the business is a small local business, the owner wanted it to feel warm and welcoming.

### Imagery

The imagery I used throughout the site was provided by the business owner. 

### Wireframes

I made my wireframes using Figma. As the scope of the project changed there are some differences from the wireframes to the finished product however they are still very similar to the expected outcome.

![Home](/documentation/wireframes/Home-wireframe.png)

![Dashboard](/documentation/wireframes/Dashboard-wireframe.png)




## Features

My site is made up of the Home page, Sign in page, Sign up page, Sign out page, Dashboard, Bookings, Add Pet, Edit Pet and Delete Pet pages.

### General features on each page

General features that reoccur on each page are the navbar, footer, favicon and background.
Each page inlcudes the base.HTML which includes all these features.

![Navbar](/documentation/testing/Navbar.png)

![Footer](/documentation/testing/Footer.png)

### Future Implementations

I have many future enhancements lined up. As my initial plan was to create the booking system that will be the next feature I will implement. Along with the hopes of implementing an automated reminder for customers with bookings too.

After this feature I would love to add a reviews section in order to allow customers to give feedback to the business and to show new customers the feedback that has been left.

I would be interested in implementing a social account login too.

### Accessibility

In my project I have added aria-labels and names to all my links and buttons to enable screen readers to understand each element. I have run a lighthouse test and a wave test to ensure I have met the requirements needed to be accessible friendly.

## Technologies Used

### Languages Used

- HTML
- CSS
- JavaScript
- Python
- [Git](https://git-scm.com/) used for version control.
- [Github](https://www.github.com) used for online storage of codebase and Projects tool.
- [GitPod](https://codeinstitute-ide.net/workspaces) as the IDE Code Institute recommeneds we use.
- [Figma](https://www.figma.com) for project design planning and wireframe creation.
- [Coolors](https://coolors.co/) for colour theme creation and accessibility checkers.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
- [Cloudinary](https://cloudinary.com/) was used for cloud media storage of user uploaded images.
- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) create and host the database.
- [Heroku](https://www.heroku.com) was used to host the Muddy Paws application.
- [WAVE](https://wave.webaim.org/) to evaluate the accessibility of the site.
- [Canva](https://canva.com/) for image creation and editing.
- [Adobe Stock](https://stock.adobe.com/uk/) for getting the placeholder image and favicon.
- [Convertio](https://convertio.co/) used for mage conversion.
- [Favicon](https://favicon.io/) used to convert the image to favicon.
- [Lucid Chart](https://www.lucidchart.com/) used to create ERD.


## Deployment


### Deployment

The site was deployed to Heroku. The steps to deploy are as follows:
 - Install the gunicorn python package and create a file called 'Procfile' in the repo's root directory
 - In the Procfile write 'web: gunicorn lunar_lists.wsgi'
 - In settings.py add ".herokuapp.com" to the ALLOWED_HOSTS list
 - In settings.py add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS list, git add, commit and push to github

Navigate to the Heroku dashboard
 - Create a new Heroku app
 - Give it a name and select the region 'Europe'
Navigate to settings tab and scroll down to Config Vars
 - Click 'Reveal Config Vars'
 - Add the following keys:
         key = DATABASE_URL | value = (my secret database url)
         key = SECRET_KEY | value = (my secret key)
Navigate to Deploy tab
 - Connect to GitHub and select the repo 'lunar-lists'
 - Scroll down to 'Manual deploy' and select the 'main' branch
 - Click 'Deploy Branch'

## Testing

All testing is documented [Here](/TESTING.md)


## Credits

### Code Used

- [perplexity](https://www.perplexity.ai/)
- [ChatGPT](https://chatgpt.com/)
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Daisy Walkthrough](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1)

  
###  Acknowledgments

- First of all I would like to thank my amazing Learning Facilitator [Amy Richardson](https://github.com/amylour) for her consistant guidance and support. Without her I would not be where I am with this project, she is a credit to Code Institute. 

- I would also like to thak my coding coaches John Rearden and [Mark Briscoe](https://github.com/mbriscoe) for all their guidance when I was struggling with my booking system. They helped to guide me in the right direction.

- I would like to thank my Cohort for always having each others backs and always lending a hand or an ear when needed. Especially to [Laura]() and [Martin] for their never ending support and willingness to all get each other to continue on the right path to the finish line.

- Finally I would like to thank my family for helping emotionally during this project. I wouldn't be here at the end of this course if it wasn't for my amazingly supportive partner.