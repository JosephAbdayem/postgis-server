# 🌐 FastAPI & PostGIS Backend with GeoServer

This project provides a FastAPI backend for geospatial data, integrated with **PostGIS** for spatial database support and **GeoServer** for advanced geospatial services. This backend can be used with a client application, such as the [OpenLayers Angular Map Project](https://github.com/JosephAbdayem/openlayers-angular), to serve and visualize spatial data.

## 📋 Prerequisites

Ensure the following dependencies are installed:

- **Docker**: For containerization.
- **Docker Compose**: To manage multi-container Docker applications.
- **FastAPI**: Installed and configured within the Docker container.

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JosephAbdayem/postgis-server.git
cd postgis-server
```

### 2. Start the Docker Containers

Use Docker Compose to build and run the containers. This command sets up the FastAPI application, PostgreSQL with PostGIS, and GeoServer.

```bash
docker-compose up --build
```

- `--build` ensures fresh images are built for any recent code changes.
- The FastAPI API will be available at `http://localhost:8000`.
- GeoServer will be accessible at `http://localhost:8080`.

### 3. Access API Documentation and GeoServer

- **FastAPI Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **FastAPI ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **GeoServer**: [http://localhost:8080](http://localhost:8080)

## 🚀 Usage

- **PostGIS Database**: A spatial database in PostgreSQL with PostGIS support.
- **GeoServer**: Provides a web interface for managing and publishing geospatial data as WMS/WFS services.
- **API Endpoints**: The FastAPI backend provides endpoints for CRUD operations on geospatial data stored in PostGIS.

### Example API Request

To retrieve geospatial data:

```http
GET /geodata
```

Additional endpoints can be explored in the Swagger UI or ReDoc interfaces.

## 🔄 Customization

- **Database Configuration**: Environment variables (e.g., username, password, and database name) can be adjusted in `docker-compose.yml`.
- **GeoServer**: Adjust GeoServer settings within its admin interface or configure WMS layers as needed.

## 🛠 Project Structure

- **FastAPI**: Acts as the main API framework.
- **PostGIS/PostgreSQL**: Provides spatial capabilities to the database.
- **GeoServer**: Handles web map services (WMS) and web feature services (WFS) for visualizing geospatial data.
- **Docker Compose**: Manages multi-container applications to isolate and control each service.

## 🐋 Docker Commands

To stop the Docker containers:

```bash
docker-compose down
```

To clean up all stopped containers and images:

```bash
docker system prune -a
```

## 💬 Issues and Contributions

Feel free to open issues for any bugs or feature requests. Contributions are welcome through pull requests to help improve the project!

## 📜 License

This project is licensed under the [MIT License](LICENSE).