# FastAPI Gateway

FastAPI async server, responsible to deliver incoming messages to all of the registered nodes.

Nodes can register to the Gateway's local state, using the  (POST)`/gateway/node` endpoint.



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install -r requirements.txt
```



## Usage

To run the Gateway locally:
```bash
(venv) D:\PycharmProjects\dors-fastapi-gateway-nodes-arch>uvicorn gateway.main:app --host 0.0.0.0 --port 3000 
```
To build the Docker image, run:
```bash
(venv) D:\PycharmProjects\dors-fastapi-gateway-nodes-arch>docker build -t fastapi-gateway -f ./gateway/Dockerfile .
```



### Endpoints

You can see all the available endpoints under:

```
http://127.0.0.1:3000/docs
or
http://127.0.0.1:3000/redoc
```



<img src=".\res\swagger.jpg" alt="swagger" style="zoom: 200%;" />



## License

[MIT](https://choosealicense.com/licenses/mit/)