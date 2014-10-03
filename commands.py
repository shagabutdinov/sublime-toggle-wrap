import sublime
import sublime_plugin

class ToggleWrap(sublime_plugin.TextCommand):
  def run(self, edit, source, target, escape = None, unescape = None):
    selections = []
    for sel in self.view.sel():
      if sel.size() == 0:
        continue

      selections.append(self._toggle_wrap(edit, sel, source, target, escape,
        unescape))

    self.view.sel().clear()
    self.view.sel().add_all(selections)

  def _toggle_wrap(self, edit, sel, source, target, escape, unescape):
    text = self.view.substr(sel)

    source_chars = None
    for source_item in source:
      is_not_match = (
        (len(source_item[0]) > 0 and
          text[0:len(source_item[0])] != source_item[0]) or
        (len(source_item[1]) > 0 and
          text[-len(source_item[1]):] != source_item[1])
      )

      if not is_not_match:
        source_chars = source_item
        break

    if source_chars == None:
      return sublime.Region(sel.a, sel.b)

    text = self.view.substr(sel)
    if len(source_chars[0]) > 0:
      text = text[len(source_chars[0]):]

    if len(source_chars[1]) > 0:
      text = text[:-len(source_chars[1])]

    text = self.escape(text, escape, unescape)

    text = target[0] + text
    text = text + target[1]

    start = min(sel.a, sel.b)
    result = sublime.Region(start, start + len(text))
    self.view.replace(edit, sel, text)

    return result

  def escape(self, text, escape, unescape):
    if escape == None and unescape == None:
      return text

    text = text.replace('\\\\', '{{backslash-placeholder}}')

    for char in escape:
      text = text.replace('\\' + char, '{{escaped-placeholder}}')
      text = text.replace(char, '\\' + char)
      text = text.replace('{{escaped-placeholder}}', '\\' + char)

    for char in unescape:
      text = text.replace('\\' + char, char)

    text = text.replace('{{backslash-placeholder}}', '\\\\')

    return text