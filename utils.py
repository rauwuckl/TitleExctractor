import xml.etree.ElementTree as ET
import numpy as np
import re

def load_tree(filepath):
    tree = ET.parse(filepath)
    return tree

def get_coordinates_of_textboxes(textboxes):
    """

    :param textboxes: list of elements with tag textbox
    :return: a numpy array with the start coordinates
    """
    topL = list()
    topR = list()
    bottomL = list()
    bottomR = list()

    def add_tuple_to_lists(tL, tR, bL, bR):
        topL.append(float(tL))
        topR.append(float(tR))
        bottomL.append(float(bL))
        bottomR.append(float(bR))

    for textbox in textboxes:
        bbox = textbox.attrib["bbox"]
        coords = bbox.split(",")
        add_tuple_to_lists(*coords)

    return [np.array(c) for c in [topL, topR, bottomL, bottomR]]

def structure_text_sting(text):
    """
    Takes a string with font annotations and returns a list of dict objects. (one for each block of text)
    :param text: a string with "[font face=...] blabla [/font]" annotations
    :return: a list of dicionaries, one for each block of text in certain font. each has the fields 'font', 'size', 'text', 'l_text'
    """
    if text is None:
        return []

    regex_string = '\[font face="([a-zA-Z\-]*)" size="(\d+\.\d*)"]([^[]*)\[\/font\]'
    pattern = re.compile(regex_string)

    matches = re.findall(pattern, text)
    collector = list()
    for m in matches:
        f = dict(font=m[0], size=float(m[1]), text=m[2], l_text=len(m[2]))
        collector.append(f)

    return collector



