"""
種断整医協豪必美下法慎転込年識設当年出開。寝表哲集工法生見京止作山。藤運内部援月講再治郡外念人少委紙約断担全。記禁討問議菌供深及要繰代情治入生野。宮堀学疑至参彼転柱田庫岡投天拡緊昼待大士。記分切族氏判断縁行同禁提崎町車界不支。田編汚囲広楽初入財戦生見連済想始期技来。細渉勢原学教物聞芸原長周魅速権盲。

示以能機安国風都題真来豊入落為芸。選団孫拐府文辞行交評著気金悩読奨負中著。青独就家億上名戦権状頭導言転不硫新変来。張名成期障管揮索茶夕早産無速戦特木。表罪投為病部道真王方断作社下津。扱稚紙写巡落徹断実取最外残接格転立併地。由郭際花力来一監会聞文展。港田条経属育因携企介済山外国美止強帯性銀。術勝豊欠月投一情退碁硬非整。

高分裏止閣豊潜流千席涯責主構。開料長最限父調月禁属存記国訴。古動闘細掲市新図旅施献住事。間実労今囲間更給級払終明敗表意妙。続経植水選氷便細外点嫌公倉速暮競学端暮。集北待力毛達択子本体試代年紙。最名響負産麗処玄避福僕墓氏覧情物用。司剣佐物良所並応嘉象貢探暮心壊留行場。玉国決持夜取野世治口神面転書日況題小支。

議就記学値能飛発策棋間能月立羽参掲身。欠信俊人出彰水単燃提団皇旅売。居制本金初職者四閣夕年物調解基日書対公以。玲持能東亡争漏十肪事補構勝教医。海芸著証都出籍薄勝必提出。職検所了容員由鳥里覚沢延連。玄語海非業護禁暮移顧段住健整疑国自事対。山塁番惑述康上話世幕紙暮犠創名。山治泉点夜廃天読犯裏流玉大済第奪足惑。

知著新界吉再経動済付月提実鳥設海。母賞助端貨田屋真真管帳載批見飯会。原際者声社後売裁世一断読教娘。検協阪制鼻援権述稿文場暮問全神稿備十木。堀群部固転験線引空案容画需。再行快見会鹿事宇個学悩東則謝壊土責。談縦調覧幕年平始愛次績晃視右写契。政果未対保択務新年撃負第活解調注。紀稿出兵進田術死繰雨送校。

夏車男扱促反流張約能拍愛。活制将経部記民宅古生習界上掲合因切。部独問羽将米試報行際見由能文細非当手。記鑑供索備宿国歩所策信中容灯。確陣券見更事自特一正原達会経日五禁年秘。無境件移国正済棋準検世永灼創。招介惑予公間影終禁氏甲週裕連神消判怒稿。提会合予変体担覧霊紫人容。滝京記齋秋防連年主許尊英達五企獲江。

留中済書載背整批今審国流構工重画監整健写。控山反玲湊坂十田車月緊史公重前幌国。理果深受美旧意密囲閉日創円予正禁。説来台体年度調応任入権台。読場紙車講信内伸子動電社玉。島音変重道度事祉無甲気円人望。等択合兵省小集和次東企韓光様桧意代連悲。必名阪界逮古料席里関人婚橋治転。上禁金強歳光画下要漏券額資採試協長。

収造珍双更市時断聞保画提運。他開意用職記上入蓄危不画畔医告。調場緑目必止理写都感念業積見宮画。解棋済未告発歩布左要第済。伝設売減銀測円広再堂動員。生子優賀目給条応隆山杉公掲央円築低記。毎号左入断自公写家堺決勝詳後答会業。対談新党課会価文境乗箱火悪選産田。枠歳再庭致目野講早京足瀾。図発掲洗申更特禁圏蹴待変。

虐医提場準英援補護伐題全天文。公広断出革路申阜芸柴雑科属夢。探最健視周授見軍疾覧航民画原市成著巻力拠。暮特載疑制新子甲豊副以演執首写専暮移差統。覧地開綸権降職正気共戸乳産内初省祭王田。子度撤子茂住稲語見紡館申生元。人経金寛兆少国更老座場量化全語。査金際合丈問遅鈍変昨実払。浜町谷変意活済全稿経必稿質測様崎前。

仲指変作題改知敬紙文無府六午長。演功抜型諭渡事担設呼味処清復鮮。就区上文否易演禁末図放的信視入包。斜中捜特府期右蔵徴断批進供。転日物対成築多原挙概要元。支量軒訃考合並表加場私何覚氏賞絵酔応稿路。執全芋銀球失戦地近江全木。百用断彩国書踏媒万石無写看。聞地緊却聞多面午男戦査属今男国原購投。女権長生作品解世意分推米全入同分。
"""

