import unittest
from helpers.queuehelper import QueueName, QueueType, QueueEntry, QueueEntries

class TestQueuenames(unittest.TestCase):
    def test_queue_valid_name(self):
        self.assertTrue(QueueName.has_value(QueueName.Q_ALERT.value))

    def test_queue_invalid_name(self):
        self.assertFalse(QueueName.has_value('notaqueuename'))

    def test_queue_alert(self):
        self.assertTrue(str(QueueName.Q_ALERT) == 'q_alert')

    def test_queue_value(self):
        self.assertTrue(QueueName.value(QueueName.Q_ALERT) == 'alert')

    def test_queue_type(self):
        self.assertTrue(QueueType.broadcast == 'broadcast')
        self.assertTrue(QueueType.publish == 'publish')

    def test_queue_entry(self):
        que = QueueEntry('', '', '')
        self.assertTrue(que)

    def test_queue_entries(self):
        que = QueueEntries()
        self.assertTrue(que)
        que.add('test', 'test')
        que.addbroadcast('qbroad', 'test')
        que.addalert('msg')
        self.assertTrue(que.hasentries())

if __name__ == '__main__':
    unittest.main()
