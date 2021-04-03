import httpx
from fastapi import FastAPI
from loguru import logger
from starlette import status
from starlette.responses import JSONResponse

from common.configuration.conf_handler import ConfHandler
from common.configuration.constants import ENDPOINT_POST_RESOURCE, ENDPOINT_GET_RESOURCE, \
    ENDPOINT_GATEWAY_POST_NODE
from common.model.node import Node
from common.model.resource import Resource
from node.core.state.node_state import NodeState

app = FastAPI()
config = ConfHandler(conf_file_path='./node/res/config.yaml')
config.read_from_file()
state = NodeState()


def register_in_gateway():
    gateway_endpoint = f"http://{config.conf['gateway']['hostname']}:{config.conf['gateway']['port']}" \
                       f"{ENDPOINT_GATEWAY_POST_NODE}"
    logger.debug(f'Gateway url: {gateway_endpoint}')
    node = Node(hostname=state.hostname, port=state.port)
    data = node.dict()
    headers = {'Content-Type': 'application/json'}
    logger.debug(f'Gateway req data : {data}')
    res = httpx.post(gateway_endpoint, json=data, headers=headers)
    logger.debug(f'Gateway sync response: {res}')


register_in_gateway()


@app.post(ENDPOINT_POST_RESOURCE)
async def post_resource(resource: Resource):
    """
    Precessing the given message and adds it to the node state.
    :param resource: Resource object containing the 'message' data.
    :return: 200 (HTTP_OK) if successful.
    """
    message_id = state.add_message(resource.message)
    logger.debug(f'post_resource message: {message_id}')
    return JSONResponse(status_code=status.HTTP_200_OK, content={'id': message_id})


@app.get(ENDPOINT_GET_RESOURCE)
async def get_resource(id: str):
    """
    Gets the message with the given id
    from the node's state.
    :param id: The Message id to query
    :return: 200 (HTTP_OK) if successful.
    """
    try:
        return JSONResponse(status_code=status.HTTP_200_OK, content=state.get_message_by_id(id))
    except KeyError:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={'reason': f'message with id {id} not found'})
