#! /usr/bin/env python3
import datetime as dt
import hashlib as hl
import json


class Blockchain:

    def __init__(self):
        self.chain = []
        initial_block = self.create_block(
            index = 1, data = "initial block", proof = 1, previous_hash = "0"
        )
        self.chain.append(initial_block)

    def create_block(self, index: int, data: str, proof: int, previous_hash: str) -> dict:
        block = {
            "index" : index,
            "timestamp" : str(dt.datetime.now()),
            "data" : data,
            "proof" : proof,
            "previous_hash" : previous_hash
        }
        return block

    def get_previous_block(self) -> dict:
        return self.chain[-1]