<div id="top"></div>
<br />
<div align="center">
  <a href="https://github.com/wilfredohq/fastapi-money-transfer">
    <img
      src="https://github.com/WilfredoHQ/md-readme/raw/main/images/logo.png"
      alt="Logo"
      width="80"
      height="80"
    />
  </a>
  <h3 align="center">FastAPI Money Transfer</h3>
  <p align="center">
    Backend for money transfer application with FastAPI and PostgreSQL.
    <br />
    <a href="https://github.com/wilfredohq/fastapi-money-transfer">
      <strong>Explore the docs »</strong>
    </a>
    <br />
    <br />
    <a href="https://m-transfer.herokuapp.com/docs">
      View Demo
    </a>
    ·
    <a href="https://github.com/wilfredohq/fastapi-money-transfer/issues">
      Report Bug
    </a>
    ·
    <a href="https://github.com/wilfredohq/fastapi-money-transfer/issues">
      Request Feature
    </a>
  </p>
</div>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About The Project

A sample of the backend application to transfer money to different branches.

<p align="right">(<a href="#top"> ↑ back to top </a>)</p>

### Built With

-   [Python 3.9.7](https://www.python.org/downloads/release/python-397/)
-   [Poetry](https://python-poetry.org/)
-   [FastAPI](https://fastapi.tiangolo.com/)
-   [PostgreSQL](https://www.postgresql.org/)

<p align="right">(<a href="#top"> ↑ back to top </a>)</p>

## Getting Started

To get a working local copy, follow these simple steps.

### Prerequisites

Things you need to use the software and how to install them.

-   Python 3.9.7
-   PostgreSQL

### Installation

1. Create a new database.
2. Clone the repo.

    ```sh
    git clone https://github.com/wilfredohq/fastapi-money-transfer.git
    ```

3. Make a copy of `.env.example` with the name `.env` and set your environment variables.
4. Install Poetry if you don't already have it.

    ```sh
    pip install poetry
    ```

5. Install Poetry packages.

    ```sh
    poetry install
    ```

6. You can then start a shell session in the new environment.

    ```sh
    poetry shell
    ```

7. Run alembic from migrations.

    ```sh
    alembic upgrade head
    ```

    ** Note: ** If you modify the tables, you must first run the following to generate a new revision.

    ```sh
    alembic revision --autogenerate -m "Structure change message"
    ```

8. Run the uvicorn server.

    ```sh
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

9. Now you can open your browser and interact with these URLs.
    - Backend, JSON based web API based on OpenAPI: http://localhost/api/
    - Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost/docs
    - Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://localhost/redoc

<p align="right">(<a href="#top"> ↑ back to top </a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit your Changes (`git commit -m 'feat: add some amazing-feature'`)
4. Push to the Branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

<p align="right">(<a href="#top"> ↑ back to top </a>)</p>

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<p align="right">(<a href="#top"> ↑ back to top </a>)</p>
