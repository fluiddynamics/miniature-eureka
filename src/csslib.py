import jinja2

templates = {
    "flex_template1": """
{{selector}} {
  display: flex;
  flex-direction: column;
}
""",
    "flex_template2": """
{{selector}} {
  display: flex;
}
""",
    "border": """
{{selector}} {
   border-{{place}}:{{width}} {{type}};
}
""",
    "font": """
{{selector}} {
  font-size: 12px;
  font-family:'Consolas', monospace;
}
""",
    "width-span": """
{{selector}} {
  width: {{width}};
  text-align: center;
}
""",
    "width-div": """
{{selector}} {
  width: {{width}};
  justify-content: space-evenly;
}
""",
    "fit": """
{{selector}} {
  width: fit-content;
}
""",
    "debug": """
{{selector}} {
  padding: 3px;
  border:solid 1px;
  margin-top:2px;
  margin-left:2px;
  background:{{color}};
}
{{selector}}.none {
  background:red;
}
{{selector}} > span {
  padding: 3px;
  border:solid 1px;

}
""",
    "dispnone": """
{{selector}}.none {
  display:none;
}
""",
    "padding": """
{{selector}} {
  padding-top:{{size}};
  padding-bottom:{{size}};
}
""",
    "header": """
{{selector}} {
  font-weight:bold;
  position:sticky;
  top:0;
  background-color:white;
  border-top:1px solid;
  z-index:1;
  border-bottom:1px solid;
}
""",
    "sticky": """
{{selector}} {
  position:sticky;
  left:{{left}};
  background-color:white;
}
""", "navy": """
{{selector}} {
  color:navy;
}
""", "note": """
.setumei {
  margin:1em;
  font-family:sans-serif;
}
.setumei p {
  display:list-item;
  list-style-type:disc;
}
"""
}

jn = {k: jinja2.Template(v) for k, v in templates.items()}


class CssWriter():
    def __init__(self, file):
        self.file = file

    def orientation(self, data):
        self.orientation = data
        tmp = ""
        sel = ".main"
        for a in data:
            match a:
                case "V":
                    tmp += jn["flex_template1"].render({"selector": sel})
                case "H":
                    tmp += jn["flex_template2"].render({"selector": sel})
                case _:
                    raise ValueError("")
            sel += " > div"
        self.file.write(tmp)

    def debug(self, i = None):
        if i is None:
            i = len(self.orientation)
        cols = ["ffffdd", "ffddff", "ddffff",
                "ffdddd", "ddffdd", "ddddff", "dddddd"]
        tmp = ""
        sel = ".main"
        for a in range(i):
            tmp += jn["debug"].render({"selector": sel,
                                      "color": "#"+cols[a]})
            sel += " > div"

        self.file.write(tmp)

    def border0(self, i, place, add="", width="1px", type="solid"):
        sel = ".main" + " > div" * i + add
        self.file.write(jn["border"].render(
            {"selector": sel, "place": place, "width": width, "type": type}))

    def border_around(self, i):
        self.border0(i, "bottom")
        self.border0(i, "right")

    def border_mid(self, i, type="dashed", add=0):
        place = {"V": "bottom", "H": "right"}[self.orientation[i-1]]
        sel1 = ".main" + " > div" * i + ":not(:last-of-type):not(.header)"

        if add == 0:
            self.file.write(jn["border"].render(
                {"selector": sel1, "place": place, "width": "1px", "type": type}))
            return

        def pseudo(a):
            return ":last-of-type" if self.orientation[i+a] == self.orientation[i-1] else ""

        for a in range(add):
            sel1 = sel1 + "> div" + pseudo(a)
        
        sel2 = sel1 + "> div" + pseudo(add)
        sel3 = sel1 + "> span" + pseudo(add)

        self.file.write(jn["border"].render(
            {"selector": sel2, "place": place, "width": "1px", "type": type}))
        self.file.write(jn["border"].render(
            {"selector": sel3, "place": place, "width": "1px", "type": type}))

    def font(self):
        sel = ".main"
        self.file.write(jn["font"].render({"selector": sel}))

    def width(self, i, w, span=False):
        if span:
            sel = ".main" + " > div" * i + "> span"
            self.file.write(
                jn["width-span"].render({"selector": sel, "width": w}))
        else:
            sel = ".main" + " > div" * i
            self.file.write(
                jn["width-div"].render({"selector": sel, "width": w}))

    def fit(self, i):
        sel = ".main" + " > div" * i
        self.file.write(jn["fit"].render({"selector": sel}))

    def undisplay(self, i):
        sel = ".main" + " > div" * i
        self.file.write(jn["dispnone"].render({"selector": sel}))

    def padding(self, pad):
        sel = ".main span"
        self.file.write(jn["padding"].render(
            {"selector": sel, "size": pad}))

    def header(self):
        sel = ".main div.header"
        self.file.write(jn["header"].render({"selector": sel}))

    def sticky(self, i, left = "0px"):
        sel = ".main" + " > div" * i + ">span"
        self.file.write(jn["sticky"].render({"selector": sel, "left": left}))

    def note(self):
        self.file.write(jn["note"].render())

    def navy(self, cls):
        sel = ".main ." + cls
        self.file.write(jn["navy"].render({"selector": sel}))
