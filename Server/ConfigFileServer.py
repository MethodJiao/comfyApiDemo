from aiohttp import web
import os
import sys
import aiofiles
import argparse

routes = web.RouteTableDef()
script_path = os.path.realpath(os.path.dirname(sys.argv[0]))

parser = argparse.ArgumentParser(description='这是一个命令行参数示例')
parser.add_argument('--listen', type=str, help='监听地址默认为127.0.0.1', default='127.0.0.1')
parser.add_argument('--port', type=int, help='监听端口默认为80', default=80)

@routes.get("/getworkflowfile")
async def get_req(request):
    request_version = request.query['version']
    json_file_path = script_path + "\\" + request_version + "\\workflow.json"
    async with aiofiles.open(json_file_path, 'r', encoding='UTF-8') as file:
        json_content = await file.read()
        return web.Response(text=json_content)

if __name__ == '__main__':
    args = parser.parse_args()
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host=args.listen, port=args.port)
