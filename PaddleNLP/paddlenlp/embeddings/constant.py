# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum

# FIXME(zhoushunjie): only for test
URL_ROOT = "http://127.0.0.1:8080"

PAD_WORD = '[PAD]'
UNK_WORD = '[UNK]'

PAD_IDX = 1
UNK_IDX = 0


# FIXME(zhoushunjie): CorpusName is related to training setting of word2vec, need to modify
class CorpusName(Enum):
    SOGOU_NEWS = 0


CORPUS_NAME_MAP = {
    CorpusName.SOGOU_NEWS:
    "sgns.target.word-word.dynwin5.thr10.neg5.dim300.iter5"
}
