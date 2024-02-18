# Sample REST API

This is a REST API built using Python and Django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed:
- Python 3.11
- pipenv

To install pipenv, run following command in your terminal:
```bash
pip install pipenv
```


### Installation and Setup 

A step by step series of examples that tell you how to get a development environment running.

1. Clone the repository
```bash
git clone https://github.com/elitecoderX/sampleRestAPI.git
```
2. Navigate to the project directory
```bash
cd sampleRestAPI
```
3. Install the dependencies using pipenv
```bash
pipenv install
```
Congratulations, Now this API is ready to run on your local machine!

### Database Migrations

After setting up the project, you'll need to create the database tables and apply migrations. Here's how you can do it:
```bash
python manage.py makemigrations
```

### Run the API on your local machine
```bash
python manage.py runserver
```
## Author
Sachin - Initial work - [elitecoderX](https://github.com/elitecoderx)