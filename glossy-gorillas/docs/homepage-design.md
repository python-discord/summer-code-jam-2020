# Home Page

## User Stories
### 1. As a person...
1. I want to view the basic functionality of the site without creating an account
2. I want to register/log-in easily
### 2. As a regular user...
1. I want to see an overview of activity on my listings/offers
2. I want a breakdown of what's happening site wide
3. I want links to navigate the site quickly
### 3. As a trading company
1. I want to see an overview of my ships and cumulative goods
2. I want to see reports of piracy on my trading routes
### 4. As a port owner
1. I want to see an overview of the activity in my port
### 5. As TeaBay
1. We want to sell ads to businesses
   - “A pub near port A should be able to advertise to users currently making use of trading in port A”
   - “Brothel A should be able to advertise services to a trading company”
   - “Port A has open docking slots, they should be able to advertise to trading companies”
2. We want to provide a paid news feed of relevant information to all users

## Solutions
### Navbar
- Homepage has a navbar at the top, with quick links to login/signup and other site pages (1.2, 2.3)

### Widget-based design
- Homepage is broken down into multiple widgets
- Each widget shows a view of something happening on the site (1.1, 2.2)
- Widgets are initialised based on whether the user is logged-in, and the type of user e.g.: (2.1, 3.1, 3.2, 4.1)
  - non logged-in users will see recent trade listings and completed trades
  - logged-in traders will see recent listings and offers on their listings
- Logged-in users can customise the widgets by moving them and selecting different ones to their liking
- Certain widgets can be used for a fee (5.2)

### Advertisements
- ads are placed around the page (5.1)
- targeted ads get shown only to their relevant users (5.1)