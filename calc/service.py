import tensorflow as tf

class CalcService:

    def __init__(self):
        pass

    @staticmethod
    def calc(num1, num2, opcode):
        sess = tf.Session()
        saver = tf.train.import_meta_graph('calc/saved/model-1000.meta')
        saver.restore(sess, tf.train.latest_checkpoint('calc/saved/'))
        graph = tf.get_default_graph()
        w1 = graph.get_tensor_by_name("w1: 0")
        w2 = graph.get_tensor_by_name("w2: 0")
        feed_dict = {w1: float(num1), w2: float(num2)}
        if opcode == 'multi':
            op_to_restore = graph.get_tensor_by_name("op_to_restore:0")

        result = sess.run(op_to_restore, feed_dict)
        return  int(result)