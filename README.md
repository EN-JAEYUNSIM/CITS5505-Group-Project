# CITS5505-Group-Project 

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

In terms of design, the application is crafted to be engaging, with a focus on usability and visual appeal. The layout is responsive, adapting to various screen sizes and devices to ensure accessibility for all users. By leveraging the power of HTML, CSS, and Bootstrap, the application presents information in a clear, organized fashion, enhanced by interactive elements implemented through JavaScript and jQuery.

Use of the application involves navigating through these views to post and respond to requests. User experience is enhanced with real-time updates through AJAX/Websockets, ensuring that the community is always up-to-date with the latest exchanges.

Overall, the Request Forum Application is an embodiment of a digital ecosystem that prioritizes user engagement and collective problem-solving, aiming to build a vibrant and supportive online community.

## Architecture 
```
CITS5505-Group-Project
├── app
│   ├── __init__.py
│   ├── blueprints.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   ├── content
│   │   ├── css
│   │   ├── images
│   │   └── js
│   └── templates
├── config.py
├── deliverables
│   ├── v1.0
│   ├── v2.0
│   └── v3.0
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── requirements.txt
├── README.md
├── tests
│   ├── selenium.py
│   └── unit.py
└── run.py
```

## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have installed the latest version of Python and Sqlite3.
* You have a Windows/Linux/Mac machine.

## Installation

Follow these steps to get your development env running:

1. Clone the repository:
  
   git clone https://github.com/EN-JAEYUNSIM/CITS5505-Group-Project.git
   
   ```
   cd CITS5505-Group-Project
   ```

2. Create a virtual environment:

   For Windows: 
   ```
   python -m venv venv
   ```

   For Unix or MacOS: 
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   
   For Windows: 
   ```
   .\venv\Scripts\activate
   ```

   For Unix or MacOS: 
   ```
   source venv/bin/activate
   ```

4. Instal the required packages:
   
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   
   ```
   flask run
   ```

## Team Members

| UWA ID   |          Name            |    GitHub Username    |
|----------|--------------------------|-----------------------|
| 24096172 | Dhanyavi Goti            | Dhanyavi08            |
| 24095031 | Janki Prafulbhai Rangani | jankirangani          |
| 24071255 | Xiaoyi Liu               | leah1leah1            |
| 24022721 | Lian Liu                 | EN-JAEYUNSIM          |
