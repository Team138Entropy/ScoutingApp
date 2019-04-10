# Scouting App

This is our scouting app. 

## Web stack

### Frontend
We use HTML, CSS, and Javascript / jQuery. The site is a form that POSTS directly to RestDB's API.s

### Backend
We have < 60 lines of backend, written in Node.js and using Express for the routing.

### Heroku
Both the frontend and backend are hosted on Heroku on [the project called `scout138`](https://dashboard.heroku.com/apps/scout138). The email for the heroku login is team138entropy@gmail.com.

### Database
We use [RestDB](https://restdb.io) and sign in with the team138entropy@gmail.com Google account. Once you've logged in, go to the [strategy](https://strategy-e354.restdb.io/) database. Click the gears in the upper-right to modify the website.

## To edit code
### Getting started
1. Clone the repo.
2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. Run this magical account: `heroku git:remote -a scout138`

### Trying your code
Run this command: `heroku local`

### Deploying your code
Run this command: `git push heroku master` and then this: `git push`