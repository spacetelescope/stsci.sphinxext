"""
Adds HTML id's to the parameter names in Numpy-formatted HTML.
"""

from docutils import nodes

def setup(app):
    app.connect("doctree-resolved", add_parameter_anchors)

class Visitor(nodes.NodeVisitor):
    def __init__(self, doctree):
        nodes.NodeVisitor.__init__(self, doctree)
        self._function = ''

    def default_visit(self, node):
        pass

    def unknown_visit(self, node):
        pass

    def visit_desc_signature(self, node):
        if len(node['ids']):
            self._function = node['ids'][0]
        else:
            self._function = ''

    def visit_field(self, node):
        if (type(node[0]) == nodes.field_name and
            node[0].astext().strip().lower() == 'parameters'):
            field_body = node[1]
            for subnode in field_body:
                parnode = subnode[0]
                if isinstance(parnode, nodes.strong):
                    if self._function:
                        name = self._function + '-' + parnode.astext()
                    else:
                        name = parnode.astext()
                    parnode['ids'].append(name)

def add_parameter_anchors(app, doctree, fromdocname):
    doctree.walk(Visitor(doctree))

