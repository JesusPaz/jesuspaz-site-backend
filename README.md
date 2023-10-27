# JesusPaz Site Backend

Backend API and server logic for the personal website of Jesus Paz. Built with FastAPI, this repository handles data processing, authentication, and other server-side functionalities essential for the smooth running of the website.

## Prerequisites

- Python 3.8 or higher
- Pip (Python Package Installer)

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/<your-username>/jesuspaz-site-backend.git
   cd jesuspaz-site-backend
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Running the application

To run the server locally:

```bash
python3 -m uvicorn app.server:app --reload
```

The server will start, typically on `http://127.0.0.1:8000/`. You can access the FastAPI documentation on `http://127.0.0.1:8000/docs`.

## Testing

To run tests:

```bash
python3 -m pytest
```

## Contribution

1. Fork the repository.
2. Create a new branch for each feature or improvement.
3. Send a pull request from each feature branch.

It's very important to separate new features or improvements into separate feature branches, and to send a pull request for each branch. This allows me to review and pull in new features or improvements individually.
