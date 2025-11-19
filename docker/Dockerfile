FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    git \
    build-essential \
    imagemagick \
    && rm -rf /var/lib/apt/lists/*

# Install Quarto
RUN wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.550/quarto-1.4.550-linux-amd64.deb && \
    dpkg -i quarto-1.4.550-linux-amd64.deb && \
    rm quarto-1.4.550-linux-amd64.deb

# Copy requirements files
COPY requirements.txt requirements.sh ./

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install Quarto extensions
RUN chmod +x requirements.sh && \
    ./requirements.sh

# Copy project files
COPY . .

# Verify installations
RUN python --version && \
    quarto --version && \
    pip list

# Expose port for preview
EXPOSE 5000

# Default command
CMD ["quarto", "preview", "--port", "5000", "--host", "0.0.0.0"]
