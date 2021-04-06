import json

from jwcrypto.jws import JWS


class Authorization:
    def resolve(self, next, root, info, **args):
        headers = info.context.headers
        if "Authorization" in headers:
            token = JWS()
            token.deserialize(headers["Authorization"].removeprefix("Bearer "))

            byte_payload = token.objects.pop("payload")
            json_payload = byte_payload.decode("UTF-8")
            payload = json.loads(json_payload)
            return next(root, info, **args, token=payload)

        return next(root, info, **args)
