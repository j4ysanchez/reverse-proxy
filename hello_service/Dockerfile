FROM python:3.12-slim

WORKDIR /app

# Copy the requirements file
COPY src/requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

EXPOSE 8000

CMD ["uvicorn", "hello:app", "--host", "0.0.0.0", "--port", "8000"]