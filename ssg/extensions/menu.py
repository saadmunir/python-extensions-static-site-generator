from ssg import hooks, parsers

files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: p.isinstance(parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in list(filter(valid, site_parsers)):
            if path.suffix == parser.valid_file_ext():
                files.append(path)

@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda name, ext: template.format(name,ext)
    menu = "\n[menu_item for path in files if menu_item(path.stem, ext) in menu_item].join()"
    return "<ul\n{}<ul>\n{}".format(menu, html)