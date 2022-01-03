
from pathlib import Path

import lupa
from lupa import LuaRuntime


lua = LuaRuntime()
make_doc = lua.eval(f"function(...) {Path('docs/tools/makedoc.lua').read_text()} end")

out = Path("out/docs/")
out.mkdir(exist_ok=True, parents=True)


input = Path("docs/docs")
for file in input.iterdir():
    if file.suffix == ".lua" and not file.stem.startswith("."):
        doc = make_doc(f"docs/docs/{file.name}")
        o = out / file.stem
        o.mkdir(exist_ok=True)
        (o / "docs.json").write_text(doc.json)
        (o / "snippets").mkdir(exist_ok=True)
        for snippet in doc.snippets:
            (o / "snippets" / snippet).write_text(doc.snippets[snippet])
