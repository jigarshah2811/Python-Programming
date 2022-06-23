if __name__ == "__main__":
    ping_result = "200 packates sent. 100 packates recieved. 0.00% lost"
    ping_result = "200 packates sent. 100 packates recieved. 50.00% lost"

    device_status = "device status: connected"
    device_status = "device status: disconnected"

    assert("0.00%" in ping_result)
    assert("connected" in device_status)

    # Instead the words should be devided in list then search
    assert("0.00%" in ping_result.split())
    assert("connected" in device_status.split())