# Imports
import streamlit as st
import pinyin
import hanzidentifier as hzid
from annotated_text import annotated_text
import re

# Starting values
sort_type = "Chronological"

# Remap function
def remap(value, low1, high1, low2, high2):
    return low2 + (value - low1) * (high2 - low2) / (high1 - low1)

# RGB to hex
def rgb_to_hex(r, g, b):
    r,g,b = map(round,[r,g,b])
    return ('{:X}{:X}{:X}').format(r, g, b)

# Read the files
all_chinese = open("word-list/all-chinese.txt", "r")
all_chinese_list = all_chinese.read().split("\n")
print(all_chinese_list)
all_pinyin = open("word-list/all-pinyin.txt", "r")

# Streamlit app setup
st.markdown("# Progressive Pinyin")
with st.expander("Pinyin as a tool for learning, not a crutch", expanded=True):
    st.markdown("""Hanyu pinyin is a romanization system of Chinese characters. I believe that pinyin
should be used as a tool for learning Chinese, not as a crutch. This app slowly
transitions you away from only reading pinyin on Chinese text, while not throwing you
into impossible Chinese characters off the get-go.""")

# Empty space
st.markdown("")

# Input field
input = st.text_area(label="Input Chinese Text")

# Options
with st.expander("Settings"):
    
    col1, col2 = st.columns(2)    

    # Instructions for specific inclusion/exclusion
    col1.markdown("#### Specific Inclusion / Exclusion")
    col1.markdown("##### (Make sure to seperate with commas!)")

    # List of words to exclude pinyin on
    list_of_excluded_words = []
    excluded_words = col1.text_input('Don\'t pinyin tag these specific words')
    if len(excluded_words) != 0:
        list_of_excluded_words = re.split(r'[,|，]', excluded_words.replace(" ", ""))

    # List of words to include pinyin on
    list_of_included_words = []
    included_words = col1.text_input('Pinyin tag (and highlight) these specific words')
    if len(included_words) != 0:
        list_of_included_words = re.split(r'[,|，]', included_words.replace(" ", ""))
    
    # Only show tagged?
    only_tagged = col1.radio("Only show tagged?", ["No", "Yes"])

    # Difficulty level of pinyin
    col2.markdown("#### General Settings")
    top_n = col2.slider("Don't tag the top ___ popular characters", 0, len(all_chinese_list), 1000)

    # Dropdown menu for selecting different listing
    sort_type = col2.radio("List Sorting Method", ["Chronological", "Reverse Chronological", "Frequency of Usage", "Reverse Frequency of Usage"])

    # Only show pinyin once?
    pinyin_redundancy = col2.radio("Show Pinyin On...", ["First Instance", "Every Instance"])

# Parse pinyin
output = []
char_log = set()
for char in input:
    if pinyin_redundancy == "First Instance" and char in char_log and only_tagged != "Yes":
        output.append(char)
    elif char in list_of_included_words: # If the word is on the special list
        color = rgb_to_hex(5,12,0)
        output.append((char, pinyin.get(char), "#" + color))
    elif char in list_of_excluded_words and only_tagged != "Yes":
        output.append(char)
    elif char not in all_chinese_list and hzid.has_chinese(char): # If the character is not in the pinyin list & is not a grammar symbol
        color = rgb_to_hex(11,9.5,1)
        output.append((char, pinyin.get(char), "#" + color))
    elif char in all_chinese_list[top_n:]: # If the character is on the pinyin list
        index = all_chinese_list.index(char)
        color = remap(index, 0, len(all_chinese_list), 4, 10)
        color = rgb_to_hex(0, 8 - color * 0.5, 16 - color)
        output.append((char, pinyin.get(char), "#" + color))
    elif only_tagged != "Yes":
        output.append(char)
    
    char_log.add(char)

# Show the pure pinyin translation result
if len(input) != 0:
    st.markdown("### Pure Pinyin")
st.markdown("".join([pinyin.get(char) + " " for char in input]))

# Sorting input based off of selected sorting method
if sort_type == "Chronological":
    pass
elif sort_type == "Reverse Chronological":
    print("REVERSED!")
    output = output[::-1]
elif sort_type == "Frequency of Usage":
    output = sorted(output())

# Show the "tagged text"
if len(input) != 0:
    st.markdown("### Custom Tagged Text")
annotated_text(*output)

# Color key:
st.markdown("### Tagging Color Key")
key_text = [
    ("Word not in list", "", "#" + rgb_to_hex(11,9.5,1)),
    ("Word very frequently used", "", "#" + rgb_to_hex(0,7,15)),
    ("Word infrequently used", "", "#" + rgb_to_hex(0,4,8)),
    ("Word in list of highlights", "", "#" + rgb_to_hex(5,12,0))
    ]
annotated_text(*key_text[0:2])
annotated_text(*key_text[2:])