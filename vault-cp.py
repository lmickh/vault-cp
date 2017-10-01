#!/usr/bin/env python3

import config as cfg
import hvac

client_old = hvac.Client(url=cfg.old_url, token=cfg.old_token)
client_new = hvac.Client(url=cfg.new_url, token=cfg.new_token)

for secret in cfg.secrets:
    data = client_old.read(secret).get('data')
    client_new.write(secret, **data)
    print("Copied " + secret)
