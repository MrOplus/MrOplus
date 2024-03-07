import feedparser


def main():
    url = "https://medium.com/feed/@mroplus"  # Medium user feed
    feed = feedparser.parse(url)
    template_file = open("README.md.template", "r", encoding="utf-8")
    template = template_file.read()
    posts = ""
    for post in feed.entries:
        posts += f"* [{post.title}]({post.link})\n"
    template = template.replace("{{POSTS}}", posts)
    template_file.close()
    readme = open("README.md", "w", encoding="utf-8")
    readme.write(template)
    readme.close()


if __name__ == '__main__':
    main()
