from httpx._models import Response


class IboxResponsehh(Response):
    key: str = None

    def secretkey(self, key):
        self.key = key


if __name__ == '__main__':
    ibox = IboxResponsehh(status_code=200)
    ibox.secretkey('abc')
    print(ibox.key)