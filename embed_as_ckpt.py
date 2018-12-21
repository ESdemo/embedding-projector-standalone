import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector
import os

graph = tf.Graph()

log_dir = 'tmp'

embedding_size = 50
vocabulary_size = 200

with graph.as_default():
    embeddings = tf.Variable(
        tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0), name="embedding")
    init_op = tf.global_variables_initializer()

with tf.Session(graph=graph) as session:
    session.run(init_op)
    print(session.run(embeddings))

    # Save the model for checkpoints.
    # Required
    saver = tf.train.Saver()
    # with tf.train.Saver() as saver:
    saver.save(session, os.path.join('tmp', 'model.ckpt'))

    # Create a configuration for visualizing embeddings with the labels in TensorBoard.
    # Required
    with tf.summary.FileWriter(log_dir, session.graph) as writer:
        config = projector.ProjectorConfig()
        embedding_conf = config.embeddings.add()
        embedding_conf.tensor_name = embeddings.name
        projector.visualize_embeddings(writer, config)


    # Write corresponding labels for the embeddings.
    # Optinal
    # with open(log_dir + '/metadata.tsv', 'w') as f:
    #     for i in xrange(vocabulary_size):
    #         f.write(reverse_dictionary[i] + '\n')
