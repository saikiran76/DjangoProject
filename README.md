# Django URL Shortener

A stylish and efficient URL shortener web application built using the Django framework. This app allows users to easily shorten their long URLs into compact and shareable links. It provides a seamless redirection to the original URLs and tracks analytics for each shortened link. 

## Features

- URL shortening: Easily generate unique and short URLs for long links.
- Redirects: Users are seamlessly redirected to the original URL when visiting the shortened link.
- Analytics: Track the number of visits and gain insights into link popularity.
- User Authentication: Securely manage and track your own shortened URLs with personalized features.
- Admin Dashboard: Authorize admins to access detailed information about long and short URLs, number of clicks, and dates.

## Tech Stack

- Django: A powerful and popular Python web framework.
- HTML/CSS: Styling and structuring the user interface.
- SQLite: A lightweight and efficient database for storing URL data using Django's ORM (Object-Relational Mapping).
## Installation

1. Clone the repository.
2. Run migrations using `python manage.py migrate`.
3. Start the development server with `python manage.py runserver`.

## Usage

1. Access the web app via the provided URL.
2. Enter a long URL in the input field.
3. Click the "Shorten" button to generate a shortened URL.


## License

This project is licensed under the [MIT License](LICENSE).

