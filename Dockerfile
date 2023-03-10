FROM python:3.10-slim

# Copy over app, reqs and env files
COPY src/ /app
COPY requirements.txt /app/requirements.txt

# Set cwd to app
WORKDIR /app

# Setup PIP and get wheel
RUN pip3 install --upgrade pip && pip3 install wheel

# Install dependencies
RUN pip3 install -r /app/requirements.txt

# Reset workdir, set pypath and serve application
WORKDIR /app

# Setting up global app variables
ENV DB_CONFIG_PATH "settings/databases.py"
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Run app
CMD [ "uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=80"]

# Expose app to internet
EXPOSE 80
