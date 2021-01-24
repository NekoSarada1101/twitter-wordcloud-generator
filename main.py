import emoji


def main(keyword: str):
    remove_emoji_keyword = remove_emoji(keyword)  # type: str


def remove_emoji(src_str: str) -> str:
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)



if __name__ == "__main__":
    input_word = sys.argv  # type: list
    main(input_word[1])
