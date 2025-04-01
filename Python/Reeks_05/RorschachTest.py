
def rorschach(fileName, output=None):
    """
    >>> rorschach('pattern.txt')
    ++...+..+++..+++..+...++
    ....++............++....
    .+.#####+######+#####.+.
    ...#@#@#.#@##@#.#@#@#...
    .+.#####.##@@##.#####.+.
    ....+.+...####...+.+....
    .....+............+.....
    ....+.....####.....+....
    ....+..+..#@@#..+..+....
    ......###.####.###......
    +...++#@#.+..+.#@#++...+
    ....#####......#####....
    ....#@#....++....#@#....
    ++..###.+......+.###..++
    +.....+..........+.....+
    >>> rorschach('pattern.txt', 'rorschach.txt')
    """

    outputstr = ''
    with open(fileName, 'r', encoding='UTF-8') as file:
        for line in file:
            line = line.rstrip()
            outputstr += line + line[::-1] + '\n'


    if output is not None:
        with open(output, 'w', encoding='UTF-8') as out_file:
            out_file.write(outputstr)
    else:
        print(outputstr.strip())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
