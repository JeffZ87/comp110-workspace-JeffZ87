def final_streaking(streaks: str) -> str:
    final_streak: str = ""
    final_max: int = 0
    temp_streak: str = ""
    temp_max: int = 0

    for char in streaks:
        # if char != final_streak and char != temp_streak:
        #     temp_streak = char
        #     temp_max = 1
        # el
        if char == temp_streak:
            temp_max += 1
        elif char != temp_streak:
            temp_streak = char
            temp_max = 1
        if temp_max >= final_max:
            final_streak = temp_streak
            final_max = temp_max
    return final_streak + str(final_max)


print(final_streaking("ABA"))
print(final_streaking("AABA"))
print(final_streaking("AABAAA"))
print(final_streaking("AABBBAA"))
print(final_streaking("TAARRR!"))
print(final_streaking("HEELSS"))
print(final_streaking("U N CCC U NN CC N N N N N N N N C"))