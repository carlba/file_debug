import os
import json

PATH = "/tmp"


def dump_to_file(thing, filename, path=PATH):
    with open(os.path.join(path, filename), 'wb+') as outfile:
        try:
            outfile.write(thing)
        except TypeError:
            outfile.write(json.dumps(thing, indent=4, separators=None, encoding='utf-8'))


def main():
    pass

if __name__ == '__main__':
    main()
