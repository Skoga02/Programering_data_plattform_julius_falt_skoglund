# FROM      - Image (Snapshot)
# WORKDIR   - Working Directory ("/app") - a new folder within docker, called app
# COPY      - Extract a duplicate copy of our app (app snapshot)
# EXPOSE    - Includes a port that OS listens to
# CMD       - Commands to be run, on startup

FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy only dependency files first (better layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies from lock file
RUN uv sync --frozen

# Copy rest of the project
COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t demo-9 .