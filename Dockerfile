FROM python:3.11.2-alpine3.16

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .

# Set the entrypoint to run the cli tool
ENTRYPOINT [ "python", "main.py" ]

CMD ["{\"player1\": { \"movimientos\": [\"DSD\", \"S\"], \"golpes\": [\"P\", \"\"] }, \"player2\": { \"movimientos\": [\"\", \"ASA\", \"DA\", \"AAA\", \"\", \"SA\"], \"golpes\": [\"P\", \"\", \"P\", \"K\", \"K\", \"K\"] } }"]
