from wordcloud import WordCloud
 
FONT_PATH = "./NotoSerifJP-Regular.otf"
TXT_NAME = "./yurry_cannon"
 
 
def get_word_str(text):
    import MeCab
    import re
 
    mecab = MeCab.Tagger()
    parsed = mecab.parse(text)
    lines = parsed.split('\n')
    lines = lines[0:-2]
    word_list = []
 
    for line in lines:
        tmp = re.split('\t|,', line)
        print(tmp)
        # 名詞のみ対象
        if tmp[1] in ["名詞","動詞"]:
            # さらに絞り込み
            if tmp[2] in ["一般", "固有名詞","自立"]:
                word_list.append(tmp[7])
 
    return " " . join(word_list)
 
 
# テキストファイル読み込み
read_text = open(TXT_NAME + ".txt", encoding="utf8").read()
 
# 文字列取得
word_str = get_word_str(read_text)
 
# 画像作成
wc = WordCloud(font_path=FONT_PATH, max_font_size=100,width=900,height=600,prefer_horizontal=1).generate(word_str)
 
# 画像保存（テキストファイル名で）
wc.to_file(TXT_NAME + ".png")