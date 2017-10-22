# coding: utf-8

import MeCab
import glob

CORPUS_PATH = './corpus/AA/wiki_*'
NEOLOGD_PATH = '/usr/lib/mecab/dic/mecab-ipadic-neologd'
MIN_COUNT = 3

tagger = MeCab.Tagger('-Ochasen -d ' + NEOLOGD_PATH)
tagger.parse('')

files = glob.glob(CORPUS_PATH)
for file in files:
    fi = open(file, 'r')
    lines = fi.readlines()
    count = 0
    output = ''
    prev_surface = ''
    is_next_skip = False
    for line in lines:
        line = line.rstrip('\n')
        if is_next_skip:
            is_next_skip = False
            continue
        if not line:
            continue
        if line[:9] == '<doc id="':
            is_next_skip = True
            continue
        if line == '</doc>':
            if count >= MIN_COUNT:
                print(output[:-1])
            count = 0
            output = ''
            prev_surface = ''
            continue
        node = tagger.parseToNode(line)
        while node:
            features = node.feature.split(",")
            if features[2] == '人名' and features[3] == '一般':
                if node.surface != prev_surface:
                    output += node.surface.replace(' ', '_') + ' '
                    count += 1
                    prev_surface = node.surface
            node = node.next
    fi.close()
