import re
import sys

from mkdocs.plugins import BasePlugin

def replace_fxn(m):
    args = m.group(1).split(',')
##    sys.stderr.write("args = %s\n" % args)
    txt = m.group(2)
    segs = txt.split('/')
    tag = args[0]
    if tag == 'bx':
        return f':material-numeric-{args[1]}-box:{{.em-label}}'        
    elif tag == 'cb':
        return f'<code class="language-ems"><span class="nb">{txt}</span></code>'
    elif tag == 'cf':
        return f'<code class="language-ems"><span class="nf">{txt}</span></code>'
    elif tag == 'ck':
        return f'<code class="language-ems"><span class="k">{txt}</span></code>'
    elif tag == 'cn':
        return f'<code class="language-ems"><span class="n">{txt}</span></code>'
    elif tag == 'ct':
        return f'<code class="language-ems"><span class="t">{txt}</span></code>'
    elif tag == 'cu':
        return f'<code class="language-ems"><span class="nn">{txt}</span></code>'
    elif tag == 'cx':
        return f'<code><span class="x">{txt}</span></code>'
    elif tag == 'es':
        return f'<code class="language-ems highlight"><span class="{args[1]}">{txt}</span></code>'
    elif tag == 'fn':
        return f'<code><span class="filename">{txt}</span></code>'
    elif tag == 'hc':
        return '<span class="em-float-right">Happy coding&thinsp;!!! &ensp; :full_moon_with_face:&nbsp;&nbsp;&nbsp;:computer:</span>'
    elif tag == 'hr':
        return f'<div class="em-break"></div>'
    elif tag == 'iu':
        return insert_unit(args, segs)
    elif tag == 'lb':
        return f'<span class="em-content-bundle-link">:material-package-variant:&nbsp;[{segs[0]}](/cargo/{txt})</span>'
    elif tag == 'lp':
        return f'<span class="em-content-pkg-link">:material-folder-open:&nbsp;[{segs[1]}](/cargo/{txt})</span>'
    elif tag == 'lq':
        return f'<span class="em-content-unit-link">:material-file:&nbsp;[{segs[1]}/{segs[2]}](/cargo/{txt})</span>'
    elif tag == 'lr':
        return f'<span class="em-lineref">[{args[2]}](#__codelineno-{args[1]}-{args[2]})</span>'
    elif tag == 'lu':
        return f'<span class="em-content-unit-link">:material-file:&nbsp;[{segs[2]}](/cargo/{txt})</span>'
    elif tag == 'sb':
        return f'<span class="em-bull">:material-circle:</span>'
    elif tag == 'sc':
        return screen_capture(args[1], args[2], txt)
    elif tag == 'se':
        return f'<code class="language-ems highlight"><span class="se">{txt}</span></code>'
    elif tag == 'sh':
        return f'<code class="language-ems highlight"><span class="si">{txt}</span></code>'
    elif tag == 'sp':
        return f'<span class="{args[1]}">{txt}</span>'
    elif tag == 'wn':
        return f'<span class="em-walk">:fontawesome-solid-person-walking-arrow-right:</span>'
    else:
        sys.stderr.write("*** unknown tag: %s\n" % tag)
        return f'<span style="color:red">${m.group(0)}</span>'

def insert_unit(args, segs):
    beg = int(args[1]) + 3 if len(args) > 1 else 4
    end = int(args[2]) + 3 if len(args) > 2 else 1000
    rng = f'hl_lines="{scale_rng(segs[3], beg-4)}"' if len(segs) > 3 else ''
    exc = ' [exc]' if len(args) > 1 else ''
    ticks = '' if end == 1000 else "```\n"
    return f"""
```zigem linenums="{beg-3}" title="{segs[1]}/{segs[2]}.em.zig{exc}" {rng}
--8<-- "docs/shelf/{segs[0]}/{segs[1]}/{segs[2]}.md:{beg}:{end}"
{ticks}
    """

def scale_rng(vals, off):
    fn = lambda m : str(int(m.group(0)) - off)
    return re.sub("\d+", fn, vals)

def screen_capture(num, src, cap):
    return f"""
<div markdown class="em-screen" id="fig{num}-dead">

<button onclick="screenSwap(document.getElementById('fig{num}-dead'), document.getElementById('fig{num}-live'))">:material-play-box-outline:</button>

<figure markdown>
<a markdown>![Image info](../../assets/screen-gifs/{src}.png)</a>
<figcaption>{cap}</figcaption> 
</figure>

</div>

<div markdown class="em-screen" id="fig{num}-live" style="display:none">

<button onclick="screenSwap(document.getElementById('fig{num}-live'), document.getElementById('fig{num}-dead'))">:material-rewind:</button>

<figure markdown id="fig{num}-live">
![Image info](../../assets/screen-gifs/{src}.gif)
<figcaption>{cap}</figcaption> 
</figure>

</div>
    """

class EmdownPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
##        sys.stderr.write("page %s\n" % page.url)
        res = re.sub(r'{\[(.+?)\](.*?)}', replace_fxn, markdown)
        return res
