import os
from urllib.parse import quote
from pyperclip import copy

templates = {
	"metadata": """
/**
 * @name New emojis
 * @author bth123
 * @authorId 567014541507035148
 * @version 1.0
 * @description ✨ Theme with new emojis from message bar
 * @website https://github.com/bth123/new-ds-emojis
 * **/
 """,

	"chat": """
.emoji[data-name=":{name}:"], .emoji[data-name="{associated_emoji}"] {{
  content: url("https://github.com/bth123/new-ds-emojis/blob/main/emojis/{link_name}.png?raw=true");
}}""",

	"reaction_list": """
.emoji__32c91[alt="{associated_emoji}"] {{
	content: url("https://github.com/bth123/new-ds-emojis/blob/main/emojis/{link_name}.png?raw=true");
}}""",

	"emoji_menu":"""
.emojiItem_b15dee[data-name="{name}"] .emojiSpriteImage__6363e {{
  opacity: 0;
}}
.emojiItem_b15dee[data-name="{name}"] {{
  background-size: 45px, 45px;
  background-position: center;
  background-repeat: no-repeat;
  background-image: url("https://github.com/bth123/new-ds-emojis/blob/main/emojis/{link_name}.png?raw=true");
}}""",
	
	"emoji_menu_preview": """
.emoji__92b46[alt=":{name}:"] {{
  content: url("https://github.com/bth123/new-ds-emojis/blob/main/emojis/{link_name}.png?raw=true");
}}""",

	"emoji_menu_preview_multiple_variants": """
.emoji__92b46[alt=":{names}:"] {{
  content: url("https://github.com/bth123/new-ds-emojis/blob/main/emojis/{link_name}.png?raw=true");
}}"""
}

files = os.listdir("emojis")

png_files = [file for file in files if file.lower().endswith('.png')]
with open("theme.css", "w", encoding="utf-8") as theme:
	theme.write(templates["metadata"])
with open("theme.css", "a", encoding="utf-8") as theme:
	for png_file in png_files:
		# Seting up vars
		png_name = png_file[:-5].split(" ")[0]
		associated_emoji = png_file[-5:-4]
		link_name = quote(png_file[:-4])
		# Compiling css
		theme.write(templates["chat"].format(name=png_name, associated_emoji=associated_emoji, link_name=link_name))
		theme.write(templates["reaction_list"].format(associated_emoji=associated_emoji, link_name=link_name))
		theme.write(templates["emoji_menu"].format(name=png_name, link_name=link_name))
		if " " in png_file:
			theme.write(templates["emoji_menu_preview_multiple_variants"].format(name=png_name, link_name=link_name, names=": :".join(png_file[:-5].split(" "))))
		else:
			theme.write(templates["emoji_menu_preview"].format(name=png_name, link_name=link_name))

with open("theme.css", "r", encoding="utf-8") as theme:
	copy(theme.read())
