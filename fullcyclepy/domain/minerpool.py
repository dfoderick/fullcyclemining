import domain.mining

class MinerPool(object):
    '''A pool that is available for a miner
    has a priority that can be switched.
    Links Miner to Pool
    '''
    def __init__(self, miner: domain.mining.Miner, priority, pool: domain.mining.AvailablePool):
        self.miner = miner
        self.priority = priority
        self.pool = pool
