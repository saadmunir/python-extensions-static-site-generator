from ssg import hooks, parsers

files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: p.isinstance(parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in path.suffix:
            if parser.valid_file_ext:
                files.append(path)

@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda name, ext: template.format(name,ext, name.title())
    menu = "\n".join([menu_item for path in files if menu_item(path.stem, ext) in menu_item])
    return "<ul>\n{}<ul>\n{}".format(menu, html)