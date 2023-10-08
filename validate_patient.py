from fhir.resources.bundle import Bundle

import requests
#Configure Requests
session = requests.Session()
BASE_URL = "http://0.0.0.0:5560/fhir"
headers = {
    "User-Agent": "Jasper FHIR Client",
    "Content-Type": "application/fhir+json;charset=utf-8",
    "Accept": "application/fhir+json;charset=utf-8",
}
session.headers.update(headers)

#Search for Patients by family name

resp = session.get(f"{BASE_URL}/Patient?family=Navarro")

#validate response

bundle = Bundle.parse_raw(resp.text)
