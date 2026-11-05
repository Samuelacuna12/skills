#!/usr/bin/env python3
"""Prepare a Botcake send_flow call; send only with explicit --send. Stdlib only."""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--page-id', required=True)
    parser.add_argument('--psid', required=True)
    parser.add_argument('--flow-id', required=True, type=int)
    parser.add_argument('--payload-file', help='JSON object with non-secret payload values')
    parser.add_argument('--send', action='store_true', help='Perform one real send; no automatic retries')
    args = parser.parse_args(argv)
    if not re.fullmatch(r'[A-Za-z0-9_-]+', args.page_id):
        parser.error('page-id must be an account ID, not a URL or path')
    if args.flow_id <= 0 or not args.psid.strip() or any(ord(c) < 32 for c in args.psid):
        parser.error('flow-id must be positive and psid must be nonempty without control characters')
    body = {'psid': args.psid, 'flow_id': args.flow_id}
    if args.payload_file:
        try:
            with open(args.payload_file, encoding='utf-8') as stream:
                payload = json.load(stream)
        except (OSError, ValueError):
            parser.error('payload-file must be a readable, valid JSON file')
        if not isinstance(payload, dict):
            parser.error('payload-file must contain a JSON object')
        body['payload'] = payload
    url = f'https://botcake.io/api/public_api/v1/pages/{args.page_id}/flows/send_flow'
    if not args.send:
        print(json.dumps({'mode': 'preview_no_network', 'method': 'POST', 'url': url, 'body': body}, ensure_ascii=False, indent=2))
        return 0
    token = os.environ.get('BOTCAKE_ACCESS_TOKEN', '').strip()
    if not token or '\n' in token or '\r' in token:
        parser.error('set BOTCAKE_ACCESS_TOKEN outside the repository before --send')
    request = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), headers={
        'access-token': token, 'Content-Type': 'application/json'}, method='POST')
    try:
        opener = urllib.request.build_opener(NoRedirect())
        with opener.open(request, timeout=30) as response:
            data = json.loads(response.read(1024 * 1024))
        if not isinstance(data, dict) or data.get('success') is not True:
            print('API did not confirm success. Inspect the authorized contact history before repeating.', file=sys.stderr)
            return 1
        print('API accepted the flow. Verify delivery in Botcake/contact history.')
        return 0
    except urllib.error.HTTPError as error:
        # Do not echo body, request headers, token, or customer data.
        print(f'HTTP {error.code}. No retry performed; verify status before another send.', file=sys.stderr)
    except (OSError, ValueError, urllib.error.URLError):
        print('No reliable success confirmation. Delivery may have occurred; check history before repeating.', file=sys.stderr)
    return 1

if __name__ == '__main__':
    sys.exit(main())
