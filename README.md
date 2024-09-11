# 🎥 YouTube Iframe Parser

This Python script extracts YouTube video URLs from HTML `<iframe>` tags and converts them into standard YouTube video links. It specifically focuses on YouTube embeds and returns the short URL format `https://youtu.be/{video_id}`.

## 🚀 Features

- Parses HTML `<iframe>` tags containing YouTube video embeds.
- Converts the embedded URL to the shortened YouTube format: `https://youtu.be/{video_id}`.
- Uses Python's `re` module for regular expression pattern matching.
  
## 🔧 Installation

Clone this repository:

```bash
git clone https://github.com/akshatjaiin/watch.git
cd youtube-iframe-parser
Make sure you have Python installed (version 3.x is recommended).

🛠️ Usage
Run the script:
bash

python watch.py
When prompted, input the HTML containing a YouTube iframe tag:
html

HTML: <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
The script will output the corresponding YouTube short link:
bash
https://youtu.be/dQw4w9WgXcQ
Example

bash
$ python3 script_name.py
HTML: <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
https://youtu.be/dQw4w9WgXcQ
```
🧠 How It Works
The script takes an HTML string input that contains an <iframe> tag embedding a YouTube video.
It uses a regular expression to identify the video ID from the src attribute of the <iframe>.
If a valid YouTube embed is found, it converts the video ID into a shortened YouTube URL format https://youtu.be/{video_id}.
Regular Expression Breakdown
regex


^<iframe.+?(?:https?://)?(?:www.)?youtu(?:.)?be(?:.com)?/(?:embed/)?(\w+).+</iframe>$
^<iframe.+?: Match an <iframe> tag starting from the beginning of the string.
(?
?://)?(?
.)?youtu(?:.)?be(?:.com)?/: Matches various forms of YouTube URLs (with or without http(s) or www).
(?
/)?(\w+): Captures the YouTube video ID.
.+"</iframe>$: Matches the closing </iframe> tag.
example:
![image](https://github.com/user-attachments/assets/efa93a41-3dfd-4936-bb67-fd362fd1ea82)

🤝 Contributing
Feel free to submit a pull request or open an issue if you have suggestions or improvements. All contributions are welcome!

