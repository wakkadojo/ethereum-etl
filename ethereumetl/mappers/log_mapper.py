
# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from ethereumetl.domain.log import EthLog
from ethereumetl.utils import hex_to_dec


class EthLogMapper(object):

    def json_dict_to_block(self, json_dict):

        log = EthLog()
        log.removed = json_dict.get('removed')
        log.log_index = hex_to_dec(json_dict.get('logIndex'))
        log.transaction_index = hex_to_dec(json_dict.get('transactionIndex'))
        log.transaction_hash = json_dict.get('transactionHash')
        log.block_hash = json_dict.get('blockHash')
        log.block_number = hex_to_dec(json_dict.get('blockNumber'))
        log.address = json_dict.get('address')
        log.data = json_dict.get('data')
        log.topics = json_dict.get('topics')

        return log

    def web3_dict_to_log(self, dict):
        
        log = EthLog()

        log.removed = dict.get('removed')
        log.log_index = dict.get('logIndex')

        transaction_index = dict.get('transactionIndex')
        transaction_hash = dict.get('transactionHash')
        if transaction_hash is not None:
            transaction_hash = transaction_hash.hex()
        log.transaction_hash = transaction_hash

        block_hash = dict.get('blockHash')
        if block_hash is not None:
            block_hash = block_hash.hex()
        log.block_hash = block_hash

        log.block_number = dict.get('blockNumber')
        log.address = dict.get('address')
        log.data = dict.get('data')

        if 'topics' in dict:
            log.topics = [topic.hex() for topic in dict['topics']]

        return log

    def log_to_dict(self, log):
        return {
            'type': 'log',
            'removed': log.removed,
            'log_index': log.log_index,
            'transaction_index': log.transaction_index,
            'transaction_hash': log.transaction_hash,
            'block_hash': log.block_hash,
            'block_number': log.block_number,
            'address': log.address,
            'data': log.data,
            'topics': log.topics,
        }
