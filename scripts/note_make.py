#!/usr/bin/python3

import time

class NoteMem():

    def __init__(self):
        self.all_notes = {}
        self.note_id = 0

    def printnotes(self):
        for note in self.all_notes:
            print ()
            print(self.all_notes[note]["title"]+"\t"+time.asctime(self.all_notes[note]["timestamp"]))
            print()
            print(self.all_notes[note]["content"])
            print()


    def makenote(self,title="", content="", timestamp=time.localtime()):
        
            if str(title):
                self.title = title
            else:
                self.title = str(input("Title: "))

            if str(content):
                self.content = content
            else:
                self.content = (input("Content: "))
        
            self.note_id += 1
            
            note = {"note_id" : self.note_id,
                    "title" : self.title,
                    "timestamp" : timestamp,
                    "content": self.content }
            
            self.all_notes[self.note_id]=note

if __name__ == "__main__":
    notes = NoteMem()
