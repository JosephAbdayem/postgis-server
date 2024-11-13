# 🌐 FastAPI & PostGIS Backend with GeoServer

This project provides a FastAPI backend for geospatial data, integrated with **PostGIS** for spatial database support and **GeoServer** for geospatial services. This setup is compatible with client applications such as the [OpenLayers Angular Map Project](https://github.com/JosephAbdayem/openlayers-angular), enabling geospatial data visualization.

## 📋 Prerequisites

Make sure you have:

- **Docker** and **Docker Compose**

## ⚙️ Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/JosephAbdayem/postgis-server.git
   cd postgis-server
   ```

2. **Start the Docker Containers**:

   Use Docker Compose to build and run the containers:

   ```bash
   docker-compose up --build -d
   ```

   - FastAPI API: `http://localhost:8000`
   - GeoServer: `http://localhost:8080`

3. **Access Documentation**:

   - **FastAPI Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **GeoServer**: [http://localhost:8080](http://localhost:8080)

## 🚀 Usage

- **PostGIS Database**: Spatial database support.
- **GeoServer**: Web interface for managing and publishing spatial data via WMS/WFS services.
- **API Endpoints**: FastAPI backend provides CRUD operations for geospatial data in PostGIS.

## 🛠 Running FastAPI

To run the FastAPI server locally (without Docker), use:

```bash
uvicorn app.main:app --reload
```

This command starts the FastAPI server in development mode with automatic reloading.

## 🔄 Running Alembic Migrations

1. **Initialize Alembic (first-time setup only):**

   ```bash
   alembic init migrations
   ```

2. **Create a Migration Script:**

   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

   This command generates a new migration based on the current database schema.

3. **Apply Migrations to the Database:**

   ```bash
   alembic upgrade head
   ```

   This command applies all pending migrations.

## 🔄 Configuration

- **Database settings**: Adjust environment variables (e.g., username, password, and database name) in `docker-compose.yml`.

## 🐋 Docker Commands

To stop the containers:

```bash
docker-compose down
```

To clean up stopped containers and images:

```bash
docker system prune -a
```

## 💬 Issues and Contributions

Open issues for bugs or feature requests. Contributions are welcome via pull requests!