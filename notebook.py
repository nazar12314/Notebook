import datetime


class Notebook:
    def __init__(self):
        self.notes = []

    def search(self, filter: str):
        result = []
        for note in self.notes:
            for tag in filter:
                if note.match(tag):
                    result.append(note)
        return result

    def new_note(self, memo, tags=[]):
        note = Note(memo, tags)
        self.notes.append(note)

    def modify_memo(self, note_id, memo):
        if len(self.notes) < note_id:
            self.notes[note_id].memo = memo

    def modify_tags(self, note_id, tags):
        if len(self.notes) < note_id:
            self.notes[note_id].tags = tags


class Note:
    def __init__(self, memo, tags):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.datetime.now()

    def match(self, search_filter: str):
        return search_filter in self.tags


def main():
    notebook = Notebook()
    while True:
        print("\nWrite <create> to create new post,\n <exit> to exit,\n <find> to find some post,\n <modify> to modify some post\n")
        level_one_response = input(">>> ")
        if level_one_response == "create":
            print("Write text for your note: ", end="")
            text = input()
            print("Write tags for your note separated by koma: ", end="")
            tags = list(map(lambda x: x.strip(), input().split(",")))
            notebook.new_note(text, tags)
        elif level_one_response == "find":
            if notebook.notes:
                print("Write a tag (or tags separated by koma): ", end="")
                tags = input()
                tags = list(map(lambda x: x.strip(), input().split(","))) if "," in tags else [tags]
                result = notebook.search(tags)
                for idx, note in enumerate(result):
                    print()
                    print("Found notes:")
                    print(f"<{idx + 1}> - {note.creation_date}\n{note.memo}")
                    print()
            else:
                print("There are no notes in your Notebook")
        elif level_one_response == "modify":
            print("Write id (number) of the note that you want to modify: ", end="")
            id = input()
            try:
                id = int(id)
                note = notebook.notes[id]
            except Exception:
                print("Invalid id")
                continue
            else:
                print("Write <text> to modify text or <tags> to modify tags")
                response = input()
                if response == "text":
                    print("Write text:")
                    text = input(">>> ")
                    note.memo = text
                elif response == "tags":
                    print("Write tags for your note separated by koma: ", end="")
                    tags = list(map(lambda x: x.strip(), input().split(",")))
                    note.tags = tags
        elif level_one_response == "exit":
            break
        else:
            print("Invalid input!")
            continue


if __name__ == '__main__':
    main()
