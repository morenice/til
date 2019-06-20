import pymysql.cursors
from datetime import datetime


class CollectDatabase:
    def __init__(self, host='localhost', port=3306, database=None, user='', passwd=''):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = passwd
        self.logger = None
        self.connection = None

    def __destroy__(self):
        if self.connection:
            self.connection.close()

    def set_logger(self, logger):
        self.logger = logger

    def connect(self):
        self.connection = pymysql.connect(host=self.host,
                                          port=self.port,
                                          user=self.user,
                                          password=self.password,
                                          db=self.database,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def get_latest_block(self):
        with self.connection.cursor() as cursor:
            sql = 'SELECT block FROM transaction_logs ORDER BY timestamp desc LIMIT 1'
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                return result['block']

        return None

    def insert_txns(self, txns):
        with self.connection.cursor() as cursor:
            '''
            CREATE TABLE `transaction_logs` (
            `block` bigint(20) unsigned NOT NULL COMMENT 'block number',
            `tx_hash` varchar(66) NOT NULL COMMENT 'transaction hash',
            `from_address` varchar(42) NOT NULL,
            `to_address` varchar(42) DEFAULT NULL,
            `value` text NOT NULL COMMENT 'ETH',
            `tx_cost` text NOT NULL COMMENT 'actual txn fee',
            `timestamp` bigint(20) unsigned NOT NULL,
            PRIMARY KEY (`tx_hash`),
            KEY `transaction_logs_registered_IDX` (`timestamp`) USING BTREE,
            KEY `transaction_logs_from_registered_IDX` (`from_address`,`timestamp`) USING BTREE,
            KEY `transaction_logs_to_registered_IDX` (`to_address`,`timestamp`) USING BTREE,
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
            '''

            sql = '''INSERT INTO transaction_logs(block, tx_hash, from_address, to_address, value, tx_cost, timestamp)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            values_set = ()
            for txn in txns:
                values_set += (
                    (
                        txn['blockNumber'],
                        txn['hash'],
                        txn['from'],
                        txn['to'],
                        txn['value'],
                        txn['gasPrice'],
                        txn['timestamp']
                    ),
                )
            cursor.executemany(sql, values_set)

        return self.connection.commit()
