import re

range_delimiters = ["-", "..", "~", " to "]
step_delimiters = [":"]


def parse_string(string: str, output_type: str = "str"):
    all_strings = string.split(",")
    if not string or not all_strings:
        return []

    result = []
    for s in all_strings:
        s = s.strip()
        if not s:
            continue

        matched = False
        for delim in range_delimiters:
            if delim in s:
                result += parse_range_with_step(s, delim)
                matched = True
                break

        if not matched:
            result.append(parse_single_value(s))

    return result


def parse_range_with_step(s: str, range_delim: str):
    start, end, step = split_range_and_step(s, range_delim)
    start, end, step = validate_and_parse_numbers(start, end, step)
    return generate_range(start, end, step)


def split_range_and_step(s: str, range_delim: str):
    parts = s.split(range_delim)
    if len(parts) != 2:
        raise Exception(f"Invalid range: {s}")
    start = parts[0].strip()
    end_step = parts[1].strip()

    step = None
    for step_delim in step_delimiters:
        if step_delim in end_step:
            end, step = end_step.split(step_delim)
            return start, end.strip(), step.strip()
    return start, end_step, None


def validate_and_parse_numbers(start, end, step):
    if not (re.fullmatch(r"\d+", start) and re.fullmatch(r"\d+", end)):
        raise Exception(f"Invalid input: start={start}, end={end}")

    start, end = int(start), int(end)

    if step is not None:
        if not re.fullmatch(r"\d+", step):
            raise Exception(f"Invalid step: {step}")
        step = int(step)
        step = -abs(step) if end < start else abs(step)
    else:
        step = 1 if end >= start else -1

    return start, end, step


def generate_range(start, end, step):
    if (step > 0 and start > end) or (step < 0 and start < end):
        raise Exception(
            f"Incompatible step and range: start={start}, end={end}, step={step}"
        )
    return list(range(start, end + (1 if step > 0 else -1), step))


def parse_single_value(s: str):
    s = s.strip()
    if re.fullmatch(r"\d+", s):
        return int(s)
    raise Exception(f"Invalid input: {s}")


if __name__ == "__main__":
    # print(parse_string("1-3,5,7-9"))
    # print(parse_string("a,1-b"))
    # print(parse_string("1 -3, 5,7 - 9"))
    # print(parse_string(" , 1-3 ,5,,7-9 "))
    # print(parse_string(" , 1-3 ,5 to 7,,7..9,9~11 "))
    # print(parse_string("1-3,5,7-9,9-3"))
    print(parse_string("1-5:x"))
