FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy project files
# COPY pyproject.toml uv.lock ./

# Install dependencies with uv
# RUN uv sync --frozen

# Copy application code
COPY app.py .

EXPOSE 5000

# Run the app with uv
CMD ["uv", "run", "python", "app.py"]