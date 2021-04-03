import asyncio

from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from common.configuration.constants import ENDPOINT_POST_RESOURCE, ENDPOINT_GET_RESOURCE, ENDPOINT_GATEWAY_POST_NODE, \
    ENDPOINT_GATEWAY_GET_NODE, ENDPOINT_GET_RESOURCE_WITHOUT_ID
from common.model.resource import Resource
from gateway.core.gateway_state import GatewayState

app = FastAPI()
state = GatewayState()


@app.post(ENDPOINT_POST_RESOURCE)
async def broadcast_post_resource(resource: Resource):
    """
    Broadcasts 'post resource' request to every
    known node.
    :param resource: Resource object containing the 'message' data.
    :return: 200 (HTTP_OK) if successful.
    """
    async with AsyncClient(app=app) as client:
        all_results = await asyncio.gather(
            *[post_async(f'{domain}{ENDPOINT_POST_RESOURCE}', client, domain, resource)
              for domain in state.nodes])

    return JSONResponse(status_code=status.HTTP_200_OK, content={'responses': all_results})


@app.get(ENDPOINT_GET_RESOURCE)
async def broadcast_get_resource(id: int):
    """
    Broadcasts 'get resource' to obtain the message with the given id
    from every known node.
    :param id: The Message id to query
    :return: 200 (HTTP_OK) if successful.
    """
    async with AsyncClient(app=app) as client:
        all_results = await asyncio.gather(
            *[get_async(f'{domain}{ENDPOINT_GET_RESOURCE_WITHOUT_ID}', domain, client, params={'id': id})
              for domain in state.nodes])

    return JSONResponse(status_code=status.HTTP_200_OK, content={'responses': all_results})


@app.post(ENDPOINT_GATEWAY_POST_NODE)
def gateway_post_node(request: Request):
    """
    Receives nodes registration to the local state.
    :param request: Request object containing the host and the ip of the client.
    :return: 201 (HTTP_201_CREATED) if successful.
    """
    client_domain = f'{request.client.host}:{request.client.port}'
    print(f'New Node registration: {client_domain}')
    is_added = state.add_node(client_domain)
    if is_added:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=client_domain)
    else:
        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content=client_domain)


@app.get(ENDPOINT_GATEWAY_GET_NODE)
def gateway_get_nodes():
    """
    Gets a snapshot of the nodes in the local state.
    :return: 200 (HTTP_OK) if successful.
    """
    return state.nodes


async def get_async(url: str, domain: str, client: AsyncClient, params: dict):
    res = await client.get(url, params=params)
    return {domain: res.json()}


async def post_async(url: str, client: AsyncClient, domain: str, resource: Resource):
    res = await client.post(url, data=resource.dict())
    return {domain: res.json()}
