from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
اهلا {}

مرحباً {}

انا بوت استطيع استخراج كود تريمكس وبايروجرام 
هذا البوت بواسطة @Tepthon
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" بدء استخراج الجلسة 🖥️", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 رجوع 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton(" بدء استخراج الجلسة 🖥️", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton(" بدء استخراج الجلسة 🖥️", callback_data="generate")],
        [InlineKeyboardButton("  قناة السورس ", url="https://t.me/Tepthon")],
        [
            InlineKeyboardButton("كيفيه استعمال البوت ❔", callback_data="help"),
            InlineKeyboardButton("حول 📜", callback_data="about")
        ],
        [InlineKeyboardButton(" احصل على مساعدة ↗️", url="https://t.me/Tepthon_Support")],
    ]

    # Help Message
    HELP = """
✨ ** الأوامر المتاحة ** ✨

/about - حول البوت 
/help - للحصول على مساعدة 
/start - لبدء البوت 
/generate - توليد استخراج الجلسة 
/cancel - للإلغاء استخراج الجلسة 
/restart - عمل اعادة تشغيل للبوت
"""

    # About Message
    ABOUT = """
**حول هذا البوت** 

بوت تليجرام لإنشاء جلسة بايروجرام واستخراج تيليثون بواسطة @Tepthon

برمجة البوت : [Pyrogram](docs.pyrogram.org)

لغة البوت : [Python](www.python.org)

المطور : @P17_12
    """
