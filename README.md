# 🧠 FastAPI ML API with Docker

This is a complete **Machine Learning API** built using **FastAPI**, containerized with **Docker** for easy deployment. It includes model development, validation using Pydantic schemas, and a clean Docker workflow.

> 💡 This project is a guided implementation from [CampusX's YouTube series](https://www.youtube.com/watch?v=WJKsPchji0Q&list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ). Huge credit to them for the detailed walkthrough!

---

## 📦 Project Structure
├── dockerfile # Dockerfile to containerize the FastAPI app
├── .dockerignore # Ignore unnecessary files during Docker build
├── ml.ipynb # Jupyter notebook to train and test ML model
├── main.py # FastAPI app with endpoint(s)
├── requirements.txt # Python dependencies
├── pyproject.toml # Optional project metadata
├── uv.lock # Optional lock file (used with uv tool)
├── schema/
│ └── schema.py # Pydantic models for request/response validation
└── README.md # Project documentation

## 🚀 How to Run the Project
# Pull the image from Docker Hub
docker pull mohitjoshi906/fastapi-app:v1

# Run the container and map port 8000 of your machine to port 8000 inside the container
docker run -p 8000:8000 mohitjoshi906/fastapi-app:v1

 -- Access the API
Once the container is running, open your browser:

🔹 http://localhost:8000/docs
