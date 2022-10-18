import os
import sys


def countlines(start, lines=0, num_of_files=0, header=True, begin_start=None):
    if header:
        print('{:>10} | {:<20}'.format('LINES_IN_FILE', 'FILE'))
        print('{:->11}|{:->20}'.format('', ''))

    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isfile(thing) and thing.endswith('.py'):
            num_of_files += 1
            with open(thing, 'r') as f:
                newlines = f.readlines()
                newlines = len(newlines)
                lines += newlines

                if begin_start is not None:
                    reldir_of_thing = '.' + thing.replace(begin_start, '')
                else:
                    reldir_of_thing = '.' + thing.replace(start, '')

                print('{:>10} | {:<20}'.format(newlines, reldir_of_thing))

    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isdir(thing):
            lines, num_of_files = countlines(thing, lines, num_of_files, header=False, begin_start=start)

    return lines, num_of_files


def main():
    total_line_count, num_of_files = countlines(sys.argv[1])
    print(f'Total Lines: {total_line_count}')
    print(f'Number of Files: {num_of_files}')


if __name__ == '__main__':
    main()
