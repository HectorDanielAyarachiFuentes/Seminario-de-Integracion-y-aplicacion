import typst

doc = """
#set page(paper: "a4", numbering: "1 / 1")
#show heading.where(level: 1): it => [
  #text(fill: blue)[#it.body]
]

= Test Heading
Hello world!
"""

with open("test.typ", "w", encoding="utf-8") as f:
    f.write(doc)

try:
    typst.compile("test.typ", output="test.pdf")
    print("Success")
except Exception as e:
    print("Error:", e)
