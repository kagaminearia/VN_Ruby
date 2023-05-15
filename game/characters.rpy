# 此文件用于定义角色以及对应图片

image ctc_icon:
    "gui/page_reminder.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat 

# 角色名
define ruby = Character("露比", image="ruby",ctc="ctc_icon", ctc_pause = "ctc", ctc_position = "nestled")
define l = Character("里昂")
define m = Character("大臣",ctc="ctc_icon",ctc_pause = "ctc_icon", ctc_timedpause = "ctc_icon",ctc_position = "fixed")
define ra = Character("起义军之首")
define rs = Character("起义军兵士")
define fa = Character("追随者A")
define fb = Character("追随者B")
define cs = Character("群众")
define ca = Character("平民A")
define cb = Character("平民B")
define s = Character("仆人")
define p = Character("神官")
define rea = Character("教徒A")
define res = Character("众教徒")
define co = Character("康拉德")
define j = Character("少年")
define va = Character("村民A")
define ad = Character("阿代尔")
define gra = Character("盗墓贼A")
define grb = Character("盗墓贼B")
define bi = Character("主教")


# 角色立绘
image ruby smile = "images/ruby smile.png"
image ruby concerned = "ruby_concerned.png"

#image side ruby smile = "side_ruby_smile.png"
image side ruby = "others/side_ruby.png"

image imgframe = "others/imgframe.png"