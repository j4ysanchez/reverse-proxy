FROM python:3.12-slim

WORKDIR /app

# Copy the requirements file
COPY src/requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

EXPOSE 9000

CMD ["uvicorn", "locations:app", "--host", "0.0.0.0", "--port", "9000"]