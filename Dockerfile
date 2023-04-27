# docker build -t fastapi-image .

# docker run -d --name fastapi-container  -p 8000:8000 fastapi-image

FROM python:3.10

# Setup working directory
RUN mkdir code
WORKDIR /code

# Copy requirements file to our working directory
COPY ./requirements.txt /code/requirements.txt

# Install packages - Use cache dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pwd
# Copy our code over to our working directory
COPY ./ /code/

# Run our project exposed on port 80
CMD ["python","-m","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "./app/log.ini"]
