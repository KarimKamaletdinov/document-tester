from docx import Document
from docx.text.font import Font


def test_document(document, font_name: str, top_margin: int, right_margin: int, bottom_margin: int, left_margin: int) \
        -> set[str]:
    def get_font_name(style, last_style=None):
        if style.font.name is None:
            if style.base_style is None:
                if last_style is not None:
                    style = last_style
                if doc.styles[style.name].font.name is None:
                    if 'Title' in style.name or 'Heading' in style.name:
                        return 'Calibri Light'
                    else:
                        return 'Calibri'
                return doc.styles[style.name].font.name
            else:
                return get_font_name(style.base_style, style if last_style is None else last_style)
        else:
            return style.font.name

    errors = []
    with document.open() as d:
        doc = Document(d)
        for p in doc.paragraphs:
            p_font = get_font_name(p.style)
            if p_font != font_name:
                errors.append(f'Неправильный шрифт: {p_font} (должен быть {font_name})')

        for section in doc.sections:
            tm = round(section.top_margin.mm)
            if tm != top_margin:
                errors.append(f'Неправильное верхнее поле: {tm} мм (должно быть {top_margin} мм)')

            rm = round(section.right_margin.mm)
            if rm != right_margin:
                errors.append(f'Неправильное правое поле: {rm} мм (должно быть {right_margin} мм)')

            bm = round(section.bottom_margin.mm)
            if bm != bottom_margin:
                errors.append(f'Неправильное нижнее поле: {bm} мм (должно быть {bottom_margin} мм)')

            lm = round(section.left_margin.mm)
            if lm != left_margin:
                errors.append(f'Неправильное левое поле: {lm} мм (должно быть {left_margin} мм)')
    return set(errors)
