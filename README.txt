# Pitch

## Built By [Samuel Muriuki](https://github.com/Samuel-Muriuki/)

## Description

The Pitch is a web application that displays a list of various news sources. On choosing a pitch category, it will preview that category and give you the option to create another pitch.

You can view the site at:[Heroku](https://pitcher-1.herokuapp.com/)

## User Stories

These are the behaviours/features that the application implements for use by a user.

* As a user I would like to:
* As a user, I would like to see the pitches other people have posted.
* As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
* As a user, I would like to be signed in for me to leave a comment
* As a user, I would like to receive a welcoming email once I sign up.
* As a user, I would like to view the pitches I have created in my profile page.
* As a user, I would like to comment on the different pitches and leave feedback.
* As a user, I would like to submit a pitch in any category.
* As a user, I would like to view the different categories.

## Specifications

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display pitch categories | **On page load** | List of various pitch categories |
| Display tabs with pitch category | **On Tab link click** | Clickable links to open pitches based on category |


## SetUp / Installation Requirements

### Prerequisites

* Python 3.9.10
* pip
* virtualenv

### Cloning

* In your terminal:

        $ git clone https://github.com/Samuel-Muriuki/Pitch/
        $ cd Pitch

## Running the Application

* Creating the virtual environment

        $ python3.9 -m venv --without-pip env
        $ source env/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.9 -m pip install flask
        $ python3.9 -m pip install flask_Bootstrap
        $ python3.9 -m pip install flask_script


* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application

* To run the tests for the class files:

        $ python3.9 manage.py tests

## Technologies Used

* Python 3.9.10
* Flask 2.0.3
* Werkzeug 2.0.3

## License

MIT License

Copyright (c) [2022] [Samuel-Muriuki]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Go Back to the top](#Pitch)

## Author Bio

Slack Profile - [Samuel-Muriuki](https://app.slack.com/)

[Go Back to the top](#Pitch)
