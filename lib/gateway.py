from time import sleep
from requests import post, get, patch
from os import getenv

MAX_RETRIES = int(getenv("GATEWAY_RETRIES"))


def establish_gateway_connection(attempts=0):
    if attempts >= MAX_RETRIES:
        return

    name = "graphql"
    upstream_name = f"{name}_upstream"
    base_url = f'http://{getenv("GATEWAY")}'
    service_url = f"{base_url}/services/{name}"
    upstream_url = f"{base_url}/upstreams/{upstream_name}"

    try:
        service_res = get(url=service_url)

        if service_res.status_code == 404:
            # Create the Kong service
            post(
                url=f"{base_url}/services",
                data={"name": name, "url": base_url},
            )
            print("Kong: Service created")
            # Create the upstream
            post(url=f"{base_url}/upstreams", data={"name": upstream_name})
            print("Kong: Upstream created")
            # Link upstream
            patch(url=service_url, data={"host": upstream_name})
            print("Kong: Upstream linked")
            # Create the route
            post(
                url=f"{service_url}/routes",
                data={"name": name, "paths[]": "/graphql", "strip_path": "false"},
            )
            print("Kong: Route added")

        # Add target
        res = post(
            url=f"{upstream_url}/targets", data={"target": getenv("GRAPHQL_URL")}
        )

        if res.status_code == 200 or res.status_code == 409:
            print("Kong: Connection established")
            return

    except:
        print("Gateway is not available!")

    sleep(0.2)
    establish_gateway_connection(attempts=attempts + 1)