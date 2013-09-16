def setup(app):
    app.add_node(wordcount)
    app.add_directive('wordcount',WordcountDirective)
    app.connect('doctree-resolved', process_wordcount_nodes)

from docutils import nodes

class wordcount(nodes.General, nodes.Element):
    pass

from sphinx.util.compat import Directive

class WordcountDirective(Directive):
    has_content = True

    def run(self):
        return [wordcount('')]

def process_wordcount_nodes(app, doctree, fromdocname):
    env = app.builder.env
    count=0
    for node in doctree.traverse(nodes.paragraph):
        tt=node.astext()
        tt.split(" ")
        count+=len(tt)

    for node in doctree.traverse(wordcount):
        para = nodes.paragraph()
        para += nodes.Text("%d words" % count)
        node.replace_self([para])
        
        

