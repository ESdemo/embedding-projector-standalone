# coding: utf-8
"""
参考：
https://www.zhihu.com/question/31780325

"""
import numpy as np

in_file = 'raw_data/facebook/fasttext.zh.30000.300d_tensor.tsv'
# in_file = 'test.data'
out_file = 'oss_data/fasttext.zh.30000.300d_tensor.bytes'

emb = np.fromfile(in_file, dtype=float, sep=" ")
emb = emb.reshape([30000, 300])



with open(out_file, 'wb') as f:
  for line in emb:
    for value in line:
      f.write(value.tobytes())
      f.write(str.encode('\t'))
    f.write(str.encode('\n'))

# a = [1.0]
# print(np.asarray(a).tobytes())
# a = [1.0, 2.000]
# print(np.asarray(a).tobytes())
#
# with open('file', 'wb') as f:
#   f.write(np.asarray(a).tobytes())




"""
from array import array
output_file = open('file', 'wb')
float_array = array('d', emb)
float_array.tofile(output_file)
output_file.close()
"""



