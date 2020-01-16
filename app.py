import bjoern
import gkmsg

from horseman.meta import Overhead
from horseman.routing import RoutingNode
from horseman.response import reply
from horseman.validation import Validator
from schema import Schema, And


class Request(Overhead):

    __slots__ = ('environ', 'params', 'data', 'method', 'content_type')

    def __init__(self, environ, **args):
        self.environ = environ
        self.params = args
        self.data = {}
        self.method = environ['REQUEST_METHOD']
        if self.method in ('POST', 'PATCH', 'PUT'):
            self.content_type = environ.get(
                'CONTENT_TYPE', 'application/x-www-form-urlencoded')
        else:
            self.content_type = None

    def set_data(self, data):
        self.data = data


class Application(RoutingNode):
    request_type = Request


app = Application()


message = Schema({
    'type': And(str, lambda s: len(s) > 6),
    'body': And(str, lambda s: len(s) > 15)
})


@app.route('/test', methods=['POST'])
@Validator(message)
def test(request):
    import pdb
    pdb.set_trace()
    return reply(body=b'This is a test')


bjoern.run(app, '127.0.0.1', 8080)
