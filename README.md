# Inventory-management
This is simple application consisting of integration of frontend and backend for inventory management.


# FastAPI Demo - Products API

A simple FastAPI application demonstrating GET and POST endpoints for product management and inventory tracking.

# Analogy
 - Node = uvicorn [Server to run FastAPI]
 - React = FastAPI [Python web framework]

## Features

- **GET /**: Welcome endpoint
- **GET /products/**: Get all products
- **GET /products/{product_id}**: Get a specific product by ID
- **POST /products/**: Create a new product

## Setup

1. **Create and activate virtual environment:** # This creates an isolated Python environment specificaly for this project
   ```bash
   python -m venv myenv
   myenv\Scripts\activate.ps1  # Windows PowerShell #Activates and open virtual terminal
   ```

   # For second time you just need to activate thevirtual environment

2. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

3. **Run the application:**
   ```bash
   uvicorn main:app --reload #Default port is 8000
   ```

4. **Access the API:**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Project Structure

```
invoTrack/
├── main.py          # FastAPI application with endpoints
├── models.py        # Pydantic models
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## API Usage Examples

### Get all products
```bash
curl http://localhost:8000/products/
```

### Get product by ID
```bash
curl http://localhost:8000/products/1
```

### Create a new product
```bash
curl -X POST "http://localhost:8000/products/" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 5,
       "name": "Monitor",
       "description": "4K monitor",
       "price": 299.99,
       "quantity": 15
     }'
```

## Models

### Product
- `id`: integer
- `name`: string
- `description`: string
- `price`: float
- `quantity`: integer

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints
- [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation
