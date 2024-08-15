# Gebruik een officiële Python runtime als basisimage
FROM python:3.11-slim

# Stel de werkdirectory in
WORKDIR /app

# Kopieer de dependencies file naar de container
COPY requirements.txt .

# Installeer de dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de rest van de code naar de container
COPY . .

# Expose de poort waarop de applicatie draait
EXPOSE 8000

# Definieer het commando om de applicatie te starten
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
