<div id="top"></div>


<br />
<div align="center">

<h3 align="center">Web Store App</h3>

  <p align="center">
    This is a web store application, which functions as a music store demo
    <br />
    <a href="https://github.com/ikolokotronis/Web-Store-App"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="">View Demo</a>
    ·
    <a href="https://github.com/ikolokotronis/Web-Store-App/issues">Report Bug</a>
    ·
    <a href="https://github.com/ikolokotronis/Web-Store-App/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project


This is my Coders Lab bootcamp graduation project.  
Originally it was written to be a music store but it could be anything you want, based on what you add to the database. (except for the logo and the ads, which you can delete or make your own of course).

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Pytest](https://docs.pytest.org/)
* [Six](https://six.readthedocs.io/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [Django mathfilters](https://pypi.org/project/django-mathfilters/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  pip install django
  ```
  ```sh
  pip install psycopg2-binary
  ```
  ```sh
  pip install six
  ```
  ```sh
  pip install django-mathfilters
  ```
  ```sh
  pip install pillow
  ```

### Installation

1. Make sure you have python installed in your sytem
2. Clone the repo
   ```sh
   git clone https://github.com/ikolokotronis/Web-Store-App
   ```
3. Install PIP packages(shown above)
4. Enter your database settings in settings.py. Here is an example if you want to use PostgreSQL:
   ```python
   DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'NAME': 'db_name_here',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'user_name_here',
        'PASSWORD': 'password_here',
    }
    }
   ```
5. In your terminal, switch to the main directory (cd web_store_app/) and run python manage.py runserver
6. In settings.py change the email data to yours if you want to work with the django send_email function. *

"*" means optional

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You could use this project as a jumpstart, prototype or an inspiration for your web store application. 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Add some JavaScript to make the app more dynamic
- [] Improve the Front-end


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Ioannis Kolokotronis - ioanniskolokotronis1@gmail.com

Project Link: [https://github.com/ikolokotronis/Web-Store-App](https://github.com/ikolokotronis/Web-Store-App)

<p align="right">(<a href="#top">back to top</a>)</p>
