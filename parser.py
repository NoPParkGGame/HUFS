import nltk
from nltk.tree import Tree

# 문장 및 문법 불러오기
sent = "Some people will look forward to watching the concert"
grammar = nltk.data.load("file:grammar.cfg")
parser = nltk.ChartParser(grammar)

tokens = nltk.word_tokenize(sent)
trees = list(parser.parse(tokens))

# 결과 텍스트 저장
with open("result.txt", "w") as f:
    for tree in trees:
        f.write(tree.pformat() + "\n\n")
        print(tree)

# 트리를 텍스트 기반 이미지로 저장 (GUI 없이)
for i, tree in enumerate(trees):
    filename = f"tree_{i}.ps"
    with open(filename, "w") as f:
        tree.pretty_print(stream=f)
    print(f"✅ 트리 저장 완료: {filename}")