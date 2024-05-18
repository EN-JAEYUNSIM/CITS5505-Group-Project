# CITS5505-Group-Project 

a description of the purpose of the application, explaining the its design and use.
a table with with each row containing the i) UWA ID ii) name and iii) Github user name of the group members.
a brief summary of the architecture of the application.
instructions for how to launch the application.
instructions for how to run the tests for the application.

## DIY Request Forum Application

#### Purpose of the Application
The Request Forum Application is a community-driven platform designed to connect individuals seeking assistance, advice, or the exchange of goods and services with those who are willing to provide help. Envisioned as a versatile request-and-response ecosystem, the application enables users to create accounts, post requests, respond to others, and engage in a self-sustained cycle of support and collaboration.

The platform's flexibility allows for a wide array of request types, ranging from problem-solving puzzles, collaborative gaming experiences, to marketplace transactions for digital goods. At its core, the application serves as a hub for community engagement, fostering a space where users can contribute to others' needs while fulfilling their own.

#### Design and Use
The application is structured into several intuitive and user-friendly views:

- Introductory View: A landing page that introduces new visitors to the application's objectives, provides insights into its community value, and guides through the process of account creation or login.
- Requests Dashboard: A dynamic view where users can browse active requests, filter by categories or tags, and interact with posts by offering solutions or further queries.
- Create Request View: A straightforward interface for users to articulate new requests, define the scope, and attach any necessary information or media.
- User Profile and Management: Personalized user dashboards where members can track their activity, manage their requests, and interact with other community members.
- 
In terms of design, the application is crafted to be engaging, with a focus on usability and visual appeal. The layout is responsive, adapting to various screen sizes and devices to ensure accessibility for all users. By leveraging the power of HTML, CSS, and Bootstrap, the application presents information in a clear, organized fashion, enhanced by interactive elements implemented through JavaScript and jQuery.

Use of the application involves navigating through these views to post and respond to requests. User experience is enhanced with real-time updates through AJAX/Websockets, ensuring that the community is always up-to-date with the latest exchanges.

Overall, the Request Forum Application is an embodiment of a digital ecosystem that prioritizes user engagement and collective problem-solving, aiming to build a vibrant and supportive online community.

## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have installed the latest version of Python and sqlite3.
* You have a Windows/Linux/Mac machine.

## Installation

Follow these steps to get your development env running:

1. Clone the repository:
  
   git clone https://github.com/EN-JAEYUNSIM/CITS5505-Group-Project.git
   cd CITS5505-Group-Project

2. Create a virtual environment:
   python -m venv venv    # For Windows
   virtualenv venv        # For Unix or MacOS

3. Activate the virtual environment:
   .\venv\Scripts\activate    # For Windows
   source venv/bin/activate   # For Unix or MacOS

4. Instal the required packages:
   pip install -r requirements.txt

3. Run the application:
   flask run


#### Color pallete:
please refer to hex codes from the website: https://www.color-hex.com/
the color pallete includes:
1. main color, 2. complementry color, 3. action color, 4.background color(which is not white), 5.additional color 
The color palletes:
1. https://colors.muz.li/palette/5e2b7e/ff6f61/2ec4b6/e0e0e0/ffd166
2. https://colors.muz.li/palette/FF6B6B/6b5bff/ffc66b/f0f0f0/5bffa3
3. https://colors.muz.li/palette/7F00FF/00ffd5/ff4d00/f8f8f8/ffd700
4. https://colors.muz.li/palette/2D3142/6a0572/ff9f1c/e0e0e0/00a8cc



#### Division of work:

janki: Intro page
Xiaoyi: Dashboard, request page
Dhanyavi: Create request page, answer request page, Login page, Signup page
Lian: User profile page



#### flie structure:
please refer to this file structure:

folders:
1. public:
  - index.html(main file which will just have reference of other pages)
2. src:
  - files:
    * the js and html files that we're making
  - CSS:
    * all the css files
  - img:
    * the images that we're using
  - Auth:
    * authentication file(backend part)
  - index.js
3. Readme.md
4. .gitignore and any other files
5. deliverables



## Team Members

| UWA ID   |          Name            |    GitHub Username    |
|----------|--------------------------|-----------------------|
| 24096172 | Dhanyavi Goti            | Dhanyavi08            |
| 24095031 | Janki Prafulbhai Rangani | jankirangani          |
| 24071255 | Xiaoyi Liu               | leah1leah1            |
| 24022721 | Lian Liu                 | EN-JAEYUNSIM          |


#### extra content:

for font family please visit: https://www.w3schools.com/howto/tryit.asp?font=Brygada%201918

you are welcome to change this, i have just added it initially in intro page.


##### can anyone find a name of the website and put it instead of AGILE WEB PROJECT