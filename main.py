import re


def parse_string(string: str, output_type: str = "str"):
    all_strings = string.split(",")

    result = []
    for s in all_strings:
        s = s.strip()
        if "-" in s:
            ranges = s.replace(" ", "").split("-")
            if re.fullmatch(r"\d+", "".join(ranges)):
                first = int(ranges[0].strip())
                second = int(ranges[1].strip())
                result += list(range(first, second + 1))

        elif re.fullmatch(r"\d+", s):
            result.append(int(s))

    return result


if __name__ == "__main__":
    # print(parse_string("1-3,5,7-9"))
    # print(parse_string("a,1-b"))
    # print(parse_string("1 -3, 5,7 - 9"))
    print(parse_string(" , 1-3 ,5,,7-9 "))
