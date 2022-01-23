#! /usr/bin/env python3
import datetime as dt
import hashlib as hl
import json


class Blockchain:

    def __init__(self):
        self.chain = []
        initial_block = self.create_block(
            data="initial block", proof=1, previous_hash="0", index=1
        )
        self.chain.append(initial_block)

    def create_block(self, data: str, proof: int, previous_hash: str, index: int) -> dict:
        block = {
            "index" : index,
            "timestamp" : str(dt.datetime.now()),
            "data" : data,
            "proof" : proof,
            "previous_hash" : previous_hash
        }
        return block