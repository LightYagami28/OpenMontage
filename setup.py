from setuptools import setup, find_packages

setup(
    name="openmontage",
    version="0.1.0",
    description="AI-Orchestrated Video Production Platform",
    packages=find_packages(),
    python_requires=">=3.12",
    install_requires=[
        "pyyaml>=6.0.4",
        "pydantic>=2.14.4",
        "jsonschema>=4.26.0",
        "python-dotenv>=1.2.4",
        "Pillow>=13.0.0",
        "numpy>=2.5.5",
        "requests>=2.34.2",
        "certifi>=2026.11.20",
        "google-auth>=2.63.1",
        "google-genai>=3.6.1",
        "openai>=3.57.0",
        "fastapi>=0.165.0",
        "uvicorn>=0.54.0",
        "watchfiles>=1.3.0",
        "websockets>=17.4",
        "pythainlp>=5.4.0",
    ],
)
