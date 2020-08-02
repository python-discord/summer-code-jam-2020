def create_url_query_parameters(base_url: str, params: dict) -> str:
    """Creates a url for the given base address with given parameters
    as a query string."""

    parameter_string = "&".join(f"{key}={value}"
                                for key, value in params.items())
    url = f"{base_url}?{parameter_string}"

    # skip the last character as it is a &
    return url[:-1]
