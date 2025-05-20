import nltk
from nltk.draw.tree import TreeView

# 1. 분석할 문장
sent = "I saw the man with a telescope"

# 2. CFG 문법 로딩 (grammar.cfg는 같은 폴더에 있어야 함)
grammar = nltk.data.load("file:grammar.cfg")
parser = nltk.ChartParser(grammar)

# 3. 토크나이즈 + 파싱
tokens = nltk.word_tokenize(sent)
trees = list(parser.parse(tokens))  # 여러 번 쓰려면 list로 변환

# 4. 현재 경로에 result.txt 저장
with open("result.txt", "w") as f:
    if not trees:
        f.write("⚠️ No parse trees were generated.\n")
    for i, tree in enumerate(trees):
        print(tree)
        f.write(tree.pformat() + "\n\n")

# 5. 트리를 .ps(PostScript) 이미지로 저장 (같은 폴더에 생성됨)
for i, tree in enumerate(trees):
    filename = f"tree_{i}.ps"
    TreeView(tree)._cframe.print_to_file(filename)
    print(f"✅ Tree image saved to {filename}")