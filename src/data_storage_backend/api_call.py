import requests
import json
import cbor2

# Configuration
CANISTER_ID = "<your_canister_id>"
IC_HOST = "https://<ic_host>"  # e.g., ic0.app or localhost:8000 for local testing
IC_API_URL = f"{IC_HOST}/api/v2/canister/{CANISTER_ID}/call"
HEADERS = {"Content-Type": "application/cbor"}

def call_canister(method_name, arg):
    payload = {
        "method_name": method_name,
        "arg": cbor2.dumps(arg)  # Encode the argument to CBOR
    }
    response = requests.post(IC_API_URL, data=cbor2.dumps(payload), headers=HEADERS)
    return cbor2.loads(response.content)  # Decode the CBOR response

def store_value(key, value):
    result = call_canister("put", (key, value))
    print("Stored:", result)

def fetch_value(key):
    result = call_canister("fetch", key)
    print("Fetched:", result)
    return result

def remove_value(key):
    result = call_canister("remove", key)
    print("Removed:", result)

if _name_ == "_main_":
    # Replace these with actual values
    store_value("myKey", "myValue")
    fetch_value("myKey")
    remove_value("myKey")