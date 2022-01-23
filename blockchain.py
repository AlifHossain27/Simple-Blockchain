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

    def mine_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        index = len(self.chain) + 1
        proof = self.proof_of_work(
            previous_proof = previous_proof,
            index = index,
            data = data
            )
        previous_hash = self._hash(block=previous_block)

    def get_previous_block(self) -> dict:
        return self.chain[-1]

    def _to_digest(self, new_proof: int, previous_proof: int, index: int, data: str) -> bytes:
        to_digest = str(new_proof ** 2 - previous_proof ** 2 + index) + data
        # It returns an utf-8 encoded version of the string
        return to_digest.encode()

    def _hash(self,block: dict) -> str:
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hl.sha256(encoded_block).hexdigest()

    def proof_of_work(self, previous_proof: str, index: int, data: str,) -> int:
        new_proof = 1
        check_proof = False
        
        while check_proof == False:
            to_digest = self._to_digest(
                new_proof = new_proof,
                previous_proof = previous_proof,
                index = index,
                data = data
                )
            hash_operation = hl.sha256(to_digest).hexdigest()

            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1

        return new_proof
