
# LLM Docker Project

This project is a test for implementing containerization of language models with a HTTP API architecture. The project aims to assess the efficiency and scalability of containerizing language models using Docker. Leveraging Docker's containerization technology, we encapsulate language model implementations, enabling seamless deployment across various environments. Through rigorous testing and performance evaluation, we analyze factors such as resource utilization, deployment overhead, and scalability to provide insights into the effectiveness of containerization for language models. This project serves as a comprehensive study to guide developers and organizations in adopting containerized solutions for deploying and managing language models efficiently.

## Model Description
The model used in the example is Facebook/OPT 350 (with 350 million parameters).
OPT was predominantly pretrained with English text, but a small amount of non-English data is still present within the training corpus via CommonCrawl. The model was pretrained using a causal language modeling (CLM) objective. OPT belongs to the same family of decoder-only models like GPT-3. As such, it was pretrained using the self-supervised causal language modedling objective.

## Application Information
| Python Version | Model       | Framework   |
|----------------|-------------|-------------|
| 3.8.10          | Facebook/OPT 350      | FastAPI  |


## Local Deployment

Install requirements

```bash
  pip install -r requirements.txt
```
Start Uvicorn server

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Docker Installation (if Docker is not present)

```bash
sudo apt-get update
```
```bash
sudo apt install docker.io
```
```bash
docker --version
```

## Pull and run the docker image for this project

```bash
sudo docker image pull souravdas431/llm-test
```

```bash
sudo docker run -dp 127.0.0.1:8000:8000 souravdas431/llm-test
```
