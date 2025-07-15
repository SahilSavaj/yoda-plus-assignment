import re


range_delimiters = ["-", "..", "~", " to "]


def parse_string(string: str, output_type: str = "str"):
    all_strings = string.split(",")

    if not string or not all_strings:
        return []

    result = []
    for s in all_strings:
        s = s.strip()

        if not s:
            continue

        for delim in range_delimiters:
            if delim in s:
                ranges = [d.strip() for d in s.split(delim)]
                if re.fullmatch(r"\d+", "".join(ranges)):
                    first = int(ranges[0].strip())
                    second = int(ranges[1].strip())
                    if second < first:
                        raise Exception(f"Invalid range {s}")
                    result += list(range(first, second + 1))
                else:
                    raise Exception(f"Invalid input {s}")
                break
        else:
            if re.fullmatch(r"\d+", s):
                result.append(int(s))
            else:
                raise Exception(f"Invalid input {s}")

    return result


if __name__ == "__main__":
    # print(parse_string("1-3,5,7-9"))
    # print(parse_string("a,1-b"))
    # print(parse_string("1 -3, 5,7 - 9"))
    # print(parse_string(" , 1-3 ,5,,7-9 "))
    # print(parse_string(" , 1-3 ,5 to 7,,7..9,9~11 "))
    print(parse_string("1-3,5,7-9,9-3"))
