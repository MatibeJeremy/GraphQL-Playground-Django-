[![Build Status](https://travis-ci.org/MatibeJeremy/Javascript-starterPack.svg?branch=master)](https://travis-ci.org/MatibeJeremy/Javascript-starterPack) [![Coverage Status](https://coveralls.io/repos/github/MatibeJeremy/Javascript-starterPack/badge.svg?branch=master)](https://coveralls.io/github/MatibeJeremy/Javascript-starterPack?branch=master)

# GraphQL Playground
A GraphQL API for users to query and mutate posts in a Postgres database

# Installation 
 Create Environment

   `python3.8 -m venv venv`

   `source venv/bin/activate`

 Install pip dependencies
    
    `pip install`

 Run migrations

    `python manage.py migrate`

 Run server

    `python manage.py runserver`


# Examples

Posts Query:

`query{
  posts{
    id
    title
    by{
      id
      username
      email
    }
  }
}
}`

Response:

`{
  "data": {
    "posts": [
      {
        "id": "5",
        "title": "To infinity an beyond",
        "by": {
          "id": "2",
          "username": "Ivar",
          "email": "ivar@email.com"
        }
      }
    ]
  }
}`

