// Walks one slide's DOM and returns the primitives a PowerPoint shape tree needs:
// filled/stroked boxes, text leaves with their runs, pictures, and the CSS
// pseudo-elements the deck draws its rules and bullets with.
() => {
  const SL = document.querySelectorAll('.slide');
  const out = [];
  const px = v => Math.round(parseFloat(v) * 1000) / 1000;
  const rgb = v => {
    if (!v || v === 'none') return null;
    const m = v.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(',').map(s => parseFloat(s));
    if (p.length > 3 && p[3] === 0) return null;
    return { r: p[0] | 0, g: p[1] | 0, b: p[2] | 0, a: p.length > 3 ? p[3] : 1 };
  };
  // the deck draws its rings with spread-only box-shadows, inside and out
  const rings = v => {
    if (!v || v === 'none') return null;
    const out = [];
    v.split(/,(?![^(]*\))/).forEach(part => {
      const c = rgb(part);
      const nums = (part.replace(/rgba?\([^)]*\)/, '').match(/-?[\d.]+px/g) || []).map(parseFloat);
      if (!c || nums.length < 4) return;
      const [dx, dy, blur, spread] = nums;
      if (Math.abs(dx) > 0.5 || Math.abs(dy) > 0.5 || blur > 0.5 || spread <= 0.2) return;
      out.push({ c, w: spread, inset: /inset/.test(part) });
    });
    return out.length ? out : null;
  };

  const vis = e => {
    const c = getComputedStyle(e);
    return c.display !== 'none' && c.visibility !== 'hidden' && parseFloat(c.opacity) > 0.02;
  };

  SL.forEach((slide, si) => {
    const sr = slide.getBoundingClientRect();
    const items = [];
    const push = o => { if (o.w > 0.4 && o.h > 0.4) items.push(o); };

    const pseudo = (e, which, r) => {
      const c = getComputedStyle(e, which);
      if (!c || c.content === 'none' || c.display === 'none') return;
      const bg = rgb(c.backgroundColor);
      const bi = c.backgroundImage;
      if (!bg && (!bi || bi === 'none')) return;
      // resolve the pseudo box against its positioned parent
      const w = parseFloat(c.width), h = parseFloat(c.height);
      if (!(w > 0 && h > 0)) return;
      let x = r.left - sr.left, y = r.top - sr.top;
      if (c.position === 'absolute') {
        const pe = getComputedStyle(e);
        const base = pe.position === 'static' ? null : r;
        const bx = base ? base.left - sr.left : 0, by = base ? base.top - sr.top : 0;
        const L = c.left, T = c.top, R = c.right, B = c.bottom;
        x = bx + (L !== 'auto' ? parseFloat(L) : (R !== 'auto' ? (base ? base.width : sr.width) - parseFloat(R) - w : 0));
        y = by + (T !== 'auto' ? parseFloat(T) : (B !== 'auto' ? (base ? base.height : sr.height) - parseFloat(B) - h : 0));
      }
      push({ k: 'rect', x: px(x), y: px(y), w: px(w), h: px(h), fill: bg,
             radius: parseFloat(c.borderTopLeftRadius) || 0,
             grad: bi && bi !== 'none' ? bi.slice(0, 40) : null, pseudo: which });
    };

    const walk = e => {
      if (!vis(e)) return;
      const c = getComputedStyle(e);
      const r = e.getBoundingClientRect();
      const x = r.left - sr.left, y = r.top - sr.top;
      const tag = e.tagName.toLowerCase();

      if (tag === 'img') {
        push({ k: 'img', x: px(x), y: px(y), w: px(r.width), h: px(r.height),
               src: e.getAttribute('src'), nw: e.naturalWidth, nh: e.naturalHeight,
               fit: c.objectFit, pos: c.objectPosition, pad: [c.paddingTop, c.paddingRight, c.paddingBottom, c.paddingLeft].map(parseFloat) });
        return;
      }
      if (tag === 'svg') {
        push({ k: 'svg', x: px(x), y: px(y), w: px(r.width), h: px(r.height),
               html: e.outerHTML, color: c.color });
        return;
      }

      // the element's own box
      const bg = rgb(c.backgroundColor);
      const bimg = c.backgroundImage !== 'none' ? c.backgroundImage : null;
      const bw = ['Top', 'Right', 'Bottom', 'Left'].map(s => parseFloat(c['border' + s + 'Width']) || 0);
      const bc = ['Top', 'Right', 'Bottom', 'Left'].map(s => rgb(c['border' + s + 'Color']));
      const bs = ['Top', 'Right', 'Bottom', 'Left'].map(s => c['border' + s + 'Style']);
      const sh = rings(c.boxShadow);
      if (bg || bimg || bw.some(v => v > 0) || sh) {
        push({ k: 'rect', x: px(x), y: px(y), w: px(r.width), h: px(r.height),
               fill: bg, bimg: bimg, bw, bc, bs, rings: sh,
               radius: parseFloat(c.borderTopLeftRadius) || 0 });
      }
      pseudo(e, '::before', r); pseudo(e, '::after', r);

      // a leaf that holds text becomes one text box
      const kids = [...e.children];
      const ownText = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      const inlineOnly = kids.length > 0 && kids.every(k => {
        const kc = getComputedStyle(k);
        return kc.display.startsWith('inline') && !k.querySelector('img,svg');
      });
      if ((ownText && (kids.length === 0 || inlineOnly)) || (kids.length === 0 && e.textContent.trim())) {
        const runs = [];
        const collect = (node, style) => {
          node.childNodes.forEach(n => {
            if (n.nodeType === 3) {
              // HTML folds any run of whitespace to one space; the source's own
              // line breaks are not breaks in the rendered text
              const t = n.textContent.replace(/\s+/g, ' ');
              if (t.length) runs.push({ t, s: style });
            } else if (n.nodeType === 1) {
              if (n.tagName.toLowerCase() === 'br') { runs.push({ t: '\n', s: style }); return; }
              const kc = getComputedStyle(n);
              collect(n, { ff: kc.fontFamily, fs: px(kc.fontSize), fw: kc.fontWeight,
                           col: rgb(kc.color), ls: px(kc.letterSpacing === 'normal' ? 0 : kc.letterSpacing),
                           tt: kc.textTransform, it: kc.fontStyle });
            }
          });
        };
        const base = { ff: c.fontFamily, fs: px(c.fontSize), fw: c.fontWeight, col: rgb(c.color),
                       ls: px(c.letterSpacing === 'normal' ? 0 : c.letterSpacing),
                       tt: c.textTransform, it: c.fontStyle };
        collect(e, base);
        if (runs.some(r => r.t.trim())) {
          // the element box can be taller than its type (a flex cell centres its
          // line box), so take the vertical run from the rendered lines themselves
          let ty = y, th = r.height, vpad = true, one = false, align = c.textAlign;
          const pd = [c.paddingTop, c.paddingRight, c.paddingBottom, c.paddingLeft].map(v => parseFloat(v) || 0);
          try {
            const rg = document.createRange();
            rg.selectNodeContents(e);
            const ls = [...rg.getClientRects()].filter(q => q.width > 0.1 && q.height > 0.1);
            if (ls.length) {
              const t0 = Math.min(...ls.map(q => q.top)), b0 = Math.max(...ls.map(q => q.bottom));
              ty = t0 - sr.top; th = b0 - t0; vpad = false;
              one = ls.length === 1;
              // a flex cell centres its line without saying so in text-align
              if (align === 'start' || align === 'left') {
                const l0 = Math.min(...ls.map(q => q.left)) - (r.left + pd[3]);
                const r0 = (r.right - pd[1]) - Math.max(...ls.map(q => q.right));
                if (l0 > 1.5 && Math.abs(l0 - r0) <= Math.max(2, 0.12 * (l0 + r0))) align = 'center';
                else if (l0 > 1.5 && r0 <= 1.5) align = 'right';
              }
            }
          } catch (err) { /* keep the element box */ }
          if (!vpad) { pd[0] = 0; pd[2] = 0; }
          push({ k: 'text', x: px(x), y: px(ty), w: px(r.width), h: px(th),
                 runs, align, lh: c.lineHeight === 'normal' ? null : px(c.lineHeight),
                 pad: pd, one, mid: !vpad, valign: c.alignContent, fs: px(c.fontSize) });
        }
        return;
      }
      kids.forEach(walk);
    };

    walk(slide);
    out.push({ n: si + 1, dark: slide.classList.contains('dark'),
               bg: rgb(getComputedStyle(slide).backgroundColor), items });
  });
  return out;
}
