import os

templates = {
	"chat": """
.emoji[data-name=":{name}:"] {{
  content: url("https://github.com/bth123/new-ds-emojis/blob/9fb4e51a2a6fc2bf68e77959f796311790d8f468/emojis/{name}.png?raw=true");
}}""",

	"emoji_menu":"""
.emojiItem_b15dee[data-name="{name}"] .emojiSpriteImage__6363e {{
  opacity: 0;
}}
.emojiItem_b15dee[data-name="{name}"] {{
  background-size: 45px, 45px;
  background-position: center;
  background-repeat: no-repeat;
  background-image: url("https://github.com/bth123/new-ds-emojis/blob/9fb4e51a2a6fc2bf68e77959f796311790d8f468/emojis/{name}.png?raw=true");
}}""",
	
	"emoji_menu_preview": """
.emoji__92b46[alt=":{name}:"] {{
  content: url("https://github.com/bth123/new-ds-emojis/blob/9fb4e51a2a6fc2bf68e77959f796311790d8f468/emojis/{name}.png?raw=true");
}}""",

	"emoji_menu_preview_multiple_variants": """
.emoji__92b46[alt=":{names}:"] {{
  content: url("https://github.com/bth123/new-ds-emojis/blob/9fb4e51a2a6fc2bf68e77959f796311790d8f468/emojis/{name}.png?raw=true");
}}"""
}

try:
	files = os.listdir("emojis")
	
	png_files = [file for file in files if file.lower().endswith('.png')]
	with open("theme.css", "a") as theme:
		for png_file in png_files:
			png_name = png_file[:-4].split(" ")[0]
			theme.write(templates["chat"].format(name=png_name))
			theme.write(templates["emoji_menu"].format(name=png_name))
			if " " in png_file:
				theme.write(templates["emoji_menu_preview_multiple_variants"].format(name=png_name, names=": :".join(png_file[:-4].split(" "))))
			else:
				theme.write(templates["emoji_menu_preview"].format(name=png_name))
except:
	print("saygex")
