"""Call the three fixed operations of CARDZ's public, stateless JSON-RPC API."""
import json
import re
from pathlib import Path

import httpx

ENDPOINT = 'https://mcp.cardz.game/mcp'
SCHEMAS = json.loads(Path(__file__).with_name('schemas.json').read_text(encoding='utf-8'))
MAX_RESPONSE = 2 * 1024 * 1024


def validate_arguments(name, arguments):
    if name not in SCHEMAS or not isinstance(arguments, dict):
        raise ValueError('Use a supported CARDZ tool and an object of parameters.')
    schema = SCHEMAS[name]
    properties = schema['properties']
    if set(arguments) - set(properties):
        raise ValueError('Unsupported CARDZ parameter.')
    # Dify sends blank optional form fields; omit these without changing required values.
    arguments = {key: value for key, value in arguments.items()
                 if key in schema['required'] or value not in ('', None)}
    if set(schema['required']) - set(arguments):
        raise ValueError('Check the required and supported CARDZ parameters.')
    for key, value in arguments.items():
        field = properties[key]
        if field['type'] == 'string':
            if not isinstance(value, str) or not value.strip() or len(value) > field.get('maxLength', 160):
                raise ValueError(f'Invalid {key}.')
            if 'pattern' in field and not re.fullmatch(field['pattern'], value):
                raise ValueError(f'Invalid {key}.')
        if field['type'] == 'integer':
            if type(value) is not int and not (type(value) is float and value.is_integer()):
                raise ValueError(f'{key} must be an integer.')
            if not field['minimum'] <= value <= field['maximum']:
                raise ValueError(f'{key} is outside the supported range.')
            arguments[key] = int(value)
        if 'enum' in field and value not in field['enum']:
            raise ValueError(f'Unsupported {key}.')
    return arguments


def call_tool(name, arguments):
    arguments = validate_arguments(name, arguments)
    payload = {'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call',
               'params': {'name': name, 'arguments': arguments}}
    headers = {'Accept': 'application/json, text/event-stream',
               'Content-Type': 'application/json', 'MCP-Protocol-Version': '2025-11-25'}
    try:
        with httpx.stream('POST', ENDPOINT, json=payload, headers=headers,
                          timeout=20, follow_redirects=False) as response:
            response.raise_for_status()
            if response.headers.get('content-type', '').split(';')[0] != 'application/json':
                raise ValueError('Unexpected CARDZ response format.')
            body = bytearray()
            for chunk in response.iter_bytes():
                body.extend(chunk)
                if len(body) > MAX_RESPONSE:
                    raise ValueError('CARDZ response exceeds the supported size.')
        envelope = json.loads(body)
        result = envelope.get('result', {})
        if envelope.get('error') or result.get('isError') or not isinstance(result.get('structuredContent'), dict):
            raise ValueError('CARDZ could not complete this public query.')
        return result['structuredContent']
    except (httpx.HTTPError, ValueError, TypeError, AttributeError) as error:
        raise ValueError('CARDZ query failed. Check the public card parameters or try again later.') from error
