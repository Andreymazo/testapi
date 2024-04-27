#!/bin/bash

# curl "http://localhost:8000/query" -d "cad_num=23&shirota=25&dolgota=55" -X CET

curl -X GET http://127.0.0.1:8000/query -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'