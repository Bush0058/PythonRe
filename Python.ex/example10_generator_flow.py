def api_flow():
    print("First step")
    yield

    print("Second step")
    yield

    print("Last step")


flow = api_flow()

next(flow)
next(flow)
next(flow)
