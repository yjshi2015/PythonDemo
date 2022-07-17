from httpx._models import Response
import typing
from httpx._types import (
    AsyncByteStream,
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
    RawURL,
    RequestContent,
    RequestData,
    RequestFiles,
    ResponseContent,
    SyncByteStream,
)
from httpx._models import Request


class IboxResponsehh(Response):
    key: str = None

    def __init__(self, status_code: int,
                 key: typing.Optional[str] = None):
        super(IboxResponsehh, self).__init__(status_code)
        self.key = key

    def secretkey(self, key):
        self.key = key


if __name__ == '__main__':
    ibox = IboxResponsehh(status_code=200)
    ibox.secretkey('abc')
    print(ibox.key)