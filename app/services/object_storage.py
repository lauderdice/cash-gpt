

class S3Wrapper():
    def save_file(self, payload: bytes):
        raise NotImplementedError

    def get_file(self, address: str):
        raise NotImplementedError